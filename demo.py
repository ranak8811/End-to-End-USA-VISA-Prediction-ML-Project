# from us_visa.logger import logging

# logging.info("Logging has started")

from us_visa.exception import USvisaException
from us_visa.logger import logging
import sys

try:
    r = 10 / 0
    print(r)

except Exception as e:
    raise USvisaException(e, sys)
