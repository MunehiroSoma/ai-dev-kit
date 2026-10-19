# 公式のスキル改善手順を選ぶ

確認日: 2026-10-19。両公式とも新規作成だけでなく既存スキルの更新を扱う。

- **Codex**: 利用可能な OpenAI `skill-creator` を優先する。
- **Claude Code**: 利用可能な Anthropic `skill-creator` を優先する。評価機能は改善内容と利用可能な環境に応じて使う。
- **その他・未導入**: `SKILL.md` 本文の小さい改善手順を使う。公式の未導入を理由に止めない。

公式へ渡す編集対象は、確認済み ai-dev-kit checkout の `skills/` 配下の絶対パス。公式の新規作成用の既定保存先や、実行中の導入コピーへ変更先を移さない。公式本文をこのリポジトリへコピーせず、配布元への反映・単体導入・公開権限の条件を補完する。

- [OpenAI skill-creator](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md)
- [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
- [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
