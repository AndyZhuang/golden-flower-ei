"use client";

import { Nav } from "@/components/Nav";
import { Footer } from "@/components/Footer";
import { DialogueDemo } from "@/components/DialogueDemo";
import { GoldenFlower } from "@/components/GoldenFlower";
import { useT } from "@/lib/i18n";

export default function DialoguePage() {
  const { t } = useT();
  return (
    <main className="relative min-h-screen">
      <Nav />

      <div className="fixed inset-0 -z-10">
        <div
          className="absolute inset-0"
          style={{
            background:
              "radial-gradient(ellipse at 50% 20%, #1a1530 0%, #06060a 60%, #000000 100%)",
          }}
        />
      </div>

      <section className="pt-32 pb-20 px-6">
        <div className="max-w-4xl mx-auto text-center mb-12">
          <div className="mb-6 flex justify-center">
            <GoldenFlower size={140} pulse={false} />
          </div>
          <div className="text-[10px] tracking-[0.5em] uppercase text-gold-300/60 mb-3">
            Dialogue · {t("nav.dialogue")}
          </div>
          <h1 className="text-4xl md:text-5xl font-serif font-light text-gold-shimmer mb-5">
            {t("dialogue.title")}
          </h1>
          <p className="text-amber-100/60 max-w-2xl mx-auto leading-relaxed text-balance">
            {t("dialogue.subtitle")}
          </p>
        </div>

        <DialogueDemo />

        <div className="max-w-2xl mx-auto mt-16 p-6 rounded-2xl border border-gold-700/20 bg-ink-900/40">
          <div className="text-[10px] tracking-widest uppercase text-gold-300/50 mb-3">
            {t("dialogue.principles")}
          </div>
          <ul className="space-y-3 text-sm text-amber-100/60 leading-relaxed">
            <li className="flex gap-3">
              <span className="text-gold-300/60">1.</span>
              <span>{t("dialogue.p1")}</span>
            </li>
            <li className="flex gap-3">
              <span className="text-gold-300/60">2.</span>
              <span>{t("dialogue.p2")}</span>
            </li>
            <li className="flex gap-3">
              <span className="text-gold-300/60">3.</span>
              <span>{t("dialogue.p3")}</span>
            </li>
          </ul>
        </div>
      </section>

      <Footer />
    </main>
  );
}
