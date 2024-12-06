import logging
import os

class LoggerClass:
    def __init__(self, logger_name=None, log_directory = None):
        self.logger_name = logger_name
        self.log_directory = log_directory
        self._create_logging_directory()
    
    def _create_logging_directory(self):
        directory = f'{self.log_directory}/logs'
        if not os.path.exists(directory):
            os.makedirs(directory)


    def create_logger(self) -> logging.Logger:

        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.DEBUG)
    
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        file_handler = logging.FileHandler(f"logs/{self.logger_name}.log")
        file_handler.setLevel(logging.DEBUG)

        console_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

        console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(file_formatter)
    
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger



