"""Pattern for classes that convert different formats to CSVs"""

from typing import Protocol

import pandas as pd


class Converter(Protocol):
    def add_metadata(
        self, data: pd.DataFrame, document_id: str, source_filename: str
    ) -> pd.DataFrame:
        ...

    def convert(self, data: pd.DataFrame) -> None:
        ...
