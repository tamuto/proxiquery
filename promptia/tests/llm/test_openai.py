import unittest

from promptia.core.defines import BuiltPrompt
from promptia.core.defines import Message
from promptia.core.defines import FunctionCallingConfig
from promptia.core.defines import Function
from promptia.core.defines import StringProperty
from promptia.llm.openai import OpenAIGPT4oMini


@unittest.skip('OpenAIのテストはスキップ')
class TestCase(unittest.TestCase):

    def test_gpt4o_mini(self):
        """OpenAIGPT4oMiniのテスト."""
        prompt = BuiltPrompt(
            system='ユーザからの入力を受け取り、それに対して英語と日本語で返答を生成する。',
            messages=[
                Message(role='user', content='こんにちは'),
            ],
            function_calling_config=None
        )
        adapter = OpenAIGPT4oMini()
        result = adapter.call_llm(prompt)
        print(result)

    def test_gpt4o_mini_with_function(self):
        """OpenAIGPT4oMiniのテスト."""
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
                            StringProperty(name='city', description='都市'),
                            StringProperty(name='date', description='日付'),
                        ]
                    )
                ],
                function_call='weather_function'
            )
        )

        adapter = OpenAIGPT4oMini()
        result = adapter.call_llm(prompt)
        print(result)
