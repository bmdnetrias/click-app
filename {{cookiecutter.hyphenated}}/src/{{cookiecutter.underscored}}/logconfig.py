import sys
from functools import partialmethod

from loguru import logger

logger.disable("{{ cookiecutter.underscored }}")


DEFAULT_LOG_FORMAT  = (
        "{level}|{elapsed}|{time:YYYY/MM/DD HH:mm:ssZ!UTC}|{name}|{function}|{message}"
    )

def logging_config(log_format, log_level, log_file):

    logger.remove()

    logger.level("MSG", no=22)
    logger.__class__.msg = partialmethod(logger.__class__.log, "MSG")

    log_config = {}
    log_config["handlers"] = [
        {"sink": sys.stdout, "format": "{level} - {message}", "level": "MSG"},
        {"sink": sys.stderr, "format": log_format, "level": log_level},
    ]

    if log_file:
        log_config["handlers"].append(
            {"sink": log_file, "format": log_format, "level": log_level},
            )

    logger.configure(**log_config)
    return logger
