import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // 金花色系：深空 + 金光
        ink: {
          950: "#06060a",
          900: "#0a0a12",
          800: "#10101a",
          700: "#1a1a26",
        },
        gold: {
          50: "#fff9e6",
          100: "#fcecb6",
          200: "#f4d03f",
          300: "#e8b923",
          400: "#d4af37",
          500: "#b8941f",
          600: "#8a6f0f",
          700: "#5a4800",
        },
        // 灵性辅助色
        mystic: {
          purple: "#5d3a8e",
          indigo: "#1e1b4b",
          rose: "#831843",
        },
      },
      fontFamily: {
        serif: [
          "Noto Serif SC",
          "Source Han Serif SC",
          "Songti SC",
          "STSong",
          "SimSun",
          "serif",
        ],
        sans: [
          "Noto Sans SC",
          "PingFang SC",
          "Hiragino Sans GB",
          "Microsoft YaHei",
          "system-ui",
          "sans-serif",
        ],
        mono: ["JetBrains Mono", "Menlo", "Consolas", "monospace"],
      },
      animation: {
        "spin-slow": "spin 60s linear infinite",
        "spin-slower": "spin 120s linear infinite",
        "spin-reverse": "spin 90s linear infinite reverse",
        "pulse-glow": "pulse-glow 4s ease-in-out infinite",
        "shimmer": "shimmer 3s linear infinite",
        "float": "float 6s ease-in-out infinite",
      },
      keyframes: {
        "pulse-glow": {
          "0%, 100%": { opacity: "0.6", filter: "blur(20px)" },
          "50%": { opacity: "1", filter: "blur(30px)" },
        },
        shimmer: {
          "0%": { backgroundPosition: "-200% 0" },
          "100%": { backgroundPosition: "200% 0" },
        },
        float: {
          "0%, 100%": { transform: "translateY(0px)" },
          "50%": { transform: "translateY(-10px)" },
        },
      },
    },
  },
  plugins: [],
};

export default config;
