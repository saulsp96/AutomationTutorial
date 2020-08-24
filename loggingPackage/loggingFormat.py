import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.warning("Warning message")
logging.info("Info message")
logging.error("Error message")