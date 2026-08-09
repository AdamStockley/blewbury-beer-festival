import { defineFunction, secret } from "@aws-amplify/backend";

export const generalContact = defineFunction({
  name: "general-contact",
  entry: "./handler.ts",
  environment: {
    TURNSTILE_SECRET_KEY: secret("TURNSTILE_SECRET_KEY"),
    CONTACT_RECIPIENT: secret("CONTACT_RECIPIENT"),
  },
});
