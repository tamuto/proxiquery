# Promptia

Promptiaは、大規模言語モデル（LLM）用のプロンプト管理と生成を効率化するためのPythonライブラリです。

## 特徴

- 様々なLLMやAPI用のプロンプトテンプレート管理
- 抽象的なテンプレートを特定のAPI形式に変換
- 詳細な設定が可能な関数呼び出しのサポート
- テンプレートのバージョン管理
- Retrieval-Augmented Generation (RAG)を使用した動的な情報埋め込み
- 柔軟性と拡張性のあるモジュラー設計

## インストール

```
pip install promptia
```

## クイックスタート

```python
from promptia import PromptiaManager, MemoryStorage, ChatGPT4o

# PromptiaManagerの初期化
manager = PromptiaManager(MemoryStorage())

# テンプレートの追加
manager.add_template(
    name="greeting",
    content="こんにちは、{name}さん！{place}へようこそ。",
    parameters={"name": "string", "place": "string"}
)

# プロンプトの構築と使用
prompt = manager.build("greeting", "1.0", {"name": "アリス", "place": "不思議の国"})
result = ChatGPT4o.call_llm(prompt)

print(result)
```

## 貢献

貢献を歓迎します！詳細は[貢献ガイドライン](CONTRIBUTING.md)をご覧ください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。
