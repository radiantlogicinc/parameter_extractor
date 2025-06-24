from abc import ABC, abstractmethod
from typing import Tuple, Type, Any

from pydantic import BaseModel

class ParameterExtractorInterface(ABC):
    @abstractmethod
    def train(
        self, 
        labeled_dataset: list[dict[str, Any]], 
        output_artifacts_folderpath: str
    ) -> bool:
        """
        Train the command router on a labeled dataset.

        Args:
            labeled_dataset: A list of (command, label) tuples.
            output_artifacts_folderpath: Path to save training artifacts.

        Returns:
            True if training was successful, False otherwise.
        """
        pass

    @abstractmethod
    def extract(
        self,
        output_artifacts_folderpath: str,
        command: str,
        signature_expected_parameters: Type[BaseModel],
        **kwargs
    ) -> BaseModel:
        """
        Extract parameters from a given command.

        Args:
            output_artifacts_folderpath: Path to save training artifacts.
            command: The command string to extract parameters from.
            signature_expected_parameters: The Pydantic model class defining the expected parameters.
            **kwargs: Additional keyword arguments for parameter extraction.

        Returns:
            A Pydantic model instance containing the extracted parameters.
        """