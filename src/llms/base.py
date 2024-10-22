"""
Base module for all LLMs
"""
from langchain_core.messages import HumanMessage


class BaseLLM:
    """
    Base class for all LLMs
    """
    def __init__(self, model_name: str):
        self._model_name = model_name
        self._llm = None
        self._verify_model_name()
        self._initialize_llm()

    def get_response(self, query: str) -> str:
        """
        Get response from the LLM

        :param query: user query
        :return: llm response
        """
        messages = [
            HumanMessage(content=query)
        ]
        result = self._llm.invoke(messages)
        results_data = result.content
        return results_data

    def get_llm(self):
        """
        Get the llm object

        :return: llm object
        """
        return self._llm

    def _verify_model_name(self):
        """
        Verify the model name. If the model name is not valid, set the default model name.
        """
        pass

    def _initialize_llm(self):
        """
        Initialize the OpenAi LLM
        """
        pass
