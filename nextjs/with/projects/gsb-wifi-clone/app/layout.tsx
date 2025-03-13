import type { Metadata } from "next";
import "@/ui/styles/globals.css";
import "@/ui/styles/gsb.css";

export const metadata: Metadata = {
  title: "GSB Wifi Clone",
  description: "GSB Wifi Clone with Next.js",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className="antialiased"
      >
        {children}
      </body>
    </html>
  );
}
