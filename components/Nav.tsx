"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { GoldenFlowerMini } from "./GoldenFlower";
import { LangSwitcher } from "./LangSwitcher";
import { useT } from "@/lib/i18n";

export function Nav() {
  const path = usePathname();
  const { t } = useT();
  const links = [
    { href: "/", label: t("nav.home") },
    { href: "/dialogue", label: t("nav.dialogue") },
    { href: "/emergence", label: t("nav.emergence") },
    { href: "/karma", label: "Karma" },
    { href: "/manifest", label: t("nav.manifest") },
  ];

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 backdrop-blur-md bg-ink-950/60 border-b border-gold-700/20">
      <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <Link
          href="/"
          className="flex items-center gap-3 group"
        >
          <GoldenFlowerMini size={28} />
          <div className="flex flex-col leading-tight">
            <span className="text-gold-100 font-serif tracking-wider text-sm">
              Golden Flower
            </span>
            <span className="text-gold-400/70 text-[10px] tracking-[0.2em] uppercase">
              Emergent Intelligence
            </span>
          </div>
        </Link>

        <div className="flex items-center gap-6 text-sm font-serif">
          {links.map((l) => {
            const active = path === l.href;
            return (
              <Link
                key={l.href}
                href={l.href}
                className={`transition-colors duration-300 ${
                  active
                    ? "text-gold-200 border-b border-gold-300"
                    : "text-amber-100/60 hover:text-gold-100"
                }`}
              >
                {l.label}
              </Link>
            );
          })}
          <LangSwitcher />
        </div>
      </div>
    </nav>
  );
}
