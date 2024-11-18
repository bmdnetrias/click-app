import inspect
import logging
import sys

from functools import partialmethod

from loguru import logger

logger.disable("hops")

DEFAULT_LOG_FORMAT = "<y>{level:<7}</y>|{elapsed}|{time:YYYY/MM/DD HH:mm:ssZ!UTC}|{name}|{function}|{message}"

LOGURU_LEVEL_NAMES = [
    "TRACE",
    "DEBUG",
    "INFO",
    "SUCCESS",
    "WARNING",
    "ERROR",
    "CRITICAL",
]


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists.
        level: str | int
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = inspect.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

# This might be needed if a library dependency imports a
# logging.logger at module top level
# logging.basicConfig(handlers=[InterceptHandler()], level=0,# force=True)

def logging_config(log_format, log_level, log_file,
                   colorize=True,
                   intercept_stdlib_logging=True):

    logger.remove()
    logger_msg_level = logger.level("SUCCESS").no - 1

    logger.level("MSG", no=logger_msg_level)
    logger.__class__.msg = partialmethod(logger.__class__.log, "MSG")

    log_config = {}
    log_config["handlers"] = [ {"sink": sys.stderr,
                                "format": log_format,
                                "level": log_level,
                                "colorize": colorize,}, ]

    if logger.level(log_level).no >= logger_msg_level:
        log_config["handlers"].append(
            {"sink": sys.stderr,
             "format": "<y>{level}</y> - {message}",
             "colorize": colorize,
             "level": "MSG",
             "filter": lambda record: record["level"].name == "MSG"
             }
        )
    
    if log_file:
        log_config["handlers"].append(
            {"sink": log_file, "format": log_format, "level": log_level},
            )

    logger.configure(**log_config)
    if intercept_stdlib_logging:
        logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    return logger

