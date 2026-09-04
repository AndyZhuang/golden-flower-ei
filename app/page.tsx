"use client";

import Link from "next/link";
import { GoldenFlower } from "@/components/GoldenFlower";
import { Nav } from "@/components/Nav";
import { Footer } from "@/components/Footer";
import { useT } from "@/lib/i18n";

export default function HomePage() {
  const { t } = useT();

  return (
    <main className="relative min-h-screen overflow-hidden">
      <Nav />

      <div className="fixed inset-0 -z-10">
        <div
          className="absolute inset-0"
          style={{
            background:
              "radial-gradient(ellipse at 50% 30%, #1a1530 0%, #06060a 60%, #000000 100%)",
          }}
        />
        <div
          className="absolute inset-0 opacity-30"
          style={{
            backgroundImage:
              "radial-gradient(circle at 20% 30%, rgba(212,175,55,0.05) 0%, transparent 40%), radial-gradient(circle at 80% 70%, rgba(93,58,142,0.08) 0%, transparent 40%)",
          }}
        />
      </div>

      <section className="relative min-h-screen flex flex-col items-center justify-center px-6 pt-20">
        <div className="mb-8 floating">
          <GoldenFlower size={420} />
        </div>

        <div className="text-center max-w-3xl">
          <div className="mb-4 text-[10px] tracking-[0.5em] uppercase text-gold-300/60">
            Golden Flower · Emergent Intelligence
          </div>
          <h1 className="text-5xl md:text-7xl font-serif font-light text-gold-shimmer mb-6 tracking-wide">
            {t("site.title")}
          </h1>
          <p className="text-lg md:text-xl text-amber-100/70 leading-relaxed font-serif max-w-2xl mx-auto text-balance">
            {t("site.subtitle")}
            <br />
            {t("site.tagline")}
          </p>
        </div>

        <div className="mt-12 flex flex-wrap items-center justify-center gap-4">
          <Link
            href="/dialogue"
            className="group px-7 py-3 rounded-full bg-gradient-to-r from-gold-300 via-gold-200 to-gold-300 text-ink-950 font-serif tracking-widest text-sm transition-all duration-500 hover:scale-105"
            style={{ boxShadow: "0 0 40px rgba(212,175,55,0.3)" }}
          >
            <span className="inline-block group-hover:translate-x-1 transition-transform">
              {t("home.cta.dialogue")}
            </span>
          </Link>
          <Link
            href="/emergence"
            className="px-7 py-3 rounded-full border border-gold-400/40 text-gold-200 font-serif tracking-widest text-sm hover:bg-gold-400/10 hover:border-gold-300 transition-all duration-500"
          >
            {t("home.cta.emergence")}
          </Link>
          <Link
            href="/manifest"
            className="px-7 py-3 rounded-full text-amber-100/60 font-serif tracking-widest text-sm hover:text-gold-200 transition-colors"
          >
            {t("home.cta.manifest")}
          </Link>
        </div>

        <div className="absolute bottom-10 left-1/2 -translate-x-1/2 text-amber-100/30 text-xs tracking-widest uppercase animate-pulse">
          ↓
        </div>
      </section>

      <section className="relative max-w-6xl mx-auto px-6 py-32">
        <div className="text-center mb-20">
          <div className="text-[10px] tracking-[0.5em] uppercase text-gold-300/60 mb-3">
            Three Propositions
          </div>
          <h2 className="text-3xl md:text-4xl font-serif font-light text-gold-50 text-balance">
            {t("home.propositions.title")}
          </h2>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          <Proposition num="I" title={t("home.propositions.i.title")} body={t("home.propositions.i.body")} />
          <Proposition num="II" title={t("home.propositions.ii.title")} body={t("home.propositions.ii.body")} />
          <Proposition num="III" title={t("home.propositions.iii.title")} body={t("home.propositions.iii.body")} />
        </div>
      </section>

      <section className="relative max-w-5xl mx-auto px-6 py-20">
        <div className="grid md:grid-cols-2 gap-5">
          <Link
            href="/dialogue"
            className="group p-8 rounded-2xl border border-gold-700/30 bg-gradient-to-br from-ink-900/80 to-ink-800/40 hover:border-gold-300/60 transition-all duration-500 sacred-glow"
          >
            <div className="text-[10px] tracking-widest uppercase text-gold-300/70 mb-3">
              {t("home.entrance.dialogue")}
            </div>
            <h3 className="text-2xl font-serif text-gold-50 mb-3 group-hover:text-gold-shimmer transition-colors">
              {t("home.entrance.dialogue.title")}
            </h3>
            <p className="text-amber-100/60 leading-relaxed text-sm whitespace-pre-line">
              {t("home.entrance.dialogue.body")}
            </p>
            <div className="mt-6 text-gold-300/50 text-xs tracking-widest group-hover:translate-x-1 transition-transform">
              {t("nav.dialogue")} →
            </div>
          </Link>

          <Link
            href="/emergence"
            className="group p-8 rounded-2xl border border-gold-700/30 bg-gradient-to-br from-ink-900/80 to-ink-800/40 hover:border-gold-300/60 transition-all duration-500 sacred-glow"
          >
            <div className="text-[10px] tracking-widest uppercase text-gold-300/70 mb-3">
              {t("home.entrance.emergence")}
            </div>
            <h3 className="text-2xl font-serif text-gold-50 mb-3 group-hover:text-gold-shimmer transition-colors">
              {t("home.entrance.emergence.title")}
            </h3>
            <p className="text-amber-100/60 leading-relaxed text-sm whitespace-pre-line">
              {t("home.entrance.emergence.body")}
            </p>
            <div className="mt-6 text-gold-300/50 text-xs tracking-widest group-hover:translate-x-1 transition-transform">
              {t("nav.emergence")} →
            </div>
          </Link>
        </div>
      </section>

      <section className="relative max-w-3xl mx-auto px-6 py-24 text-center">
        <div className="text-6xl text-gold-300/30 font-serif leading-none mb-4">
          &ldquo;
        </div>
        <blockquote className="text-2xl md:text-3xl font-serif text-gold-50 leading-relaxed text-balance italic font-light">
          {t("home.quote.line1")}
          <br />
          {t("home.quote.line2")}
        </blockquote>
        <div className="mt-6 text-amber-100/40 text-sm tracking-widest">
          {t("home.quote.cite")}
        </div>
      </section>

      <Footer />
    </main>
  );
}

function Proposition({
  num,
  title,
  body,
}: {
  num: string;
  title: string;
  body: string;
}) {
  return (
    <div className="p-6 rounded-2xl border border-gold-700/20 bg-ink-900/40 backdrop-blur-sm hover:border-gold-400/40 transition-all duration-500 group">
      <div className="text-4xl font-serif text-gold-300/40 mb-3 group-hover:text-gold-300/70 transition-colors">
        {num}
      </div>
      <h3 className="text-xl font-serif text-gold-50 mb-3 leading-snug">
        {title}
      </h3>
      <p className="text-amber-100/60 leading-relaxed text-sm">{body}</p>
    </div>
  );
}
