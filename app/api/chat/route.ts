/**
 * app/api/chat/route.ts — 修行对话 API
 *
 * POST /api/chat
 * body: { input: string, history?: DialogueTurn[], lang?: "zh" | "en" }
 * returns: { content: string, provider, model, hint? }
 *
 * 由 /dialogue 页面调用。
 */

import { NextRequest, NextResponse } from "next/server";
import { chat, getStatus } from "@/lib/llm";
import { findHint } from "@/lib/dialogue";
import type { DialogueTurn } from "@/lib/dialogue";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json(getStatus());
}

export async function POST(req: NextRequest) {
  try {
    const body = (await req.json()) as {
      input?: string;
      history?: DialogueTurn[];
      lang?: "zh" | "en";
    };

    const input = (body.input || "").trim();
    const history = Array.isArray(body.history) ? body.history : [];
    const lang: "zh" | "en" = body.lang === "en" ? "en" : "zh";

    if (!input) {
      return NextResponse.json({ error: "input required" }, { status: 400 });
    }
    if (input.length > 4000) {
      return NextResponse.json({ error: "input too long" }, { status: 400 });
    }

    const result = await chat(input, history, lang);
    const hint = findHint(input);

    return NextResponse.json({
      content: result.content,
      provider: result.provider,
      model: result.model,
      hint,
    });
  } catch (e) {
    const msg = e instanceof Error ? e.message : String(e);
    return NextResponse.json({ error: msg }, { status: 500 });
  }
}
