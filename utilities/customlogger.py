import os
import logging


class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[94m',
        'INFO': '\033[92m',
        'WARNING': '\033[93m',
        'ERROR': '\033[91m',
        'CRITICAL': '\033[95m',
        'ENDC': '\033[0m'
    }

    def format(self, record):
        log_level = record.levelname
        msg = super().format(record)
        return f"{self.COLORS.get(log_level, '')}{msg}{self.COLORS['ENDC']}"


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("sign_in_test")

        # Specify the directory for logs
        log_dir = os.path.join(os.path.dirname(__file__), 'Logs')

        # Ensure the directory exists, create if not
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Specify the log file path
        log_file_path = os.path.join(log_dir, "test.log")

        filehandler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :"
                                      "%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        # Create console handler with colored formatter
        console_handler = logging.StreamHandler()
        colored_formatter = ColoredFormatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        console_handler.setFormatter(colored_formatter)
        logger.addHandler(console_handler)

        return logger


