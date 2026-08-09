import { SESv2Client, SendEmailCommand } from "@aws-sdk/client-sesv2";

const ses = new SESv2Client({ region: "eu-west-2" });

const ALLOWED_HOSTNAMES = new Set([
  "main.d2nfagz8x81avw.amplifyapp.com",
  "blewbury-beer-festival.co.uk",
  "www.blewbury-beer-festival.co.uk",
]);

const json = (statusCode: number, body: unknown) => ({
  statusCode,
  headers: {
    "content-type": "application/json",
  },
  body: JSON.stringify(body),
});

const clean = (value: unknown) =>
  typeof value === "string" ? value.trim() : "";

const validEmail = (value: string) =>
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);

export const handler = async (event: any) => {
  if (event.requestContext?.http?.method !== "POST") {
    return json(405, {
      ok: false,
      message: "Method not allowed.",
    });
  }

  let payload: any;

  try {
    payload = JSON.parse(event.body || "{}");
  } catch {
    return json(400, {
      ok: false,
      message: "Invalid request.",
    });
  }

  const businessName = clean(payload.businessName);
  const contactName = clean(payload.contactName);
  const email = clean(payload.email).toLowerCase();
  const phone = clean(payload.phone);
  const message = clean(payload.message);
  const website = clean(payload.website);
  const turnstileToken = clean(payload.turnstileToken);

  /*
   * Honeypot. Real visitors never see or complete this field.
   * Return success rather than advertising that the submission
   * has been classified as automated.
   */
  if (website) {
    return json(200, {
      ok: true,
      message: "Thanks — your sponsorship enquiry has been sent.",
    });
  }

  if (
    !businessName ||
    !contactName ||
    !email ||
    !message ||
    !turnstileToken
  ) {
    return json(400, {
      ok: false,
      message: "Please complete all required fields.",
    });
  }

  if (!validEmail(email)) {
    return json(400, {
      ok: false,
      message: "Please enter a valid email address.",
    });
  }

  if (
    businessName.length > 150 ||
    contactName.length > 150 ||
    email.length > 254 ||
    phone.length > 80 ||
    message.length > 3000
  ) {
    return json(400, {
      ok: false,
      message: "One or more fields are too long.",
    });
  }

  const turnstileSecret = process.env.TURNSTILE_SECRET_KEY;
  const recipient = process.env.SPONSORSHIP_RECIPIENT;

  if (!turnstileSecret || !recipient) {
    console.error("Sponsorship function secrets are not configured.");

    return json(503, {
      ok: false,
      message: "The enquiry form is temporarily unavailable.",
    });
  }

  let verification: {
    success?: boolean;
    hostname?: string;
    action?: string;
    "error-codes"?: string[];
  };

  try {
    const verifyResponse = await fetch(
      "https://challenges.cloudflare.com/turnstile/v0/siteverify",
      {
        method: "POST",
        headers: {
          "content-type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          secret: turnstileSecret,
          response: turnstileToken,
        }),
      }
    );

    verification = await verifyResponse.json();
  } catch (error) {
    console.error("Turnstile verification request failed", error);

    return json(503, {
      ok: false,
      message: "Verification is temporarily unavailable. Please try again.",
    });
  }

  const usingTurnstileTestSecret =
    turnstileSecret === "1x0000000000000000000000000000000AA";

  const hostnameValid =
    usingTurnstileTestSecret ||
    Boolean(
      verification.hostname &&
      ALLOWED_HOSTNAMES.has(verification.hostname)
    );

  const actionValid =
    !verification.action ||
    verification.action === "sponsorship";

  if (!verification.success || !hostnameValid || !actionValid) {
    console.warn("Turnstile validation rejected", {
      hostname: verification.hostname,
      action: verification.action,
      errors: verification["error-codes"],
    });

    return json(400, {
      ok: false,
      message: "CAPTCHA verification failed. Please try again.",
    });
  }

  const subject =
    `Barrel sponsorship enquiry — ${businessName}`;

  const bodyText = [
    "New Blewbury Beer Festival barrel sponsorship enquiry",
    "",
    `Business: ${businessName}`,
    `Contact: ${contactName}`,
    `Email: ${email}`,
    `Phone: ${phone || "Not provided"}`,
    "",
    "Message:",
    message,
  ].join("\n");

  try {
    await ses.send(
      new SendEmailCommand({
        FromEmailAddress: "admin@blewbury-beer-festival.co.uk",
        Destination: {
          ToAddresses: [recipient],
        },
        ReplyToAddresses: [email],
        Content: {
          Simple: {
            Subject: {
              Data: subject,
              Charset: "UTF-8",
            },
            Body: {
              Text: {
                Data: bodyText,
                Charset: "UTF-8",
              },
            },
          },
        },
      })
    );
  } catch (error) {
    console.error("SES delivery failed", error);

    return json(503, {
      ok: false,
      message:
        "We couldn't send your enquiry just now. Please try again shortly.",
    });
  }

  return json(200, {
    ok: true,
    message:
      "Thanks — your barrel sponsorship enquiry has been sent. We'll be in touch.",
  });
};
