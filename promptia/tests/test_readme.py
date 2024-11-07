"""README記載のコードをテストするモジュール."""
import unittest

from promptia import Promptia
from promptia import PromptTemplate
from promptia.llm.openai import OpenAIGPT4oMini


@unittest.skip('テストはスキップ')
class TestCase(unittest.TestCase):
    """README記載のコードをテストするテストケース."""

    def test_readme_ja(self):
        """README記載のコードをテストする."""
        template = PromptTemplate(
            name='greeting',
            description='greeting template',
            system="あなたの名前は{{name}}です。あなたは{{place}}に迷い込みました。役を演じてください。",
            messages=[
                {'role': 'user', 'content': 'あなたは誰ですか？'},
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

    def test_readme_en(self):
        """README記載のコードをテストする."""
        template = PromptTemplate(
            name='greeting',
            description='greeting template',
            system="Your name is {{name}}. You have wandered into {{place}}. Please act.",
            messages=[
                {'role': 'user', 'content': 'Who are you?'},
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
