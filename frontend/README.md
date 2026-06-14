# Aistriu Frontend

SvelteKit frontend for Aistriu, using TypeScript and Athbheochan Labs brand tokens.

## Requirements

- Node.js 20+
- npm 10+

## Local Development

From the `frontend` directory:

```bash
npm install
npm run dev
```

The app will be available at `http://localhost:5173`.

To expose the dev server on your local network:

```bash
npm run dev -- --host
```

## Useful Commands

```bash
npm run check
npm run build
npm run preview
```

## Project Structure

```text
frontend/
  src/
    lib/
      styles/
        tokens.css
    routes/
      about/
        +page.svelte
      +layout.svelte
      +page.svelte
    app.html
  package.json
  svelte.config.js
  tsconfig.json
  vite.config.ts
```

## Brand Tokens

Athbheochan Labs design tokens are defined in `src/lib/styles/tokens.css` as CSS custom properties for colours, fonts, spacing, radii, and shadows.
