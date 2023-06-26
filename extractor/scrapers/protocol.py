from pathlib import Path
from typing import Any, Dict, List, Protocol

class Website(Protocol):
    def list(self, report: dict, year: str) -> List[str]:
        ...

    def get(self, report_url: str) -> Any:
        ...
