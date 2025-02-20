import logging
from colorama import init, Fore

init()

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        msg = super().format(record)
        if record.levelno == logging.INFO and "detected" in msg.lower():
            return Fore.RED + msg + Fore.RESET
        return msg

def setup_logger(verbose=False):
    logger = logging.getLogger("RabbitVulnScanner")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    return logger
