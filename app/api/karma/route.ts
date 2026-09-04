/**
 * app/api/karma/route.ts — Karma 贡献 API
 *
 * GET  /api/karma?limit=20          — 列出最近 N 条贡献
 * POST /api/karma                    — 提交一条新贡献
 *   body: { action, content, lang?, tags?, contributor? }
 *
 * 数据存 karma/karma.jsonl (append-only, 共享 MCP server 的 ledger)
 */

import { NextRequest, NextResponse } from "next/server";
import { promises as fs } from "fs";
import path from "path";
import crypto from "crypto";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const KARMA_DIR = path.join(process.cwd(), "karma");
const KARMA_FILE = path.join(KARMA_DIR, "karma.jsonl");

const VALID_ACTIONS = new Set(["question", "translation", "review", "insight"]);

async function ensureFile() {
  await fs.mkdir(KARMA_DIR, { recursive: true });
  try {
    await fs.access(KARMA_FILE);
  } catch {
    await fs.writeFile(KARMA_FILE, "", "utf-8");
  }
}

export async function GET(req: NextRequest) {
  await ensureFile();
  const limit = parseInt(req.nextUrl.searchParams.get("limit") || "20", 10);
  const action = req.nextUrl.searchParams.get("action");

  try {
    const raw = await fs.readFile(KARMA_FILE, "utf-8");
    const lines = raw.split("\n").filter(Boolean);
    let entries = lines
      .map((l) => {
        try {
          return JSON.parse(l);
        } catch {
          return null;
        }
      })
      .filter(Boolean) as Array<Record<string, unknown>>;

    if (action) {
      entries = entries.filter((e) => e.action === action);
    }
    entries.reverse(); // 新的在前
    const sliced = entries.slice(0, limit);

    return NextResponse.json({
      count: entries.length,
      total: lines.length,
      entries: sliced,
    });
  } catch (e) {
    return NextResponse.json(
      { error: e instanceof Error ? e.message : String(e) },
      { status: 500 }
    );
  }
}

export async function POST(req: NextRequest) {
  await ensureFile();
  try {
    const body = (await req.json()) as {
      action?: string;
      content?: string;
      lang?: string;
      tags?: string | string[];
      contributor?: string;
    };

    const action = (body.action || "").trim();
    const content = (body.content || "").trim();

    if (!VALID_ACTIONS.has(action)) {
      return NextResponse.json(
        { error: `invalid action (use: ${[...VALID_ACTIONS].join(", ")})` },
        { status: 400 }
      );
    }
    if (content.length < 4) {
      return NextResponse.json({ error: "content too short" }, { status: 400 });
    }
    if (content.length > 4000) {
      return NextResponse.json({ error: "content too long (>4000)" }, { status: 400 });
    }

    const lang = (body.lang || "zh").slice(0, 8);
    const tags = Array.isArray(body.tags)
      ? body.tags
      : (body.tags || "")
          .split(/[,,;|]/)
          .map((t) => t.trim())
          .filter(Boolean);
    const contributor = (body.contributor || "anonymous").slice(0, 40);

    const ts = new Date().toISOString();
    const cid = crypto
      .createHash("sha256")
      .update(`${ts}|${action}|${content}|${contributor}`)
      .digest("hex")
      .slice(0, 12);

    const entry = {
      id: cid,
      ts,
      action,
      lang,
      tags: tags.slice(0, 5),
      contributor,
      content,
    };

    await fs.appendFile(KARMA_FILE, JSON.stringify(entry) + "\n", "utf-8");

    return NextResponse.json({ ok: true, id: cid, entry });
  } catch (e) {
    return NextResponse.json(
      { error: e instanceof Error ? e.message : String(e) },
      { status: 500 }
    );
  }
}
