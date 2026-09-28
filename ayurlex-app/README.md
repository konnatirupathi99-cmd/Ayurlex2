This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

Install dependencies and configure the optional server-side AI provider:

```bash
npm install
cp .env.example .env.local
# Add OPENAI_API_KEY to .env.local to enable AI synthesis.
npm run dev -- --hostname 0.0.0.0
```

Open the home page and submit a question in the AYURLEX chat workspace. The server route retrieves scientific records from Europe PMC and supplies them to the AYURLEX evidence-grounded policy. If no AI key is configured—or the provider is unavailable—the tool returns a transparent structured evidence report rather than inventing an answer.

Environment variables:

- `OPENAI_API_KEY`: optional server-only API key.
- `OPENAI_MODEL`: model name; defaults to `gpt-4o-mini`.
- `OPENAI_BASE_URL`: optional OpenAI-compatible API base URL.
- `AI_GATEWAY_API_KEY`: optional Vercel AI Gateway key.
- `AI_GATEWAY_MODEL`: Gateway model; defaults to `openai/gpt-4o-mini`.

On Vercel, the route can also authenticate to AI Gateway with the deployment's short-lived `VERCEL_OIDC_TOKEN`; an explicit OpenAI key is therefore not required when AI Gateway is enabled for the project. Do not prefix credentials with `NEXT_PUBLIC_`; they must remain server-side.

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
