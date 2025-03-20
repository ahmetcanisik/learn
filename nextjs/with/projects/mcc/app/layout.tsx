import type { Metadata } from "next";
import { fontSans } from "@/config/font";
import "@/styles/globals.css";

export const metadata: Metadata = {
  title: "MCC",
  description: "Multi Cost Compare",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${fontSans.className} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
