# ai-dev-kit

AI駆動開発の運用を補完するスキル集。GitHub Issue からの着手、検証、PR 提出、スキル改善・配布を扱う。**一般的な実装・レビュー・スキル作成は、実行環境で利用できる公式手順を優先し、このキットにはチームの運用条件を残す。**

`SKILL.md` は Agent Skills 形式。Claude Code / Codex での呼び出しを案内し、他の対応エージェントでも各スキルの小さい代替手順を使える。形式互換と、全ホスト・全モデルでの実行検証済みであることは別。利用できるツール・認証・シェルを実行時に確認する。

## 日常利用

| スキル | 役割・終了条件 |
|---|---|
| `start` | 指定 Issue または Issue なしの作業から、作業ブランチを準備 |
| `new-feature` | `start` の Issue なし経路への互換入口。単体導入でも動く |
| `create-issue` | 粒度・完了条件・内容を確定して Issue を作成 |
| `sync-main` | 指定した基準ブランチの更新を取り込む。名前にかかわらず main 固定ではない |
| `ship` | 対象変更の commit → push → PR 作成/更新で終了。merge・ブランチ削除は含めない |
| `review` | 読み取り専用のレビューと優先度付き指摘。修正・投稿は別の依頼範囲 |
| `test-check` | 変更に必要な検証と証跡。静的レビュー・公開・本番確認とは区別 |
| `long-run` | 完了条件、進捗、チェックポイントを保ち、許可範囲で長時間作業を継続 |
| `output-style` | 応答・ドキュメント・コードの記述や推敲に、対象別のルールを適用 |

## 保守者向け

| スキル | 役割・終了条件 |
|---|---|
| `update-skill` | 公式 skill-creator を優先して、このリポジトリの正本 `skills/` を改善。配布操作は含めない |
| `release-kit` | 正本を検証して配布を準備。具体的な対象・内容の承認後に公開 |

`new-feature` を急に削除せず、既存の呼び出しを維持する。一般利用者は必要なスキルだけを導入できる。

## インストールと呼び出し

### GitHub CLI の `gh skill`

`gh skill` を備えた GitHub CLI（v2.90+）を使う。手元の `gh skill install --help` で使用可能な agent・scope を確認する。

```text
gh skill install MunehiroSoma/ai-dev-kit start --agent claude-code --scope user
gh skill install MunehiroSoma/ai-dev-kit ship --agent claude-code --scope user
gh skill update
```

### Claude Code プラグイン

```text
/plugin marketplace add MunehiroSoma/ai-dev-kit
/plugin install ai-dev-kit@ai-dev-training
/reload-plugins
```

プラグインでは `/ai-dev-kit:start`、個別導入では `/start`。Codex では利用可能なスキルとして `$start` などで呼び出す。実行中のホストの呼び出し方法を使い、別ホストのスラッシュコマンドをシェルで実行しない。

### 手動コピー

`skills/スキル名/` を、対象ホストが読み込むスキルディレクトリ（例: `.claude/skills/`、`.agents/skills/`）へ**フォルダごと**コピーする。`SKILL.md` だけをコピーしない。

各スキルは単体導入できる。必須の参照は同じスキルのフォルダ内に置き、兄弟スキルやリポジトリ直下の文書を実行時の必須依存にしない。別スキル・公式手順は利用可能な場合だけ使い、なければ本文の代替で進める。勝手に公式プラグインをインストールしない。

## 記述ルール

[output-style](skills/output-style/SKILL.md) に共通原則と、応答・ドキュメント・コードのルールをまとめる。既存の全スキルも、記述・編集前と提出前に出力対象に応じて適用する。チャット内の仕様書にはドキュメント、添える返答には応答のルールを使う。

現行の仕様や手順を直接書き、変更の経緯と理由は原則としてコミットログやPRへ残す。移行・互換性・禁止事項など、読者の行動に必要な説明は文書に残す。

ルールの編集元は `skills/output-style/references/output-*.md`。各スキルの同名ファイルは単体導入用のコピーとして同梱する。更新時はリポジトリ直下で `python scripts/sync-output-rules.py` を実行し、`python scripts/sync-output-rules.py --check` で一致を確認する。

[実出力の評価記録](evals/output-style/README.md)に、依頼と資料、実際の出力、修正した問題、コード例の再実行用テストを収録する。

## 通常モードと研修モード

通常は、作業の結果と必要な未確認事項を報告して終了する。毎回の感想・改善確認・見送り理由の記録は要求しない。

ユーザーが**「研修モード」**と明示した場合だけ、タスク終了時に次の4項目をまとめて1回確認する。複数スキルを使っても、各段階では繰り返さない。

1. 良かった点
2. 使いにくかった点・迷った点
3. エージェントからの改善提案
4. 今すぐスキルを更新するか

更新を希望した場合は、その依頼範囲で正本を改善する。更新しない理由の説明や、Issue への投稿を必須にしない。

## プロジェクトに合わせる情報

導入ファイルのプレースホルダを案件ごとに書き換える方式は使わない。対象リポジトリの規約、設定、会話から、remote・既定ブランチ・検証コマンド・PR テンプレートを実行時に確認する。根拠がなく結果が変わる不明点だけを質問する。

既存の未コミット変更・ステージ内容・worktree を保全し、ユーザーの指定と承認済みの範囲を引き継ぐ。CLI の例は実際のシェルへ合わせる。PowerShell に Bash の行継続や環境変数構文をそのまま渡さない。

## 正本と配布

スキルの正本は **このリポジトリの `skills/`** に一本化する。導入コピー、plugin キャッシュ、利用プロジェクト側の `.claude/`・`.agents/`・`.codex/` を直接修正・相互同期しない。

`update-skill` は正本の改善まで。`release-kit` で検証、ルート `.claude-plugin/plugin.json` の version 更新、変更履歴、公開先・対象コミット・タグを準備する。commit / tag / push は依頼範囲に従い、公開前に具体的な対象・内容の承認を確かめる。公開後の更新は利用者の導入方式で行う。

配布バージョンは `.claude-plugin/plugin.json` で管理する。対応するタグとリリース内容は [Releases](https://github.com/MunehiroSoma/ai-dev-kit/releases) で確認できる。

## 公式との分担

確認日: **2026-10-19**。候補名が同じでも、対象・権限・環境を確認して選ぶ。

| このキット | 公式の優先候補 | 残す補完 |
|---|---|---|
| `ship` | Codex `yeet` / Claude `commit-push-pr` | 対象変更の限定、PR base、既存 PR の保持、PR 提出で終了 |
| `update-skill` | 各ホストの `skill-creator` | 正本の特定、導入コピー編集禁止、配布への引継ぎ |
| `review` | 利用可能な公式レビュー機能 / Claude `pr-review-toolkit` | チーム固有観点、読み取り専用・投稿の境界、証拠に基づく判定 |

公式の詳細は、該当するスキル内の `references/providers.md` に出典と適用条件を置く。公式本文を複製しない。`feature-dev` は設計・実装まで含むため、ブランチ準備だけの `new-feature` の置換とは扱わない。

- [OpenAI: skills とプロンプトの見直し](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
- [OpenAI: skills の公式案内](https://developers.openai.com/codex/skills)
- [Claude Code: Skills](https://code.claude.com/docs/en/skills)

## ライセンス

Proprietary（公開リポジトリ・社内/研修利用）。
