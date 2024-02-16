"""Exception handling for the package"""
import sys
from uplink import error_handler, response_handler

def orijen_handler(exc_type, exc_value, tb, debug: bool = False):
    """Custom exception handler to give concise errors"""
    if debug:
        sys.__excepthook__(exc_type, exc_value, tb)
    else:
        print(f"{exc_type.__name__}: {exc_value}")


sys.excepthook = orijen_handler


class OrijenXCException(Exception):
    """Class to where all exceptions should rise"""


@response_handler
def xc_status(response):
    """Function to handle HTTP responses"""
    if 200 <= response.status_code < 300:
        return response
    raise OrijenXCException("API ResponseCode")


@error_handler(requires_consumer=True)
def raise_xc_error(consumer):
    """Function to handle HTTP client errors"""
    if isinstance(consumer.exceptions.BaseClientException):
        raise OrijenXCException("BaseClientException")
    if isinstance(consumer.exceptions.ConnectionError):
        raise OrijenXCException("ConnectionError")
    if isinstance(consumer.exceptions.ConnectionTimeout):
        raise OrijenXCException("ConnectionTimeout")
    if isinstance(consumer.exceptions.ServerTimeout):
        raise OrijenXCException("ServerTimeout")
    if isinstance(consumer.exceptions.SSLError):
        raise OrijenXCException("SSLError")
    if isinstance(consumer.exceptions.InvalidURL):
        raise OrijenXCException("InvalidURL")
