from logger_folder.logger_class import LoggerClass
import os

BASEDIR = os.path.dirname(os.path.realpath(__file__))

spam = LoggerClass(logger_name="spam_logging", log_directory=BASEDIR)
spam_logger = spam.create_logger()

spam_logger.warning("this is my spam warning")
spam_logger.info("this is my spam info")
spam_logger.debug("this is my spam debug")



eggs = LoggerClass(logger_name="eggs_logging", log_directory=BASEDIR)
eggs_logger = eggs.create_logger()

eggs_logger.warning("this is my egg warning")
eggs_logger.info("this is my egg info")
eggs_logger.debug("this is my egg debug")