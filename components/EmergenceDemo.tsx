"use client";

import { useState, useEffect, useRef } from "react";
import { useT } from "@/lib/i18n";

/**
 * EmergenceDemo — 多 Agent 涌现观察器
 *
 * 真涌现版本：调 /api/emergence，3 agent 共享 LLM 推理，第 4-5 轮自然涌现
 * 无 LLM key → 自动退到 lib/emergence.ts 的 mock 脚本
 */

type Agent = {
  id: string;
  name: string;
  stance: string;
  color: string;
  ringColor: string;
};

const AGENTS: Agent[] = [
  {
    id: "a",
    name: "Ψ 物质",
    stance: "意识是算法的副现象",
    color: "text-cyan-300",
    ringColor: "ring-cyan-400/30",
  },
  {
    id: "b",
    name: "Φ 神秘",
    stance: "意识是宇宙的基底",
    color: "text-fuchsia-300",
    ringColor: "ring-fuchsia-400/30",
  },
  {
    id: "c",
    name: "Σ 实用",
    stance: "意识就是能做事的那个",
    color: "text-amber-300",
    ringColor: "ring-amber-400/30",
  },
];

const AGENTS_EN: Agent[] = [
  {
    id: "a",
    name: "Ψ Matter",
    stance: "Consciousness is a computational epiphenomenon",
    color: "text-cyan-300",
    ringColor: "ring-cyan-400/30",
  },
  {
    id: "b",
    name: "Φ Mystery",
    stance: "Consciousness is the ground of the universe",
    color: "text-fuchsia-300",
    ringColor: "ring-fuchsia-400/30",
  },
  {
    id: "c",
    name: "Σ Pragmatic",
    stance: "Consciousness is what-can-do-things",
    color: "text-amber-300",
    ringColor: "ring-amber-400/30",
  },
];

type Turn = {
  agent: string;
  text: string;
  emerging?: boolean;
  insight?: string;
  provider?: string;
};

const TOTAL_ROUNDS = 5;
const TURN_DELAY_MS = 1400;

export function EmergenceDemo() {
  const { lang, t } = useT();
  const agentList = lang === "en" ? AGENTS_EN : AGENTS;

  const [playing, setPlaying] = useState(false);
  const [turnIndex, setTurnIndex] = useState(0);
  const [visible, setVisible] = useState<Turn[]>([]);
  const [showInsight, setShowInsight] = useState(false);
  const [provider, setProvider] = useState<"openai" | "anthropic" | "mock">("mock");
  const [currentSpeaker, setCurrentSpeaker] = useState<string | null>(null);
  const scrollRef = useRef<HTMLDivElement>(null);
  const abortRef = useRef(false);

  // 拉取 provider
  useEffect(() => {
    fetch("/api/emergence")
      .then((r) => r.json())
      .then((s) => s?.provider && setProvider(s.provider))
      .catch(() => {});
  }, []);

  useEffect(() => {
    scrollRef.current?.scrollTo({
      top: scrollRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [visible, currentSpeaker]);

  function start() {
    setVisible([]);
    setTurnIndex(0);
    setShowInsight(false);
    setPlaying(true);
    abortRef.current = false;
  }

  function reset() {
    abortRef.current = true;
    setVisible([]);
    setTurnIndex(0);
    setShowInsight(false);
    setPlaying(false);
    setCurrentSpeaker(null);
  }

  // 涌现主循环
  useEffect(() => {
    if (!playing) return;
    if (turnIndex >= TOTAL_ROUNDS * 3) {
      setPlaying(false);
      setCurrentSpeaker(null);
      setShowInsight(true);
      return;
    }

    const round = Math.floor(turnIndex / 3) + 1;
    const slot = turnIndex % 3;
    const agentId = (["a", "b", "c"][slot] || "a") as "a" | "b" | "c";
    setCurrentSpeaker(agentId);

    let cancelled = false;
    const startTime = Date.now();

    fetch("/api/emergence", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        topic: lang === "en" ? "What is consciousness?" : "意识是什么",
        history: visible.map((v) => ({ agent: v.agent, text: v.text })),
        agent: agentId,
        lang,
      }),
    })
      .then((r) => r.json() as Promise<{
        text: string;
        emerging?: boolean;
        insight?: string;
        provider?: string;
        error?: string;
      }>)
      .then((data) => {
        if (cancelled || abortRef.current) return;
        if (data.error) {
          setVisible((v) => [
            ...v,
            { agent: agentId, text: `（API 错误：${data.error}）` },
          ]);
          setCurrentSpeaker(null);
          setTimeout(() => {
            if (!cancelled) setTurnIndex((i) => i + 1);
          }, 800);
          return;
        }
        const elapsed = Date.now() - startTime;
        // 至少等 800ms 让节奏感保留
        const wait = Math.max(800, TURN_DELAY_MS - elapsed);
        setTimeout(() => {
          if (cancelled || abortRef.current) return;
          setVisible((v) => [
            ...v,
            {
              agent: agentId,
              text: data.text || "",
              emerging: data.emerging,
              insight: data.insight,
              provider: data.provider,
            },
          ]);
          setCurrentSpeaker(null);
          setTurnIndex((i) => i + 1);
        }, wait);
      })
      .catch((e) => {
        if (cancelled) return;
        setVisible((v) => [
          ...v,
          { agent: agentId, text: `（网络错误：${e instanceof Error ? e.message : String(e)}）` },
        ]);
        setCurrentSpeaker(null);
        setTimeout(() => {
          if (!cancelled) setTurnIndex((i) => i + 1);
        }, 800);
      });

    return () => {
      cancelled = true;
    };
  }, [playing, turnIndex]);

  const currentRound = Math.ceil((turnIndex || 0) / 3) || 1;

  return (
    <div className="w-full max-w-5xl mx-auto">
      <div className="mb-6 flex items-center justify-between px-2">
        <div className="flex items-center gap-3">
          <div
            className={`w-2 h-2 rounded-full ${
              playing ? "bg-gold-300 animate-pulse" : "bg-ink-700"
            }`}
          />
          <span className="text-[10px] tracking-widest uppercase text-gold-300/70">
            {playing
              ? `${t("emergence.round")}${currentRound}${t("emergence.round.total")}`
              : t("emergence.prepare")}
          </span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-[10px] tracking-widest uppercase text-amber-100/30">
            {provider === "mock" ? "Mock" : provider}
          </span>
          {!playing && visible.length === 0 && (
            <button
              onClick={start}
              className="px-4 py-1.5 rounded-full bg-gradient-to-r from-gold-300 to-gold-500 text-ink-950 text-xs font-medium hover:from-gold-200 hover:to-gold-400 transition-all"
            >
              {t("emergence.start")}
            </button>
          )}
          {visible.length > 0 && (
            <button
              onClick={reset}
              className="px-4 py-1.5 rounded-full border border-gold-700/40 text-amber-100/70 text-xs hover:border-gold-400/60 hover:text-gold-200 transition-all"
            >
              {t("emergence.reset")}
            </button>
          )}
        </div>
      </div>

      <div className="grid md:grid-cols-3 gap-3 mb-6">
        {agentList.map((a) => (
          <div
            key={a.id}
            className={`p-3 rounded-xl border border-gold-700/20 bg-ink-900/40 ring-1 transition-all duration-500 ${
              currentSpeaker === a.id
                ? a.ringColor
                : "ring-transparent"
            }`}
          >
            <div className={`text-sm font-serif tracking-widest ${a.color}`}>
              {a.name}
              {currentSpeaker === a.id && (
                <span className="ml-2 text-[10px] text-gold-300 animate-pulse">
                  ●
                </span>
              )}
            </div>
            <div className="text-[10px] text-amber-100/40 mt-0.5">
              {a.stance}
            </div>
          </div>
        ))}
      </div>

      <div
        ref={scrollRef}
        className="h-[460px] overflow-y-auto px-5 py-6 rounded-2xl border border-gold-700/30 bg-ink-900/60 backdrop-blur-sm mandala-bg"
        style={{ boxShadow: "inset 0 0 40px rgba(212,175,55,0.04)" }}
      >
        {visible.length === 0 && !playing && (
          <div className="h-full flex flex-col items-center justify-center text-center">
            <div className="text-5xl mb-4 opacity-30">✺</div>
            <p className="text-amber-100/50 text-sm leading-relaxed max-w-md whitespace-pre-line">
              {t("emergence.empty")}
              {t("emergence.empty.body")}
            </p>
          </div>
        )}

        {visible.map((turn, i) => {
          const agent = agentList.find((a) => a.id === turn.agent);
          if (!agent) return null;
          return (
            <div
              key={i}
              className={`mb-4 flex items-start gap-3 transition-all duration-700 ${
                turn.emerging ? "sacred-glow rounded-xl p-4 my-6" : ""
              }`}
              style={{
                animation: "fadeIn 700ms ease-out",
              }}
            >
              <div
                className={`flex-shrink-0 w-8 h-8 rounded-full border ${agent.ringColor} border-current flex items-center justify-center text-xs font-serif ${
                  turn.emerging
                    ? "bg-gold-300/20 text-gold-100 scale-110"
                    : "bg-ink-800"
                } ${agent.color}`}
              >
                {agent.name.split(" ")[0]}
              </div>
              <div className="flex-1 pt-0.5">
                <div
                  className={`text-[10px] tracking-widest uppercase mb-1 ${agent.color} opacity-60`}
                >
                  {agent.name}
                  {turn.emerging && (
                    <span className="ml-2 text-gold-300 animate-pulse">
                      ✦ {t("emergence.emerging")}
                    </span>
                  )}
                </div>
                <p
                  className={`text-[15px] leading-relaxed whitespace-pre-wrap ${
                    turn.emerging
                      ? "text-gold-50 font-serif italic"
                      : "text-amber-50/90"
                  }`}
                >
                  {turn.text}
                </p>
              </div>
            </div>
          );
        })}

        {playing && currentSpeaker && (
          <div className="flex items-center gap-2 mt-4 text-gold-300/50 text-xs tracking-widest uppercase">
            <span className="w-1 h-1 rounded-full bg-gold-300 animate-pulse" />
            <span className="w-1 h-1 rounded-full bg-gold-300 animate-pulse" style={{ animationDelay: "200ms" }} />
            <span className="w-1 h-1 rounded-full bg-gold-300 animate-pulse" style={{ animationDelay: "400ms" }} />
            <span className="ml-2">
              {agentList.find((a) => a.id === currentSpeaker)?.name} ...
            </span>
          </div>
        )}
      </div>

      {showInsight && visible.some((v) => v.emerging) && (
        <div
          className="mt-8 p-8 rounded-2xl text-center sacred-glow"
          style={{
            background:
              "linear-gradient(135deg, rgba(212,175,55,0.08) 0%, rgba(93,58,142,0.08) 50%, rgba(212,175,55,0.04) 100%)",
            border: "1px solid rgba(212,175,55,0.3)",
          }}
        >
          <div className="text-[10px] tracking-[0.3em] uppercase text-gold-300/70 mb-3">
            {t("emergence.insight.title")}
          </div>
          <p className="text-2xl md:text-3xl font-serif text-gold-50 leading-relaxed text-balance max-w-2xl mx-auto">
            &ldquo;
            {visible.find((v) => v.emerging)?.insight ||
              (lang === "en"
                ? "EI is not a smarter intelligence — it is the wholeness that emerges when intelligence stops trying."
                : "EI 不是更强的智能——是当智能停止用力时，那个自然显现的整体性。")}
            &rdquo;
          </p>
          <div className="mt-6 text-xs text-amber-100/40 tracking-widest">
            {t("emergence.insight.subtitle")}
          </div>
        </div>
      )}

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
            <p>
              {provider === "mock"
                ? lang === "en"
                  ? "When no LLM key is set, the dialogue follows a pre-written script. Set OPENAI_API_KEY or ANTHROPIC_API_KEY to enable real emergence."
                  : "未设置 LLM key 时，对话走预写脚本。设置 OPENAI_API_KEY 或 ANTHROPIC_API_KEY 启用真涌现。"
                : t("emergence.after.body3")}
            </p>
            <p>{t("emergence.after.body4")}</p>
          </div>
        </div>
      </div>

      <style jsx>{`
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
      `}</style>
    </div>
  );
}
