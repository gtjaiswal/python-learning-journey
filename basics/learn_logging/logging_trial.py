import logging
from logging import basicConfig

basicConfig(level=logging.INFO, filename="log.log", filemode="w",
            format="%(asctime)s - %(levelname)s - %(message)s")
# x=2
# logging.info(f"the value of x is {x}")
#
# try:
#     1/0
# except ZeroDivisionError as e:
#     logging.exception("ZeroDivisionError")

logger = logging.getLogger(__name__)
handler = logging.FileHandler('test.log')
formatter = logging.Formatter("%(asctime)s - %(name)s -  %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("tests custom logger")

'''
Levels of logs/logging

'''
# # lowest
# logging.debug("debug")
# logging.info("info")
# # default is warning and above
# logging.warning("warning")
# logging.error("error")
# # highest
# logging.critical("critical")