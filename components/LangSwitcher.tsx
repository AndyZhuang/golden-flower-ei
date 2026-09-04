"use client";

import { useT } from "@/lib/i18n";

export function LangSwitcher() {
  const { lang, setLang, t } = useT();
  return (
    <button
      onClick={() => setLang(lang === "zh" ? "en" : "zh")}
      className="ml-2 text-[10px] tracking-widest uppercase text-gold-300/60 hover:text-gold-100 transition-colors px-2 py-1 border border-gold-700/30 rounded-full"
      aria-label="Switch language"
    >
      {t("lang.switch")}
    </button>
  );
}
