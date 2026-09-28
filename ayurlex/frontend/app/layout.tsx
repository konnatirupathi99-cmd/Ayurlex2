import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Analytics } from "@vercel/analytics/next";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "AYURLEX | Intelligence Assistant",
  description: "Evidence-Grounded Ayurveda, IP & Regulatory Intelligence Assistant",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.className} bg-[var(--color-ayur-900)] text-[var(--color-ayur-25)] h-screen overflow-hidden flex`}>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
