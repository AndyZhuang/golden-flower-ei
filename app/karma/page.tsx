"use client";

import { useEffect, useState } from "react";
import { Nav } from "@/components/Nav";
import { Footer } from "@/components/Footer";
import { GoldenFlower } from "@/components/GoldenFlower";
import { useT } from "@/lib/i18n";

type KarmaEntry = {
  id: string;
  ts: string;
  action: "question" | "translation" | "review" | "insight";
  lang: string;
  tags: string[];
  contributor: string;
  content: string;
};

const ACTION_LABELS: Record<KarmaEntry["action"], { zh: string; en: string; color: string; ring: string }> = {
  question: { zh: "问", en: "Question", color: "text-amber-300", ring: "ring-amber-400/40" },
  translation: { zh: "译", en: "Translation", color: "text-cyan-300", ring: "ring-cyan-400/40" },
  review: { zh: "评", en: "Review", color: "text-fuchsia-300", ring: "ring-fuchsia-400/40" },
  insight: { zh: "悟", en: "Insight", color: "text-gold-200", ring: "ring-gold-400/50" },
};

export default function KarmaPage() {
  const { lang, t } = useT();
  const [entries, setEntries] = useState<KarmaEntry[]>([]);
  const [count, setCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [submitMsg, setSubmitMsg] = useState("");

  // 表单状态
  const [action, setAction] = useState<KarmaEntry["action"]>("question");
  const [content, setContent] = useState("");
  const [tags, setTags] = useState("");
  const [contributor, setContributor] = useState("");

  async function load() {
    setLoading(true);
    try {
      const r = await fetch("/api/karma?limit=50");
      const data = (await r.json()) as { entries: KarmaEntry[]; count: number };
      setEntries(data.entries || []);
      setCount(data.count || 0);
    } catch {
      // ignore
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load();
  }, []);

  async function submit() {
    if (!content.trim() || submitting) return;
    setSubmitting(true);
    setSubmitMsg("");
    try {
      const r = await fetch("/api/karma", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action,
          content: content.trim(),
          lang,
          tags,
          contributor: contributor.trim() || undefined,
        }),
      });
      const data = await r.json();
      if (data.ok) {
        setContent("");
        setTags("");
        setSubmitMsg(
          lang === "en"
            ? "✓ Your contribution has been added to the ledger."
            : "✓ 已记入 karma。"
        );
        load();
      } else {
        setSubmitMsg(`Error: ${data.error || "unknown"}`);
      }
    } catch (e) {
      setSubmitMsg(`Error: ${e instanceof Error ? e.message : String(e)}`);
    } finally {
      setSubmitting(false);
    }
  }

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
            <GoldenFlower size={120} pulse={false} />
          </div>
          <div className="text-[10px] tracking-[0.5em] uppercase text-gold-300/60 mb-3">
            Karma · 共 修
          </div>
          <h1 className="text-4xl md:text-5xl font-serif font-light text-gold-shimmer mb-5">
            {lang === "en" ? "Co-creation Ledger" : "共修 Karma"}
          </h1>
          <p className="text-amber-100/60 max-w-2xl mx-auto leading-relaxed text-balance">
            {lang === "en"
              ? "Each entry is a small step on the path. A real question, a faithful translation, a sincere review — together they become the field."
              : "每一条都是修行路上的一小步。一个真问题，一段忠实的翻译，一份诚实的评审——它们一起成为道场。"}
          </p>
        </div>

        {/* 贡献表单 */}
        <div className="max-w-3xl mx-auto mb-16 p-6 md:p-8 rounded-2xl border border-gold-700/30 bg-ink-900/60 sacred-glow">
          <div className="text-[10px] tracking-widest uppercase text-gold-300/50 mb-4">
            {lang === "en" ? "Contribute" : "贡献"}
          </div>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-2 mb-5">
            {(["question", "translation", "review", "insight"] as const).map(
              (a) => (
                <button
                  key={a}
                  onClick={() => setAction(a)}
                  className={`p-3 rounded-xl border text-left transition-all ${
                    action === a
                      ? `border-gold-300/60 bg-gold-300/10 ${ACTION_LABELS[a].ring} ring-1`
                      : "border-gold-700/20 hover:border-gold-400/30"
                  }`}
                >
                  <div
                    className={`text-xs tracking-widest uppercase ${ACTION_LABELS[a].color}`}
                  >
                    {ACTION_LABELS[a][lang === "en" ? "en" : "zh"]}
                  </div>
                  <div className="text-[10px] text-amber-100/40 mt-1">
                    {a === "question" && (lang === "en" ? "a real, felt question" : "一个真的、感受到的问题")}
                    {a === "translation" && (lang === "en" ? "between zh / en" : "中英互译")}
                    {a === "review" && (lang === "en" ? "a critical reflection" : "对某条贡献的反思")}
                    {a === "insight" && (lang === "en" ? "a spark of clarity" : "一念的清澈")}
                  </div>
                </button>
              )
            )}
          </div>

          <textarea
            value={content}
            onChange={(e) => setContent(e.target.value)}
            placeholder={
              lang === "en"
                ? "Write your contribution here…"
                : "写下你的贡献……"
            }
            rows={4}
            className="w-full bg-ink-800/60 border border-gold-700/20 rounded-xl p-4 text-amber-50 placeholder:text-amber-100/30 text-[15px] leading-relaxed outline-none focus:border-gold-400/50 transition-colors resize-none"
          />

          <div className="mt-3 flex flex-col md:flex-row gap-3">
            <input
              type="text"
              value={tags}
              onChange={(e) => setTags(e.target.value)}
              placeholder={lang === "en" ? "Tags (comma-separated)" : "标签（逗号分隔）"}
              className="flex-1 bg-ink-800/60 border border-gold-700/20 rounded-lg px-4 py-2 text-amber-50 placeholder:text-amber-100/30 text-sm outline-none focus:border-gold-400/50"
            />
            <input
              type="text"
              value={contributor}
              onChange={(e) => setContributor(e.target.value)}
              placeholder={lang === "en" ? "Your name (optional)" : "你的名字（可选）"}
              maxLength={40}
              className="md:w-48 bg-ink-800/60 border border-gold-700/20 rounded-lg px-4 py-2 text-amber-50 placeholder:text-amber-100/30 text-sm outline-none focus:border-gold-400/50"
            />
            <button
              onClick={submit}
              disabled={!content.trim() || submitting}
              className="px-6 py-2 rounded-lg bg-gradient-to-br from-gold-300 to-gold-500 text-ink-950 font-serif font-medium text-sm disabled:opacity-30 disabled:cursor-not-allowed hover:from-gold-200 hover:to-gold-400 transition-all"
              style={{ boxShadow: "0 0 20px rgba(212,175,55,0.2)" }}
            >
              {submitting ? "..." : lang === "en" ? "Contribute ✦" : "记入 ✦"}
            </button>
          </div>

          {submitMsg && (
            <div className="mt-3 text-sm text-gold-300/80">{submitMsg}</div>
          )}
        </div>

        {/* 列表 */}
        <div className="max-w-3xl mx-auto">
          <div className="flex items-center justify-between mb-4 px-1">
            <div className="text-[10px] tracking-widest uppercase text-gold-300/50">
              {lang === "en" ? "Recent" : "最近"}
            </div>
            <div className="text-[10px] tracking-widest uppercase text-amber-100/30">
              {count} {lang === "en" ? "entries" : "条"}
            </div>
          </div>

          {loading && (
            <div className="text-amber-100/40 text-sm text-center py-8">
              {lang === "en" ? "Loading..." : "载入中…"}
            </div>
          )}

          {!loading && entries.length === 0 && (
            <div className="text-amber-100/40 text-sm text-center py-12">
              {lang === "en"
                ? "No entries yet. Be the first to contribute."
                : "暂无贡献。来做第一个吧。"}
            </div>
          )}

          <div className="space-y-3">
            {entries.map((e) => {
              const a = ACTION_LABELS[e.action];
              return (
                <div
                  key={e.id}
                  className={`p-4 md:p-5 rounded-xl border border-gold-700/20 bg-ink-900/40 hover:border-gold-400/30 transition-all ${a.ring} ring-0 hover:ring-1`}
                >
                  <div className="flex items-center gap-2 mb-2">
                    <span className={`text-[10px] tracking-widest uppercase ${a.color}`}>
                      {a[lang === "en" ? "en" : "zh"]}
                    </span>
                    <span className="text-amber-100/30 text-[10px]">
                      {e.lang} · {new Date(e.ts).toLocaleString()}
                    </span>
                    {e.contributor && (
                      <span className="text-amber-100/30 text-[10px]">
                        · {e.contributor}
                      </span>
                    )}
                  </div>
                  <p className="text-amber-50/90 text-[15px] leading-relaxed whitespace-pre-wrap">
                    {e.content}
                  </p>
                  {e.tags && e.tags.length > 0 && (
                    <div className="mt-2 flex flex-wrap gap-1.5">
                      {e.tags.map((tag, i) => (
                        <span
                          key={i}
                          className="text-[10px] px-2 py-0.5 rounded-full border border-gold-700/30 text-gold-300/60"
                        >
                          #{tag}
                        </span>
                      ))}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      </section>

      <Footer />
    </main>
  );
}
