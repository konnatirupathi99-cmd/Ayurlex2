import type { Metadata } from "next";
import "./globals.css";

import { LanguageProvider } from "@/components/LanguageProvider";

export const metadata: Metadata = {
  title: "AYURLEX | AI Intelligence for Ayurvedic Innovation",
  description: "Analyse Ayurvedic innovations with structured AI intelligence, evidence-aware research, and clear insights.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-background text-foreground antialiased selection:bg-botanical-200 selection:text-botanical-900">
        <LanguageProvider>
          {children}
        </LanguageProvider>
      </body>
    </html>
  );
}
