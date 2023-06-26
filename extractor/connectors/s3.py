from pathlib import Path
from typing import Any, List
from s3fs import S3FileSystem


class S3FileStore:
    def __init__(self, bucket: str, key: str, secret: str):
        self._bucket = bucket
        self._s3 = S3FileSystem(key=key, secret=secret)

    def list(self, path: Path) -> List[str]:
        return self._s3.glob(path)

    def fetch(self, path: Path) -> Any:
        with self._s3.open(path, "rb") as target:
            return target.read()

    def save(self, path: Path, data: Any) -> None:
        with self._s3.open(path, "wb") as target:
            target.write(data)
