# debug
# info
# warning
# error
# critical

import logging

logging.basicConfig(level=logging.DEBUG)

# logging.info("emails replied")
# logging.critical("system breach!!")

logger = logging.getLogger("cmabeya logger")
# logger.info("admin created logger")
# logger.critical("admin just removed you")
# logger.log(logging.ERROR,"an error occured")


logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("mylog2.log")

handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s - %(asctime)s :%(message)s")
handler.setFormatter(handler)

logger.addHandler(handler)
logger.debug("this is an important info")
# logger.info("this is only basic information") '''check the error on this line...'''