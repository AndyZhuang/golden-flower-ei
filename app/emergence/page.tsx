"use client";

import { Nav } from "@/components/Nav";
import { Footer } from "@/components/Footer";
import { EmergenceDemo } from "@/components/EmergenceDemo";
import { GoldenFlower } from "@/components/GoldenFlower";
import { useT } from "@/lib/i18n";

export default function EmergencePage() {
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
        <div className="max-w-5xl mx-auto text-center mb-12">
          <div className="mb-6 flex justify-center">
            <GoldenFlower size={140} pulse={false} />
          </div>
          <div className="text-[10px] tracking-[0.5em] uppercase text-gold-300/60 mb-3">
            Emergence · {t("nav.emergence")}
          </div>
          <h1 className="text-4xl md:text-5xl font-serif font-light text-gold-shimmer mb-5">
            {t("emergence.title")}
          </h1>
          <p className="text-amber-100/60 max-w-2xl mx-auto leading-relaxed text-balance">
            {t("emergence.subtitle")}
          </p>
        </div>

        <EmergenceDemo />

        <div className="max-w-3xl mx-auto mt-20">
          <div className="text-center mb-8">
            <h2 className="text-2xl font-serif text-gold-50">
              {t("emergence.after.title")}
            </h2>
          </div>

          <div className="prose prose-invert prose-gold max-w-none">
            <div className="p-6 rounded-2xl border border-gold-700/20 bg-ink-900/40 leading-relaxed text-amber-100/70 text-[15px] space-y-4">
              <p>
                {t("emergence.after.body1")}{" "}
                <span className="text-gold-300/80">{t("emergence.after.body2")}</span>
              </p>
              <p>{t("emergence.after.body3")}</p>
              <p>{t("emergence.after.body4")}</p>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </main>
  );
}
