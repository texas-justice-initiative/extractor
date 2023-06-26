from pathlib import Path
from typing import Any, List

import requests  # type: ignore
from bs4 import BeautifulSoup

from extractor.utils.logger import LOGGER


class TCJSArchive:
    URLS: dict = {
        "jail_population": "https://www.tcjs.state.tx.us/historical-population-reports/#1580454195676-420daca6-0a306",
        "immigration": "https://www.tcjs.state.tx.us/historical-county-jail-population-reports-abbreviated-population-reports/#1580454185676-420daca6-5a56",
        "pregnancies": "https://www.tcjs.state.tx.us/historical-county-jail-population-reports-pregnant-female-reporting/#1580454182378-369daca6-5a29",
    }

    def _check_report_type(self, report_type: str):
        if report_type not in self.URLS.keys():
            raise NotImplementedError(
                f"{report_type} not valid report type. Valid types are {list(self.URLS.keys())}"
            )

    def list(
        self, path: Path, year: str = "2022", report_type: str = "jail_population"
    ) -> List[str]:
        """Get all URLs for a report in a given year"""

        try:
            self._check_report_type(report_type=report_type)
            pdf_links = []
            self._check_report_type(report_type)

            response = requests.get(self.URLS[report_type])
            html = BeautifulSoup(response.text, "html.parser")
            for link in html.find_all("li"):
                try:
                    if "pdf" in link["class"]:
                        pdf_link: str = link.find("a").get("href")
                        if year in pdf_link:
                            pdf_links.append(pdf_link)
                except KeyError:
                    LOGGER.info(f"{link} not valid url")

            return pdf_links

        except NotImplementedError as error:
            LOGGER.error(error)
            return []

    def fetch(self, path: str) -> Any:
        file_contents: requests.Response = requests.get(path)
        return file_contents
