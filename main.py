import os
import logging
from webserver import webserver

log_level: str = os.getenv('LOG_LVL', "DEBUG")
if log_level == "DEBUG":
    log_level = logging.DEBUG
else:
    log_level = logging.INFO
logging.basicConfig(level=log_level)


if __name__ == "__main__":

    webserver()
