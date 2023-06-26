import click
from pathlib import Path
import os
import datetime
from typing import List, Union

import dotenv
import sqlalchemy as sa
import pandas as pd

from extractor.tcjs import TCJSConnection
from extractor.convert import PDFConverter
from extractor.database import DatabaseConnection

dotenv.load_dotenv()
postgres_engine = sa.create_engine(
    f'postgresql+psycopg2://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_URI")}:{os.getenv("DB_PORT")}/{os.getenv("DB_EXTERNAL")}'
)


@click.command()
@click.option(
    "--report-type",
    type=click.Choice(
        ["jail_population", "pregnancies", "immigration", "serious_incidents"]
    ),
)
@click.option("--download", is_flag=True)
@click.option("--convert", is_flag=True)
@click.option("--load", is_flag=True)
@click.option("--remote", is_flag=True)
@click.option("--date-start", type=click.DateTime(formats=["%Y%m"]), default="202112")
@click.option("--date-end", type=click.DateTime(formats=["%Y%m"]), default="202201")
def extract(report_type, download, convert, load, remote, date_start, date_end):
    reports: list = [
        "jail_population",
        "pregnancies",
        "immigration",
        "serious_incidents",
    ]
    if report_type is not None:
        reports = [report_type]

    start: datetime.datetime = date_start.date()
    end: datetime.datetime = date_end.date()
    report_dates: list = pd.date_range(
        start, end + datetime.timedelta(days=35), freq="m"
    )

    # if remote, then need to set up s3 bucket/key and an S3 FileSystem
    # if local, then need to set up filesystem to have local stuff ingrained

    if remote:
        filesystem = "s3"
    else:
        filesystem = "local"

    for report in reports:
        click.echo(f"{report} reports between {start} to {end}")

        if download and report != "serious_incidents":
            for report_date in report_dates:
                report_year = report_date.year
                report_month = str(int(report_date.month))
                click.echo(f"Processing {report} | {report_year}{report_month}")

                click.echo("Downloading PDF")
                try:
                    TCJSConnection().download(
                        document_type=report,
                        data_year=report_year,
                        data_month=report_month,
                        data_path=Path("../data"),
                    )
                except FileNotFoundError as err:
                    click.echo(err)

        report_years: list = list(set([date.year for date in report_dates]))

        if convert:
            for report_year in report_years:
                click.echo(f"Converting PDF to CSV for {report_year}")
                data_paths: List[Path] = Path(f"../data/{report}/{report_year}/").glob(
                    "*.pdf"
                )
                converter = PDFConverter(document_type=report)

                for path in data_paths:
                    converter.convert(doc_path=path)

        if load:
            for report_year in report_years:
                click.echo(f"Loading CSV to data warehouse for {report_year}")
                data_path: List[Path] = Path(f"../data/{report}/parsed/{report_year}/")

                DatabaseConnection(engine=postgres_engine).load(
                    data_path=data_path,
                    document_type=report,
                )


def set_output(doc_path: Union[str, Path], is_remote: bool) -> Union[str, Path]:
    """Generate the beginning of the output path for the files. Local path needs to be created, whereas S3 just needs to be a string"""
    doc_path = doc_path
    if is_remote:
        output_path: Union[str, Path] = "s3://tcjs_reports/doc_path.parts[-2]"  # type: ignore
    else:
        output_path = doc_path.parent.parent / "parsed" / doc_path.parts[-2]  # type: ignore
        os.makedirs(output_path)

    return output_path

# output schema for dbt source
