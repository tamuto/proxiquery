"""PromptiaManagerテストモジュール."""
import unittest

from promptia.core.manager import Promptia
from promptia.core.defines import PromptTemplate


class TestCase(unittest.TestCase):
    """PromptiaManagerのテストケース."""

    def test_build(self):
        """buildメソッドのテスト."""
        template = PromptTemplate(
            name='test_template',
            description='Test template',
            system='Hello, {{ name }}!',
            messages=[],
            parameters={'name': 'string'},
            function_calling_config=None
        )
        tia = Promptia()
        built_prompt = tia.build(template, {'name': 'World'})
        self.assertEqual(built_prompt.system, 'Hello, World!')

    def test_build_with_list(self):
        """パラメータにlistを指定したbuildメソッドのテスト."""
        template = PromptTemplate(
            name='test_template',
            description='Test template',
            system='''{{ data }}
            {% for d in data %}
            - {{ d }}
            {% endfor %}
            ''',
            messages=[],
            parameters={'name': 'list'},
            function_calling_config=None
        )
        tia = Promptia()
        built_prompt = tia.build(template, {'data': ['a', 'b', 'c']})
        # self.assertEqual(built_prompt.content, 'Hello, World!')
        print(built_prompt.system)
