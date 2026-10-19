# レビュー先の選択

確認日: 2026-10-19。インストール状態と実行可能な機能は、その環境で確認する。

- **Claude Code**: 変更差分・ローカルファイルには、利用可能なら Anthropic `pr-review-toolkit` の該当する観点を優先する。全エージェントを毎回起動する必要はない。
- **Claude Code の PR レビュー**: Anthropic `code-review` は GitHub PR と外部コメント投稿を含む手順。投稿の依頼がないローカルレビューを、そのまま委譲しない。
- **Codex**: 利用可能な公式レビュー機能が対象（PR、差分等）に合えば使う。存在しない公式 `review` スキルを前提にしない。
- **設計文書・計画**: コード用の公式手順へ無理に委譲せず、[設計・計画の観点](design-review.md) と本文で評価する。対象に適した公式手順が利用可能な場合は、同じ対象・権限の条件で利用できる。
- **未導入・対象外**: `SKILL.md` 本文の読み取り専用レビューを行う。

利用可能なレビュー先にも、対象・比較元・読み取り専用か修正可か・投稿の可否を渡す。詳細な専門レビューや追加エージェントは必要性と利用者の依頼範囲に合わせる。公式本文をコピーして別ホストへ移植しない。

独自の共通基準はこの `review` を正本とし、別名の互換入口へレビューを差し戻さない。

- [Anthropic PR Review Toolkit](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/pr-review-toolkit/README.md)
- [Anthropic Code Review](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-review/commands/code-review.md)
- [Codex skills の公式案内](https://developers.openai.com/codex/skills)
