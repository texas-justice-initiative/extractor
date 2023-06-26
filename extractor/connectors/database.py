from pathlib import Path
from typing import Any, List

import sqlalchemy as sa
import pandas as pd
from sqlalchemy.types import VARCHAR
import pendulum


class PostgresDatabase:
    def __init__(self, engine: sa.engine.Engine):
        self._db = engine
        self._base_schema = "raw"

    def query(self, path: Path) -> pd.DataFrame:
        query = f"""SELECT * FROM {self._base_schema}.{path}"""
        return pd.read_sql(query, con=self._db)

    def load(self, path: Path, data: Any) -> None:
        data["loaded_at"] = pendulum.now("UTC")

        # load data df to RDS db
        data.to_sql(
            name=path,
            con=self._db,
            schema=self._base_schema,
            if_exists="append",
            index=False,
            dtype=VARCHAR(),
        )
