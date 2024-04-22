"""Package helpers"""
import sys
from datetime import datetime
from uplink import retry,ratelimit, response_handler, error_handler

def common_decorators(cls):
    """Function to package all uplink decorators for reuse"""
    decorators = [
        #returns.json,
        ratelimit(calls=50, period=50),
        xc_error_handler,
        xc_response_handler,
        retry(
            when=retry.when.status(503) | retry.when.status(429),
            stop=retry.stop.after_attempt(5) | retry.stop.after_delay(20),
            backoff=retry.backoff.jittered(multiplier=2)
        )
    ]
    for decorator in decorators:
        cls = decorator(cls)
    return cls

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
def xc_response_handler(response):
    """Function to handle HTTP responses"""
    if 200 <= response.status_code < 300:
        try:
            return response.json()
        except Exception as e:
            raise OrijenXCException("Response not JSON") from e
    raise OrijenXCException("API ResponseCode")

@error_handler(requires_consumer=True)
def xc_error_handler(consumer):
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

def xc_filter_items(d: dict, keys: list) -> dict:
    """Fuction to filter XC reponse with 'items' dict"""
    items = d.get('items', [])
    filtered_items = [{key: d[key] for key in keys if key in d} for d in items]
    return {'items': filtered_items}

def xc_format_date(date_obj: datetime):
    """
    Function to format dates to what the console expects
    in
    """
    return date_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
