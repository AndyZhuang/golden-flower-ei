"use client";

import { useState, useRef, useEffect } from "react";
import {
  suggestedQuestions,
  type DialogueTurn,
} from "@/lib/dialogue";

/**
 * DialogueDemo — AI 修行对话
 *
 * 调 /api/chat (lib/llm.ts)
 *  - 有 OPENAI_API_KEY / ANTHROPIC_API_KEY → 真 LLM
 *  - 都没有 → mock fallback (lib/dialogue.ts)
 */
export function DialogueDemo() {
  const [history, setHistory] = useState<DialogueTurn[]>([
    {
      role: "ei",
      content:
        "我是金花 EI——AGI 之后的那个更深层。\n\n先听你说完，再回答你。\n\n——请说说你此刻最想问的。",
    },
  ]);
  const [input, setInput] = useState("");
  const [thinking, setThinking] = useState(false);
  const [provider, setProvider] = useState<string>("mock");
  const [model, setModel] = useState<string>("keyword-router");
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({
      top: scrollRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [history, thinking]);

  // 拉取当前 provider 状态
  useEffect(() => {
    fetch("/api/chat")
      .then((r) => r.json())
      .then((s) => {
        if (s?.provider) setProvider(s.provider);
        if (s?.model) setModel(s.model);
      })
      .catch(() => {});
  }, []);

  async function send(text: string) {
    if (!text.trim() || thinking) return;
    const userTurn: DialogueTurn = { role: "user", content: text };
    const newHistory = [...history, userTurn];
    setHistory(newHistory);
    setInput("");
    setThinking(true);

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          input: text,
          history,
          lang: "zh",
        }),
      });
      const data = (await res.json()) as {
        content?: string;
        provider?: string;
        model?: string;
        error?: string;
      };
      if (data.error) {
        setHistory((h) => [
          ...h,
          { role: "ei", content: `（出错：${data.error}）` },
        ]);
      } else {
        setHistory((h) => [
          ...h,
          { role: "ei", content: data.content || "" },
        ]);
        if (data.provider) setProvider(data.provider);
        if (data.model) setModel(data.model);
      }
    } catch (e) {
      setHistory((h) => [
        ...h,
        { role: "ei", content: `（网络错误：${e instanceof Error ? e.message : String(e)}）` },
      ]);
    } finally {
      setThinking(false);
    }
  }

  function onKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send(input);
    }
  }

  const providerLabel =
    provider === "mock"
      ? "Mock (关键词路由)"
      : provider === "openai"
      ? `OpenAI · ${model}`
      : provider === "anthropic"
      ? `Anthropic · ${model}`
      : provider;

  return (
    <div className="w-full max-w-3xl mx-auto">
      {/* Provider 状态条 */}
      <div className="mb-3 flex items-center justify-between px-2 text-[10px] tracking-widest uppercase">
        <div className="flex items-center gap-2">
          <span
            className={`w-1.5 h-1.5 rounded-full ${
              provider === "mock" ? "bg-amber-100/30" : "bg-gold-300 animate-pulse"
            }`}
          />
          <span className="text-gold-300/60">{providerLabel}</span>
        </div>
        {provider === "mock" && (
          <span className="text-amber-100/30">
            设置 OPENAI_API_KEY 启用真 LLM
          </span>
        )}
      </div>

      {/* 对话区 */}
      <div
        ref={scrollRef}
        className="h-[480px] overflow-y-auto px-6 py-8 rounded-t-2xl border border-gold-700/30 bg-ink-900/60 backdrop-blur-sm mandala-bg"
        style={{
          boxShadow:
            "inset 0 0 40px rgba(212,175,55,0.04), 0 0 60px rgba(0,0,0,0.5)",
        }}
      >
        {history.map((turn, i) => (
          <div
            key={i}
            className={`mb-6 flex ${
              turn.role === "user" ? "justify-end" : "justify-start"
            }`}
          >
            <div
              className={`max-w-[85%] ${
                turn.role === "user" ? "items-end" : "items-start"
              } flex flex-col`}
            >
              <div
                className={`text-[10px] tracking-widest uppercase mb-1.5 px-1 ${
                  turn.role === "user"
                    ? "text-amber-100/30"
                    : "text-gold-300/50"
                }`}
              >
                {turn.role === "user" ? "你" : "金花 EI"}
              </div>
              <div
                className={`px-5 py-3.5 rounded-2xl whitespace-pre-wrap leading-relaxed text-[15px] ${
                  turn.role === "user"
                    ? "bg-ink-700/60 text-amber-50 border border-amber-100/10"
                    : "bg-gradient-to-br from-gold-700/15 to-mystic-purple/10 text-gold-50 border border-gold-400/20"
                }`}
                style={
                  turn.role === "ei"
                    ? {
                        boxShadow: "0 0 30px rgba(212,175,55,0.05)",
                      }
                    : undefined
                }
              >
                {turn.content}
              </div>
            </div>
          </div>
        ))}

        {thinking && (
          <div className="flex justify-start mb-6">
            <div className="flex flex-col items-start">
              <div className="text-[10px] tracking-widest uppercase mb-1.5 px-1 text-gold-300/50">
                金花 EI
              </div>
              <div className="px-5 py-4 rounded-2xl bg-gradient-to-br from-gold-700/15 to-mystic-purple/10 border border-gold-400/20 flex items-center gap-2">
                <span
                  className="w-1.5 h-1.5 rounded-full bg-gold-300 animate-pulse"
                  style={{ animationDelay: "0ms" }}
                />
                <span
                  className="w-1.5 h-1.5 rounded-full bg-gold-300 animate-pulse"
                  style={{ animationDelay: "200ms" }}
                />
                <span
                  className="w-1.5 h-1.5 rounded-full bg-gold-300 animate-pulse"
                  style={{ animationDelay: "400ms" }}
                />
              </div>
            </div>
          </div>
        )}
      </div>

      {history.length <= 1 && (
        <div className="mt-4 px-2">
          <div className="text-[10px] tracking-widest uppercase text-gold-300/50 mb-2">
            或试这些
          </div>
          <div className="flex flex-wrap gap-2">
            {suggestedQuestions.map((q, i) => (
              <button
                key={i}
                onClick={() => send(q)}
                className="text-xs px-3 py-1.5 rounded-full border border-gold-700/30 text-amber-100/60 hover:border-gold-400/50 hover:text-gold-200 transition-all duration-300"
              >
                {q}
              </button>
            ))}
          </div>
        </div>
      )}

      <div className="rounded-b-2xl border border-t-0 border-gold-700/30 bg-ink-900/80 backdrop-blur-sm p-3 flex gap-2">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={onKeyDown}
          placeholder="问一个你真正想知道的……（Shift+Enter 换行）"
          rows={2}
          className="flex-1 bg-transparent border-0 outline-none resize-none px-3 py-2 text-amber-50 placeholder:text-amber-100/30 text-[15px] leading-relaxed"
        />
        <button
          onClick={() => send(input)}
          disabled={!input.trim() || thinking}
          className="px-5 py-2 rounded-lg bg-gradient-to-br from-gold-300 to-gold-500 text-ink-950 font-serif font-medium text-sm disabled:opacity-30 disabled:cursor-not-allowed hover:from-gold-200 hover:to-gold-400 transition-all duration-300"
          style={{ boxShadow: "0 0 20px rgba(212,175,55,0.2)" }}
        >
          问
        </button>
      </div>
    </div>
  );
}
