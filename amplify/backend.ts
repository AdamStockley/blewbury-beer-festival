import { defineBackend } from "@aws-amplify/backend";
import { Stack } from "aws-cdk-lib";
import {
  CorsHttpMethod,
  HttpApi,
  HttpMethod,
} from "aws-cdk-lib/aws-apigatewayv2";
import { HttpLambdaIntegration } from "aws-cdk-lib/aws-apigatewayv2-integrations";
import { PolicyStatement } from "aws-cdk-lib/aws-iam";
import { sponsorshipContact } from "./functions/sponsorship-contact/resource";
import { generalContact } from "./functions/general-contact/resource";

const backend = defineBackend({
  sponsorshipContact,
  generalContact,
});

const apiStack = backend.createStack("sponsorship-api-stack");

const integration = new HttpLambdaIntegration(
  "SponsorshipContactIntegration",
  backend.sponsorshipContact.resources.lambda
);

const httpApi = new HttpApi(apiStack, "SponsorshipContactApi", {
  apiName: "bbf-sponsorship-contact",
  createDefaultStage: true,
  corsPreflight: {
    allowOrigins: [
      "http://localhost:4321",
      "https://main.d2nfagz8x81avw.amplifyapp.com",
      "https://blewbury-beer-festival.co.uk",
      "https://www.blewbury-beer-festival.co.uk",
    ],
    allowMethods: [CorsHttpMethod.POST],
    allowHeaders: ["content-type"],
  },
});

httpApi.addRoutes({
  path: "/sponsorship-enquiry",
  methods: [HttpMethod.POST],
  integration,
});

const contactIntegration = new HttpLambdaIntegration(
  "GeneralContactIntegration",
  backend.generalContact.resources.lambda
);

httpApi.addRoutes({
  path: "/contact-enquiry",
  methods: [HttpMethod.POST],
  integration: contactIntegration,
});

/*
 * The function only needs permission to send email using the
 * Blewbury Beer Festival SES identity.
 */
backend.sponsorshipContact.resources.lambda.addToRolePolicy(
  new PolicyStatement({
    actions: ["ses:SendEmail"],
    resources: [
      `arn:aws:ses:${Stack.of(apiStack).region}:${Stack.of(apiStack).account}:identity/blewbury-beer-festival.co.uk`,
      `arn:aws:ses:${Stack.of(apiStack).region}:${Stack.of(apiStack).account}:identity/admin@blewbury-beer-festival.co.uk`,
      `arn:aws:ses:${Stack.of(apiStack).region}:${Stack.of(apiStack).account}:configuration-set/my-first-configuration-set`,
    ],
  })
);

backend.generalContact.resources.lambda.addToRolePolicy(
  new PolicyStatement({
    actions: ["ses:SendEmail"],
    resources: [
      `arn:aws:ses:${Stack.of(apiStack).region}:${Stack.of(apiStack).account}:identity/blewbury-beer-festival.co.uk`,
      `arn:aws:ses:${Stack.of(apiStack).region}:${Stack.of(apiStack).account}:identity/admin@blewbury-beer-festival.co.uk`,
      `arn:aws:ses:${Stack.of(apiStack).region}:${Stack.of(apiStack).account}:configuration-set/my-first-configuration-set`,
    ],
  })
);

backend.addOutput({
  custom: {
    sponsorshipApi: {
      endpoint: httpApi.url,
      region: Stack.of(httpApi).region,
    },
  },
});
