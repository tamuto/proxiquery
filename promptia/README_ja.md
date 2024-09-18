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
pip install promptia[openai]
```

## クイックスタート

```python
from promptia import Promptia
from promptia import PromptTemplate
from promptia import Message
from promptia.llm.openai import OpenAIGPT4oMini

template = PromptTemplate(
    name='greeting',
    description='greeting template',
    system="あなたの名前は{{name}}です。あなたは{{place}}に迷い込みました。役を演じてください。",
    messages=[
        Message(role='user', content='あなたは誰ですか？'),
    ],
    parameters={
        'name': 'string',
        'place': 'string'
    },
    function_calling_config=None
)
tia = Promptia()
prompt = tia.build(template, {"name": "Alice", "place": "Wonderland"})

llm = OpenAIGPT4oMini()
result = llm.call_llm(prompt)
print(result)
```

## 貢献

貢献を歓迎します！詳細は[貢献ガイドライン](CONTRIBUTING.md)をご覧ください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。
