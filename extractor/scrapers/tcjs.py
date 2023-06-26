import os
from pathlib import Path

import requests  # type: ignore

# from connection.protocol import Connection

BASE_URL: str = "https://www.tcjs.state.tx.us/wp-content/uploads"
FILENAMES = {
    "jail_population": "AbbreRptCurrent.pdf",
    "pregnancies": "PregnantFemaleReportingCurrent.pdf",
    "immigration": "ImmigrationDetainerReportCurrent.pdf",
}

# dates are two-digit month and 4-digit years
# URL format: {BASE}/{YEAR}/{MONTH}/{FILENAME}


class TCJSConnection:
    # _input: Connection
    # _output: Connection

    # def list_files(file_slug: str, start: datetime, end: datetime) -> None:
    #     pass

    @staticmethod
    def _initialize(output_path: Path):
        os.makedirs(output_path, exist_ok=True)

    def download(
        self, document_type: str, data_year: str, data_month: str, data_path: Path
    ) -> None:
        # TODO:
        # function to create paths if DNE
        # convert data date to month/year format

        output_path: Path = Path.cwd().parent / f"data/{document_type}/{data_year}"
        self._initialize(output_path)
        file_contents: requests.Response = requests.get(
            f"{BASE_URL}/{data_year}/{data_month.zfill(2)}/{FILENAMES[document_type]}"
        )

        if file_contents.status_code == 200:
            with open(
                output_path / f"{data_month}{data_year}_{FILENAMES[document_type]}",
                "wb",
            ) as write_file:
                # add log message
                write_file.write(file_contents.content)
        else:
            raise FileNotFoundError(
                f"{FILENAMES[document_type]} not available for date: {data_month}/{data_year} at {BASE_URL}/{data_year}/{data_month.zfill(2)}/{FILENAMES[document_type]}"
            )
