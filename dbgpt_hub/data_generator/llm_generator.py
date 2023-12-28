from abc import ABC, abstractmethod

from typing import Any, Dict, List, Optional, Tuple, Union

class LLMGenerator(ABC):
    """An interface for large language model data generator.
    A LLM data generator can accept prompts and generate synthetic Text2SQL dataset.
    """

    @abstractmethod
    def generate_synthetic_dataset(self):
        """Function for generating synthetic dataset"""
        pass

    @abstractmethod
    def _chat_llm(self):
        """Function for interacting with LLMs"""
        pass

    @abstractmethod
    def _writeout_dataset(self):
        """Function for writing out generated dataset"""
        pass
