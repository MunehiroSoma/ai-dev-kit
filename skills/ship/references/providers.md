# 公式の提出手順を選ぶ

確認日: 2026-10-19。公式本文は複製せず、実行時に利用可能なスキルの説明と範囲を読む。

| 実行環境 | 優先候補 | このキットで補完する条件 |
|---|---|---|
| Codex | OpenAI `yeet` | 対象差分のみ、明示した base / head、既存 PR の保持、PR 提出で終了 |
| Claude Code | Anthropic `commit-commands` の `commit-push-pr` | 同上。公式が既存 PR を扱わない場合は重複作成せず既存 PR を更新する |
| その他・未導入 | このスキル本文の代替手順 | 認証済みで利用可能な CLI / 接続ツールを使う |

公式はホスト固有のツールや前提を持つ。別ホスト用の本文をコピーして実行しない。公式に全件 staging や固定ブランチを使う手順があっても、今回の対象外変更や base を変更する許可にはならない。条件を満たせない部分だけ本文の代替を使う。公式がないこと自体を作業停止理由にしない。

- [OpenAI yeet](https://github.com/openai/skills/blob/main/skills/.curated/yeet/SKILL.md)
- [Anthropic commit-push-pr](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/commit-commands/commands/commit-push-pr.md)
