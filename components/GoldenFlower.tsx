"use client";

import { useEffect, useState } from "react";

/**
 * GoldenFlower — 金花曼陀罗
 * 灵感来自荣格《金花的秘密》中的内丹意象
 * 多层同心结构：外光晕 → 12 道光芒 → 8 瓣莲花 → 中央金花
 */
export function GoldenFlower({
  size = 480,
  pulse = true,
}: {
  size?: number;
  pulse?: boolean;
}) {
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  const cx = size / 2;
  const cy = size / 2;

  return (
    <div
      className="relative inline-block"
      style={{ width: size, height: size }}
    >
      {/* 外层光晕（脉冲） */}
      {pulse && (
        <>
          <div
            className="absolute inset-0 rounded-full animate-pulse-glow"
            style={{
              background:
                "radial-gradient(circle, rgba(212,175,55,0.15) 0%, transparent 60%)",
            }}
          />
          <div
            className="absolute rounded-full"
            style={{
              inset: -size * 0.2,
              background:
                "radial-gradient(circle, rgba(93,58,142,0.08) 0%, transparent 70%)",
            }}
          />
        </>
      )}

      <svg
        viewBox={`0 0 ${size} ${size}`}
        className="relative z-10"
        style={{ width: size, height: size }}
        aria-label="Golden Flower Mandala"
      >
        <defs>
          {/* 中心金花径向渐变 */}
          <radialGradient id="goldCore" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="#fff9e6" stopOpacity="1" />
            <stop offset="30%" stopColor="#f4d03f" stopOpacity="1" />
            <stop offset="70%" stopColor="#d4af37" stopOpacity="0.9" />
            <stop offset="100%" stopColor="#8a6f0f" stopOpacity="0.6" />
          </radialGradient>

          {/* 莲花瓣渐变 */}
          <linearGradient id="petal" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#f4d03f" stopOpacity="0.7" />
            <stop offset="100%" stopColor="#8a6f0f" stopOpacity="0.2" />
          </linearGradient>

          {/* 光线渐变 */}
          <linearGradient id="ray" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#fff9e6" stopOpacity="0" />
            <stop offset="50%" stopColor="#f4d03f" stopOpacity="0.4" />
            <stop offset="100%" stopColor="#d4af37" stopOpacity="0" />
          </linearGradient>

          {/* 12 道光芒（每 30°）*/}
          {Array.from({ length: 12 }).map((_, i) => (
            <g
              key={`ray-def-${i}`}
              transform={`rotate(${i * 30} ${cx} ${cy})`}
            >
              <polygon
                points={`${cx},${cy - size * 0.48} ${cx - 3},${cy} ${cx + 3},${cy}`}
                fill="url(#ray)"
              />
            </g>
          ))}
        </defs>

        {/* 最外圈：8 瓣莲花（反向慢旋）*/}
        <g
          style={{
            transformOrigin: `${cx}px ${cy}px`,
            animation: "spin 120s linear infinite reverse",
          }}
        >
          {Array.from({ length: 8 }).map((_, i) => {
            const angle = (i * 360) / 8;
            return (
              <g
                key={`petal-${i}`}
                transform={`rotate(${angle} ${cx} ${cy})`}
              >
                <ellipse
                  cx={cx}
                  cy={cy - size * 0.34}
                  rx={size * 0.06}
                  ry={size * 0.18}
                  fill="url(#petal)"
                  opacity="0.6"
                />
              </g>
            );
          })}
        </g>

        {/* 12 道光芒（中速旋转）*/}
        <g
          style={{
            transformOrigin: `${cx}px ${cy}px`,
            animation: "spin 90s linear infinite",
          }}
        >
          {Array.from({ length: 12 }).map((_, i) => {
            const angle = i * 30;
            return (
              <g
                key={`ray-${i}`}
                transform={`rotate(${angle} ${cx} ${cy})`}
              >
                <polygon
                  points={`${cx},${cy - size * 0.48} ${cx - 4},${cy - size * 0.25} ${cx + 4},${cy - size * 0.25}`}
                  fill="url(#ray)"
                  opacity="0.7"
                />
              </g>
            );
          })}
        </g>

        {/* 同心圆环 */}
        <circle
          cx={cx}
          cy={cy}
          r={size * 0.42}
          fill="none"
          stroke="#d4af37"
          strokeWidth="0.5"
          opacity="0.3"
        />
        <circle
          cx={cx}
          cy={cy}
          r={size * 0.32}
          fill="none"
          stroke="#d4af37"
          strokeWidth="0.5"
          opacity="0.4"
        />
        <circle
          cx={cx}
          cy={cy}
          r={size * 0.22}
          fill="none"
          stroke="#d4af37"
          strokeWidth="0.5"
          opacity="0.5"
        />

        {/* 8 角星（呼应八阵图）*/}
        <g
          style={{
            transformOrigin: `${cx}px ${cy}px`,
            animation: "spin 60s linear infinite",
          }}
        >
          {Array.from({ length: 4 }).map((_, i) => {
            const angle = i * 45;
            return (
              <g
                key={`star-${i}`}
                transform={`rotate(${angle} ${cx} ${cy})`}
              >
                <path
                  d={`M ${cx} ${cy - size * 0.18} L ${cx + size * 0.04} ${cy - size * 0.08} L ${cx + size * 0.04} ${cy + size * 0.08} L ${cx} ${cy + size * 0.18} L ${cx - size * 0.04} ${cy + size * 0.08} L ${cx - size * 0.04} ${cy - size * 0.08} Z`}
                  fill="none"
                  stroke="#d4af37"
                  strokeWidth="1"
                  opacity="0.6"
                />
              </g>
            );
          })}
        </g>

        {/* 中央金花（不旋转，呼吸光晕）*/}
        <g>
          <circle
            cx={cx}
            cy={cy}
            r={size * 0.12}
            fill="url(#goldCore)"
            opacity="0.9"
          />
          <circle
            cx={cx}
            cy={cy}
            r={size * 0.08}
            fill="none"
            stroke="#fff9e6"
            strokeWidth="0.8"
            opacity="0.8"
          />
          {/* 中央 6 瓣小花 */}
          {Array.from({ length: 6 }).map((_, i) => {
            const angle = (i * 360) / 6;
            return (
              <g
                key={`center-petal-${i}`}
                transform={`rotate(${angle} ${cx} ${cy})`}
              >
                <ellipse
                  cx={cx}
                  cy={cy - size * 0.05}
                  rx={size * 0.018}
                  ry={size * 0.04}
                  fill="#fff9e6"
                  opacity="0.9"
                />
              </g>
            );
          })}
          {/* 中央白点 */}
          <circle cx={cx} cy={cy} r={size * 0.012} fill="#fff9e6" />
        </g>
      </svg>
    </div>
  );
}

/**
 * GoldenFlowerMini — 紧凑版，用于导航和小卡片
 */
export function GoldenFlowerMini({ size = 32 }: { size?: number }) {
  const cx = size / 2;
  return (
    <svg
      viewBox={`0 0 ${size} ${size}`}
      width={size}
      height={size}
      className="inline-block"
      aria-hidden
    >
      <defs>
        <radialGradient id={`mini-gold-${size}`}>
          <stop offset="0%" stopColor="#fff9e6" />
          <stop offset="60%" stopColor="#f4d03f" />
          <stop offset="100%" stopColor="#8a6f0f" stopOpacity="0" />
        </radialGradient>
      </defs>
      <circle cx={cx} cy={cx} r={cx} fill={`url(#mini-gold-${size})`} />
      {Array.from({ length: 8 }).map((_, i) => {
        const a = (i * 360) / 8;
        return (
          <g key={i} transform={`rotate(${a} ${cx} ${cx})`}>
            <line
              x1={cx}
              y1={cx - cx * 0.5}
              x2={cx}
              y2={cx - cx * 0.95}
              stroke="#f4d03f"
              strokeWidth="0.5"
              opacity="0.7"
            />
          </g>
        );
      })}
      <circle cx={cx} cy={cx} r={cx * 0.25} fill="#fff9e6" opacity="0.9" />
    </svg>
  );
}
