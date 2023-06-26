from pathlib import Path
from typing import Any, List
import glob

from extractor.utils.logger import (
    file_handler,
    get_logger,
)

LOGGER = get_logger(logger_name=__name__, handlers=[file_handler])

class LocalFileSystem:
    def __init__(self, root_dir: Path):
        self._root_dir: Path = root_dir

    def list(self, file_extension: str = "*") -> List[str]:
        return sorted(
            [
                filepath
                for filepath in glob.glob(
                    f"{self._root_dir}/**/*.{file_extension}", recursive=True
                )
            ]
        )

    def get(self, filepath: str) -> Any:
        pass

    def save(self, filepath: Path, data: Any) -> None:
        pass

    def move(
        self, source_filepath: Path, destination_filepath: Path, copy: bool
    ) -> None:
        pass