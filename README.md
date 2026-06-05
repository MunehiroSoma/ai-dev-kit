# ai-dev-kit

AI駆動開発の**標準ワークフロースキル集**。GitHub Flow をベースに、作業開始 → 実装 → レビュー →
完了判定 → PR → スキル自己改善・配布までを、エージェント用スキル（`SKILL.md`）として提供する。

[agentskills.io](https://agentskills.io) 仕様準拠。**マルチエージェント対応**（Claude Code / Cursor / Codex / Copilot / Gemini ほか）。

## インストール

### A. `gh skill`（推奨・マルチエージェント）

GitHub CLI v2.90+ が必要。

```bash
# 個別スキルを導入（例）
gh skill install MunehiroSoma/ai-dev-kit start --agent claude-code --scope user
gh skill install MunehiroSoma/ai-dev-kit ship  --agent claude-code --scope user

# プレビュー / 更新
gh skill update
```

### B. Claude Code プラグイン（まとめて導入）

```
/plugin marketplace add MunehiroSoma/ai-dev-kit
/plugin install ai-dev-kit@ai-dev-training
/reload-plugins
```
呼び出しは名前空間付き：`/ai-dev-kit:start` など。

### C. 手動コピー

`skills/<skill>/` を対象リポジトリの `.claude/skills/`（または `.agents/skills/`）にコピー。

## 収録スキル

| スキル | 役割 |
|---|---|
| `start` | 作業開始（Issue確認 → ブランチ作成） |
| `new-feature` | main からブランチを切る |
| `create-issue` | Issue を正しい粒度で登録 |
| `sync-main` | main 同期 & rebase |
| `ship` | commit → push → PR |
| `review` | 実装レビュー（汎用観点） |
| `test-check` | 完了判定チェックリスト |
| `long-run` | 自走で長時間タスクを完遂 |
| `update-skill` | スキルを使うたびに育てる |
| `release-kit` | 改善を公開リポジトリへ反映・配布 |

## プレースホルダ

各スキルは `<owner>/<repo>` `<TEST_CMD>` `<LINT_CMD>` `<FORMAT_CMD>` `<PRECOMMIT_CMD>` `<MERGE_STYLE>`
をプロジェクトに合わせて置き換えて使う。

## 更新の配布

スキルを改善したら `release-kit` スキルを使う（version 更新 → commit → tag → push）。
利用者は `gh skill update` または `/plugin update` で受け取る。

## ライセンス

Proprietary（非公開リポジトリ・社内/研修利用）。
</content>
