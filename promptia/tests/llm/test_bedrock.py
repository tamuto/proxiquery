"""AWS Bedorckのテストモジュール."""
import unittest

from promptia.core.defines import BuiltPrompt
from promptia.core.defines import Message
from promptia.core.defines import FunctionCallingConfig
from promptia.core.defines import Function
from promptia.core.defines import ObjectProperty
from promptia.core.defines import StringProperty
from promptia.llm.bedrock import BedrockClaude3Haiku


@unittest.skip('Bedrockのテストはスキップ')
class TestCase(unittest.TestCase):
    """Bedrockのテストケース."""

    def test_claude3haiku(self):
        """BedrockClaude3Haikuのテスト."""
        prompt = BuiltPrompt(
            system='ユーザからの入力を受け取り、それに対して返答を生成する。',
            messages=[
                Message(role='user', content='こんにちは'),
            ],
            function_calling_config=None
        )

        adapter = BedrockClaude3Haiku()
        result = adapter.call_llm(prompt)
        print(result)

    def test_claude3haiku_with_function(self):
        """BedrockClaude3Haikuのテスト."""
        prompt = BuiltPrompt(
            system=None,
            messages=[
                Message(role='user', content='2024/9/17の東京の天気を教えて'),
            ],
            function_calling_config=FunctionCallingConfig(
                functions=[
                    Function(
                        name='weather_function',
                        description='天気を取得する関数',
                        properties=[
                            ObjectProperty(
                                name='weather_object',
                                properties=[
                                    StringProperty(name='city', description='都市'),
                                    StringProperty(name='date', description='日付'),
                                ]
                            )
                        ]
                    )
                ],
                function_call='weather_function'
            )
        )

        adapter = BedrockClaude3Haiku()
        result = adapter.call_llm(prompt)
        print(result)
