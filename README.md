# py-reader

**打开即讲解的代码阅读 Skill** —— 面向零基础初学者，丢入一个 `.py` / `.html` 文件，自动生成三栏对照讲解网页并在浏览器中打开。

> A "read-code-instantly" skill for AI coding agents (Kimi Code / Claude Code): drop in a Python or HTML file, get an auto-generated three-pane explanation page (source / line-block explanations / overall logic & output), opened in your browser automatically.

## 它解决什么问题

现有 AI 编程工具（Cursor、Copilot 等）是"选中 → 提问 → 解释"的模式，但代码初学者**连该问什么都不知道**。py-reader 把模式翻转过来：**AI 主动讲，用户看了产生疑惑再追问**——像带逐句翻译的读本，而不是需要自己会查的字典。

## 效果

- 左栏：源代码（按逻辑块分段、语法着色）
- 中栏：逐段大白话解释（术语必解释、配生活类比）
- 右栏：整体运行逻辑、数据流向、预期运行结果、常见报错
- 左右栏**点击互相定位**
- 生成后自动在浏览器打开；看不懂的地方复制回 Agent 对话继续追问

示例见 `examples/三栏视图原型_讲解.html`（直接双击即可体验）。

## 安装

把 `py-reader/SKILL.md` 复制到 Agent 的 skills 目录（注意放在 `py-reader` 子文件夹中）：

| 宿主 | 路径 |
|------|------|
| Kimi Code | `~/.agents/skills/py-reader/SKILL.md` |
| Claude Code | `~/.claude/skills/py-reader/SKILL.md` |

重启宿主后生效。

## 使用

```
用 py-reader 讲解 <任意 .py 或 .html 文件路径>
```

Skill 会在源文件旁生成 `原文件名_讲解.html` 并自动打开（Windows 用 `start`，macOS 用 `open`）。

## 仓库结构

```
├── py-reader/SKILL.md    ← 技能本体
├── examples/             ← 示例代码与讲解效果样本
│   ├── 示例代码_词频统计.py      （教学用示例：词频统计）
│   ├── article.txt              （示例的输入文件）
│   ├── 三栏视图原型.html         （三栏讲解页的界面原型）
│   ├── 三栏视图原型_讲解.html     （skill 对原型页的实际讲解产出）
│   └── 演示输出_词频统计讲解.md   （v1.0 文字版讲解，留作对比）
└── docs/设计思路与实现路径.md   ← 设计文档与产品路线图
```

## 路线图

1. **Skill（当前）**：验证讲解内容质量与三栏交互
2. **Agent 平台原型**（Coze / Dify）：发给真实小白用户验证需求
3. **独立 Web 应用**：浏览器打开即用的三栏代码阅读器，零基础用户的"打开即读"工具

详细思考见 `docs/设计思路与实现路径.md`。
