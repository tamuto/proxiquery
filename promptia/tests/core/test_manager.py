"""PromptiaManagerテストモジュール."""
import unittest

from promptia.core.manager import PromptiaManager
from promptia.core.defines import PromptTemplate
from promptia.storages.memory_storage import MemoryStorage


class TestCase(unittest.TestCase):
    """PromptiaManagerのテストケース."""

    def test_build(self):
        """buildメソッドのテスト."""
        manager = PromptiaManager(MemoryStorage())
        manager.add_template(
            PromptTemplate(
                name='test_template',
                description='Test template',
                system='Hello, {{ name }}!',
                messages=[],
                parameters={'name': 'string'},
                function_calling_config=None
            )
        )
        built_prompt = manager.build('test_template', '1.0', {'name': 'World'})
        self.assertEqual(built_prompt.system, 'Hello, World!')

    def test_build_with_list(self):
        """パラメータにlistを指定したbuildメソッドのテスト."""
        manager = PromptiaManager(MemoryStorage())
        manager.add_template(
            PromptTemplate(
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
        )
        built_prompt = manager.build('test_template', '1.0', {'data': ['a', 'b', 'c']})
        # self.assertEqual(built_prompt.content, 'Hello, World!')
        print(built_prompt.system)
