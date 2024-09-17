"""LLMAdapterモジュール."""
from abc import abstractmethod

from ..core.defines import BuiltPrompt


class LLMAdapter:
    """LLMとの通信を行うための抽象クラス."""

    @abstractmethod
    def call_llm(self, prompt: BuiltPrompt) -> str:
        """LLMを呼び出す."""
        pass
