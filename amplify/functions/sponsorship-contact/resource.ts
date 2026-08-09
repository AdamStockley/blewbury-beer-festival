import { defineFunction, secret } from "@aws-amplify/backend";

export const sponsorshipContact = defineFunction({
  name: "sponsorship-contact",
  entry: "./handler.ts",
  environment: {
    TURNSTILE_SECRET_KEY: secret("TURNSTILE_SECRET_KEY"),
    SPONSORSHIP_RECIPIENT: secret("SPONSORSHIP_RECIPIENT"),
  },
});
