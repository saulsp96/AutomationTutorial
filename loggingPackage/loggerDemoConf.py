"""
Logger Demo
"""
import logging
import logging.config

class LoggerDemoConfig():
    def testLog(self):
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConfig.__name__)

        logger.warning("Warning message")
        logger.info("Info message")
        logger.error("Error message")



logger = LoggerDemoConfig()
logger.testLog()