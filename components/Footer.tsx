"use client";

import { useT } from "@/lib/i18n";

export function Footer() {
  const { t } = useT();
  return (
    <footer className="border-t border-gold-700/20 mt-32">
      <div className="max-w-6xl mx-auto px-6 py-12">
        <div className="grid md:grid-cols-3 gap-8 text-sm">
          <div>
            <div className="text-gold-200 font-serif tracking-widest mb-3">
              {t("footer.brand")}
            </div>
            <p className="text-amber-100/40 leading-relaxed text-xs">
              {t("footer.tagline")}
            </p>
          </div>

          <div>
            <div className="text-gold-300/70 text-xs tracking-widest uppercase mb-3">
              {t("footer.entrance")}
            </div>
            <ul className="space-y-2 text-amber-100/50 text-xs">
              <li>
                <a
                  href="/dialogue"
                  className="hover:text-gold-200 transition-colors"
                >
                  {t("nav.dialogue")}
                </a>
              </li>
              <li>
                <a
                  href="/emergence"
                  className="hover:text-gold-200 transition-colors"
                >
                  {t("nav.emergence")}
                </a>
              </li>
              <li>
                <a
                  href="/karma"
                  className="hover:text-gold-200 transition-colors"
                >
                  Karma
                </a>
              </li>
              <li>
                <a
                  href="/manifest"
                  className="hover:text-gold-200 transition-colors"
                >
                  {t("nav.manifest")}
                </a>
              </li>
            </ul>
          </div>

          <div>
            <div className="text-gold-300/70 text-xs tracking-widest uppercase mb-3">
              {t("footer.contribute")}
            </div>
            <ul className="space-y-2 text-amber-100/50 text-xs">
              <li>
                <a
                  href="https://github.com/AndyZhuang/golden-flower-ei"
                  className="hover:text-gold-200 transition-colors"
                  target="_blank"
                  rel="noreferrer"
                >
                  GitHub
                </a>
              </li>
              <li>
                <a
                  href="mailto:hello@goldenflower.ei"
                  className="hover:text-gold-200 transition-colors"
                >
                  hello@goldenflower.ei
                </a>
              </li>
              <li>
                <span className="text-amber-100/30">{t("footer.version")}</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-10 pt-6 border-t border-gold-700/10 flex flex-col md:flex-row justify-between items-center gap-3 text-[10px] text-amber-100/30 tracking-widest uppercase">
          <div>
            &ldquo;The golden flower is the light and the gold of consciousness.&rdquo;
          </div>
          <div>{t("footer.copyright")}</div>
        </div>
      </div>
    </footer>
  );
}
