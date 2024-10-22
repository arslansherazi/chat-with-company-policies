from enum import Enum


class OpenAiModel(Enum):
    GPT_35_TURBO = "gpt-3.5-turbo"
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


CHAT_BOT_INITIAL_PROMPT = """
"""