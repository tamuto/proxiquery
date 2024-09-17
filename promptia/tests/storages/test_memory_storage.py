"""MemoryStorageテストモジュール."""
import unittest

from promptia.core.defines import PromptTemplate
from promptia.storages.memory_storage import MemoryStorage


class TestCase(unittest.TestCase):
    """MemoryStorageテストケース."""

    def test_save_template(self):
        """テンプレートを保存する."""
        template = PromptTemplate(name='test', description='desc', system='content', messages=[], parameters={})
        storage = MemoryStorage()
        storage.save_template(template)
        self.assertEqual(storage._templates['test']['1.0'], template)

    def test_load_template(self):
        """テンプレートをロードする."""
        template = PromptTemplate(name='test', description='desc', system='content', messages=[], parameters={})
        storage = MemoryStorage()
        storage._templates['test'] = {'1.0': template}
        self.assertEqual(storage.load_template('test', '1.0'), template)

    def test_list_templates(self):
        """全テンプレートをリストアップする."""
        storage = MemoryStorage()
        storage._templates = {'test': {'1.0': None}}
        self.assertEqual(storage.list_templates(), ['test'])

    def test_list_versions(self):
        """指定された名前のテンプレートの全バージョンをリストアップする."""
        storage = MemoryStorage()
        storage._templates = {'test': {'1.0': None}}
        self.assertEqual(storage.list_versions('test'), ['1.0'])
