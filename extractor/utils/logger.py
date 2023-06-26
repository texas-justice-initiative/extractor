import logging
from typing import List
from pathlib import Path

import pendulum

# make logging directory
log_directory: Path = Path.cwd() / "logs"
Path(log_directory).mkdir(parents=True, exist_ok=True)

## formatters
default_format: logging.Formatter = logging.Formatter(
    "%(name)s %(asctime)s %(levelname)s %(message)s"
)

## handlers
### output to files
file_handler: logging.FileHandler = logging.FileHandler(
    log_directory / f"{pendulum.now().to_iso8601_string()}.log", mode="w"
)

### output to console
stream_handler: logging.StreamHandler = logging.StreamHandler()

## set up logger
def get_logger(
    logger_name: str,
    handlers: List[logging.Handler] = [file_handler],
    formatter: logging.Formatter = default_format,
    level: int = logging.INFO,
) -> logging.Logger:

    # get a custom logger & set the logging level
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # add handler to the logger
    for handler in handlers:
        # add formatter to the handler
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
