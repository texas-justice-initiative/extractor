from pathlib import Path
from typing import Any, Dict, List, Protocol


class FileSystem(Protocol):
    def list(self, file_extension: str) -> List[Path]:
        ...

    def get(self, filepath: str) -> Any:
        ...

    def save(self, filepath: Path, data: Any) -> None:
        ...

    def move(
        self, source_filepath: Path, destination_filepath: Path, copy: bool
    ) -> None:
        ...


class Database(Protocol):
    def query(self, query_string: str) -> Dict[Any, Any]:
        ...

    def load(self, data: dict) -> None:
        ...