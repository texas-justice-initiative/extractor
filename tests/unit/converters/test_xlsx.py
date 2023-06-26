from typing import Dict
from extractor.converters.tabular.xlsx import XLSXConverter

from extractor.utils.logger import get_logger, stream_handler

LOGGER = get_logger(logger_name="test_logger", handlers=[stream_handler])

def test_convert_xlsx_immigrant_detainer():
    """
    Convert Excel file into properly-formatted dictionary
    """
    expected: Dict = {}

    converter = XLSXConverter(report_type='pregnant_inmate')
    actual: Dict = converter.convert()

    assert expected == actual
