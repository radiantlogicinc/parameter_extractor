from abc import ABC, abstractmethod
from typing import Tuple

class CommandRouterInterface(ABC):
    @abstractmethod
    def train(self, labeled_dataset: list[Tuple[str, str]], output_artifacts_folderpath: str) -> bool:
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
    def predict(self, output_artifacts_folderpath: str, command: str) -> list[str]:
        """
        Predict the label(s) for a given command.

        Args:
            output_artifacts_folderpath: Path to load training artifacts.
            command: The command string to classify.

        Returns:
            A list of predicted labels.
        """