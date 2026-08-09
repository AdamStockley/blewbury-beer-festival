import { SESv2Client, SendEmailCommand } from "@aws-sdk/client-sesv2";

const ses = new SESv2Client({ region: "eu-west-2" });

const ALLOWED_HOSTNAMES = new Set([
  "main.d2nh6jvn6p8uji.amplifyapp.com",
  "blewbury-beer-festival.co.uk",
  "www.blewbury-beer-festival.co.uk",
]);

const json = (statusCode: number, body: unknown) => ({
  statusCode,
  headers: { "content-type": "application/json" },
  body: JSON.stringify(body),
});

const clean = (value: unknown) =>
  typeof value === "string" ? value.trim() : "";

const validEmail = (value: string) =>
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);

export const handler = async (event: any) => {
  if (event.requestContext?.http?.method !== "POST") {
    return json(405, { ok: false, message: "Method not allowed." });
  }

  let payload: any;

  try {
    payload = JSON.parse(event.body || "{}");
  } catch {
    return json(400, { ok: false, message: "Invalid request." });
  }

  const name = clean(payload.name);
  const email = clean(payload.email).toLowerCase();
  const subject = clean(payload.subject);
  const message = clean(payload.message);
  const website = clean(payload.website);
  const turnstileToken = clean(payload.turnstileToken);

  if (website) {
    return json(200, {
      ok: true,
      message: "Thanks — your message has been sent.",
    });
  }

  if (!name || !email || !subject || !message || !turnstileToken) {
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
    name.length > 150 ||
    email.length > 254 ||
    subject.length > 180 ||
    message.length > 3000
  ) {
    return json(400, {
      ok: false,
      message: "One or more fields are too long.",
    });
  }

  const turnstileSecret = process.env.TURNSTILE_SECRET_KEY;
  const recipient = process.env.CONTACT_RECIPIENT;

  if (!turnstileSecret || !recipient) {
    return json(503, {
      ok: false,
      message: "The contact form is temporarily unavailable.",
    });
  }

  let verification: {
    success?: boolean;
    hostname?: string;
    action?: string;
    "error-codes"?: string[];
  };

  try {
    const response = await fetch(
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

    verification = await response.json();
  } catch (error) {
    console.error("Turnstile request failed", error);

    return json(503, {
      ok: false,
      message: "Verification is temporarily unavailable. Please try again.",
    });
  }

  const usingTestSecret =
    turnstileSecret === "1x0000000000000000000000000000000AA";

  const hostnameValid =
    usingTestSecret ||
    Boolean(
      verification.hostname &&
      ALLOWED_HOSTNAMES.has(verification.hostname)
    );

  const actionValid =
    !verification.action ||
    verification.action === "contact";

  if (!verification.success || !hostnameValid || !actionValid) {
    return json(400, {
      ok: false,
      message: "CAPTCHA verification failed. Please try again.",
    });
  }

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
              Data: `Festival enquiry — ${subject}`,
              Charset: "UTF-8",
            },
            Body: {
              Text: {
                Data: [
                  "New Blewbury Beer Festival enquiry",
                  "",
                  `Name: ${name}`,
                  `Email: ${email}`,
                  `Subject: ${subject}`,
                  "",
                  "Message:",
                  message,
                ].join("\n"),
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
      message: "We couldn't send your message just now. Please try again shortly.",
    });
  }

  return json(200, {
    ok: true,
    message: "Thanks — your message has been sent.",
  });
};
