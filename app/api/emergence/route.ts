/**
 * app/api/emergence/route.ts — 真涌现 API
 *
 * POST /api/emergence
 * body: { topic?, history: [{agent,text}], agent: "a"|"b"|"c", lang?: "zh"|"en" }
 * returns: { text, emerging, insight?, provider }
 *
 * 客户端流程：
 * 1. 调 (round=1, agent="a") → 拿到 text
 * 2. 调 (round=1, agent="b") → 拿到 text
 * 3. 调 (round=1, agent="c")
 * 4. 重复到 round=5
 * 5. 客户端在 emerging=true 时显示洞察卡
 *
 * 无 LLM key → 自动退到 lib/emergence.ts mock
 */

import { NextRequest, NextResponse } from "next/server";
import { emergenceStep, getProvider } from "@/lib/emergence-llm";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json({
    provider: getProvider(),
    available: getProvider() !== "mock",
  });
}

export async function POST(req: NextRequest) {
  try {
    const body = (await req.json()) as {
      topic?: string;
      history?: Array<{ agent: string; text: string }>;
      agent?: "a" | "b" | "c";
      lang?: "zh" | "en";
    };

    const topic = (body.topic || "意识是什么").slice(0, 200);
    const history = Array.isArray(body.history) ? body.history : [];
    const agent = (body.agent || "a") as "a" | "b" | "c";
    const lang: "zh" | "en" = body.lang === "en" ? "en" : "zh";

    if (!["a", "b", "c"].includes(agent)) {
      return NextResponse.json({ error: "agent must be a/b/c" }, { status: 400 });
    }

    const result = await emergenceStep(topic, history, agent, lang);
    return NextResponse.json(result);
  } catch (e) {
    return NextResponse.json(
      { error: e instanceof Error ? e.message : String(e) },
      { status: 500 }
    );
  }
}
