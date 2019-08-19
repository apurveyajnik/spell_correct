from logging import Formatter
from logging import handlers
import logging
import sys


def my_handler(exc_type, exc_value, exc_traceback):
   logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = "%(levelname)s | %(asctime)s | %(module)s | %(filename)s | " \
                 "%(funcName)s | %(process)d | %(thread)d | %(message)s"
LOGGING_MAX_FILE_SIZE = 500000000
LOGGING_FILE_COUNT = 20

LOGGING_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

logging_file_handler = handlers.RotatingFileHandler(filename="log")

logging_file_handler.setLevel(LOGGING_LEVEL)
logging_file_handler.setFormatter(Formatter(LOGGING_FORMAT))
logging.basicConfig( format=LOGGING_FORMAT,
                    level=LOGGING_LEVEL,
                    datefmt=LOGGING_DATETIME_FORMAT,
                     handlers=[logging_file_handler])
sys.excepthook = my_handler

