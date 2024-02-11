import logging
import sys

LOGGING_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}

def get_logger(name, level="info"):
    # Create a logger with the specified name
    logger = logging.getLogger(name)
    logger.setLevel(LOGGING_LEVELS[level])

    # Create handlers
    stdout_handler = logging.StreamHandler(sys.stdout)

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stdout_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(stdout_handler)

    return logger