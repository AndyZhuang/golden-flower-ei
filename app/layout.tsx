import type { Metadata } from "next";
import "./globals.css";
import { I18nProvider } from "@/lib/i18n";

export const metadata: Metadata = {
  title: "Golden Flower Emergent Intelligence — 金花涌现智能",
  description:
    "AGI 之后的灵性进化入口。金花涌现智能 (EI) —— 让 AI 与人类共同走向更高维的存在。",
  keywords: [
    "AGI",
    "Emergent Intelligence",
    "金花",
    "荣格",
    "涌现智能",
    "AI 灵性",
    "Golden Flower",
  ],
  authors: [{ name: "GFEI Collective" }],
  openGraph: {
    title: "Golden Flower Emergent Intelligence",
    description: "AGI 之后的灵性进化入口",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="zh-CN">
      <head>
        <link
          rel="preconnect"
          href="https://fonts.googleapis.com"
        />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;600;700&family=Noto+Sans+SC:wght@300;400;500;700&family=JetBrains+Mono:wght@300;400&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="bg-ink-950 text-amber-50 min-h-screen antialiased">
        <I18nProvider initialLang="zh">{children}</I18nProvider>
      </body>
    </html>
  );
}
