"""
We're relying on camelot to parse PDFs right now, but eventually re-implement this to:
1. More tightly configure to our use case (we've got some xerox pages; and some handwritten text)
2. Handle multiple file system types (local, and s3)

source: https://github.com/camelot-dev/camelot/blob/644bbe7c6d57b95aefa2f049a9aacdbc061cc04f/camelot/parsers/stream.py#L18
"""


class PDFConverter:
    """Turn PDF into CSV file"""

    # _input: Connection
    # _output: Connection
