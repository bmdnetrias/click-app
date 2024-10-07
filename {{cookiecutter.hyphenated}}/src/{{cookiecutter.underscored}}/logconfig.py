import sys
from functools import partialmethod

from loguru import logger

logger.disable("{{ cookiecutter.underscored }}")


DEFAULT_LOG_FORMAT = (
    "{level:<7}|{elapsed}|{time:YYYY/MM/DD HH:mm:ssZ!UTC}|{name}|{function}|{message}"
)

def logging_config(log_format, log_level, log_file):

    logger.remove()
    logger_msg_level = logger.level("SUCCESS").no - 1

    logger.level("MSG", no=logger_msg_level)
    logger.__class__.msg = partialmethod(logger.__class__.log, "MSG")

    log_config = {}
    log_config["handlers"] = [
        {"sink": sys.stderr,
         "format": log_format, "level": log_level,
         "colorize": True,},
    ]

    if logger.level(log_level).no >= logger_msg_level:
        log_config["handlers"].append(
            {"sink": sys.stdout, "format": "<y>{level}</y> - {message}",
             "colorize": True,
             "level": "MSG",
             "filter": lambda record: record["level"].name == "MSG"
             }
        )
    
    if log_file:
        log_config["handlers"].append(
            {"sink": log_file, "format": log_format, "level": log_level},
            )

    logger.configure(**log_config)
    return logger
