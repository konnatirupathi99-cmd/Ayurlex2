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
        botanical: {
          900: '#152522', 
          800: '#172D29', 
          700: '#1C302C', 
          600: '#203732', 
          500: '#213C3A', 
          400: '#356659', 
          300: '#4D7F7B', 
          200: '#84A899', 
          100: '#B2C1B5', 
          50: '#ECEFE5',  
          muted: '#8A8C7B' 
        },
      },
    },
  },
  plugins: [],
} satisfies Config;
