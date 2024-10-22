from enum import Enum


class OpenAiModel(Enum):
    GPT_35_TURBO = "gpt-3.5-turbo"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


CHATBOT_INITIAL_PROMPT = """Use the following pieces of context to answer the question at the end. If you don't 
know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the 
answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
{context}"""

EMPLOYEE_HANDBOOK_PATH = "./static/pdfs/employee_handbook_2024.pdf"
VECTOR_DB_DIR = "./static/chroma/"
