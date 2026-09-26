import type { Config } from "tailwindcss";

export default {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        
        /* 1. Core neutral */
        ink: "var(--ink)",
        "ink-soft": "var(--ink-soft)",
        muted: "var(--muted)",
        line: "var(--line)",
        "line-strong": "var(--line-strong)",
        paper: "var(--paper)",
        surface: "var(--surface)",
        "surface-soft": "var(--surface-soft)",

        /* 2. Botanical green */
        sage: "var(--sage)",
        "sage-deep": "var(--sage-deep)",
        "sage-pale": "var(--sage-pale)",
        "sage-deep-hover": "var(--sage-deep-hover)",

        /* 3. Innovation accents */
        terra: "var(--terra)",
        "terra-pale": "var(--terra-pale)",
        amber: "var(--amber)",
        "amber-pale": "var(--amber-pale)",
        indigo: "var(--indigo)",
        "indigo-pale": "var(--indigo-pale)",
        teal: "var(--teal)",

        /* 4. Hero & Dark Botanical */
        hero: "var(--hero)",
        "hero-highlight": "var(--hero-highlight)",
        "hero-text": "var(--hero-text)",
        "hero-copy": "var(--hero-copy)",
        "hero-muted": "var(--hero-muted)",
        "hero-grid": "var(--hero-grid)",

        /* 5. Semantic state */
        primary: "var(--color-primary)",
        "primary-soft": "var(--color-primary-soft)",
        positive: "var(--color-positive)",
        "positive-soft": "var(--color-positive-soft)",
        attention: "var(--color-attention)",
        "attention-soft": "var(--color-attention-soft)",
        "human-context": "var(--color-human-context)",
        "human-context-soft": "var(--color-human-context-soft)",
        research: "var(--color-research)",
        "research-soft": "var(--color-research-soft)",
        live: "var(--color-live)",
        danger: "var(--color-danger)",
        "danger-soft": "var(--color-danger-soft)",
      },
    },
  },
  plugins: [],
} satisfies Config;
