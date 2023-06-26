from dataclasses import dataclass
from enum import Enum


class DocumentFormat(Enum):
    PDF = 1
    CSV = 2
    SQL = 3
    XSLX = 4

class ReportType(Enum):
    JAIL_POPULATION = 1
    PREGNANT_INMATE = 2
    SERIOUS_INCIDENT = 3
    IMMIGRANT_DETAINER = 4
    OPERATION_LONE_STAR = 5

class DataSource(Enum):
    TEXAS_AG = 1
    TCJS = 2
    US_CENSUS = 3