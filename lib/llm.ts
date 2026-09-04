/**
 * llm.ts — LLM 客户端 (OpenAI / Anthropic 适配)
 *
 * 设计原则：
 * 1. 优先用 OPENAI_API_KEY（OpenAI / 任何 OpenAI-compatible API）
 * 2. 否则用 ANTHROPIC_API_KEY
 * 3. 都没有 → fallback 到 lib/dialogue.ts 的 mock
 *
 * 模型默认 gpt-4o-mini（便宜、够用），可由环境变量覆盖
 *  - OPENAI_MODEL, ANTHROPIC_MODEL
 */

import OpenAI from "openai";
import { getPersona } from "./personas";
import {
  generateResponse as mockGenerate,
  type DialogueTurn,
} from "./dialogue";

type Lang = "zh" | "en";

export interface LLMResult {
  content: string;
  provider: "openai" | "anthropic" | "mock";
  model: string;
}

function getProvider(): "openai" | "anthropic" | "mock" {
  if (process.env.OPENAI_API_KEY) return "openai";
  if (process.env.ANTHROPIC_API_KEY) return "anthropic";
  return "mock";
}

async function callOpenAI(
  messages: Array<{ role: "system" | "user" | "assistant"; content: string }>,
  lang: Lang
): Promise<LLMResult> {
  const apiKey = process.env.OPENAI_API_KEY!;
  const baseURL = process.env.OPENAI_BASE_URL; // 可指向任何 OpenAI-compatible API
  const model = process.env.OPENAI_MODEL || "gpt-4o-mini";

  const client = new OpenAI({ apiKey, baseURL });

  const res = await client.chat.completions.create({
    model,
    messages,
    temperature: 0.8,
    max_tokens: 400,
  });

  const content = res.choices[0]?.message?.content?.trim() || "";
  return { content, provider: "openai", model };
}

async function callAnthropic(
  messages: Array<{ role: "user" | "assistant"; content: string }>,
  system: string,
  lang: Lang
): Promise<LLMResult> {
  const apiKey = process.env.ANTHROPIC_API_KEY!;
  const model = process.env.ANTHROPIC_MODEL || "claude-3-5-haiku-20241022";

  // 用 fetch 直接调，避免再加 SDK
  const res = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": apiKey,
      "anthropic-version": "2023-06-01",
    },
    body: JSON.stringify({
      model,
      max_tokens: 400,
      system,
      messages,
    }),
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Anthropic API error ${res.status}: ${text.slice(0, 200)}`);
  }

  const data = (await res.json()) as {
    content: Array<{ type: string; text: string }>;
  };
  const content = data.content?.[0]?.text?.trim() || "";
  return { content, provider: "anthropic", model };
}

/**
 * 调 LLM（带 mock fallback）
 */
export async function chat(
  userInput: string,
  history: DialogueTurn[] = [],
  lang: Lang = "zh"
): Promise<LLMResult> {
  const provider = getProvider();
  const persona = getPersona(lang);

  if (provider === "mock") {
    const m = mockGenerate(userInput, history);
    return { content: m.content, provider: "mock", model: "mock-keyword-router" };
  }

  // 把 history 转换为 OpenAI/Anthropic 的 messages 格式
  const messages: Array<{ role: "user" | "assistant"; content: string }> = [];
  for (const turn of history) {
    if (turn.role === "user") {
      messages.push({ role: "user", content: turn.content });
    } else if (turn.role === "ei") {
      messages.push({ role: "assistant", content: turn.content });
    }
  }
  messages.push({ role: "user", content: userInput });

  if (provider === "openai") {
    return callOpenAI(
      [{ role: "system", content: persona }, ...messages],
      lang
    );
  } else {
    return callAnthropic(messages, persona, lang);
  }
}

/**
 * 客户端可见的状态（用于 /dialogue 页面显示当前用的是 mock 还是真 LLM）
 */
export function getStatus(): {
  provider: "openai" | "anthropic" | "mock";
  model: string;
  available: boolean;
} {
  const provider = getProvider();
  if (provider === "openai") {
    return { provider, model: process.env.OPENAI_MODEL || "gpt-4o-mini", available: true };
  }
  if (provider === "anthropic") {
    return { provider, model: process.env.ANTHROPIC_MODEL || "claude-3-5-haiku-20241022", available: true };
  }
  return { provider: "mock", model: "keyword-router", available: false };
}
