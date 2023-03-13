""" Submodule file

"""

from utils.log_utils.custom_logging import CustomLogging
logger = CustomLogging.module_logger(__name__)

def add(a,b):
    c = a+b
    logger.info(f'addition result is: {c}')
    return c