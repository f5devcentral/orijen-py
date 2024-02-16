from urllib.parse import urlparse
from uplink import retry, error_handler, returns
import re
from orijenpy import exception


def common_decorators(cls):
    common_decorators = [
        retry(
            when=retry.when.status(503) | retry.when.status(429),
            stop=retry.stop.after_attempt(5) | retry.stop.after_delay(20),
            backoff=retry.backoff.jittered(multiplier=2) 
        ),
        returns.json,
        error_handler(exception.raise_xc_error)
    ]
    for decorator in common_decorators:
        cls = decorator(cls)
    return cls


def validate_url(url: str) -> str:
    '''Customize this to validate an XC console URL'''
    parsed_url = urlparse(url)
    if parsed_url.scheme and parsed_url.netloc:
        stripped_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path.rstrip('/')}"
        return stripped_url
    else:
        raise exception.InvalidURLException("Invalid URL")
    

def filter_items(dict: dict, keys: list) -> dict:
    items = dict.get('items', [])
    filtered_items = [{key: d[key] for key in keys if key in d} for d in items]
    return {'items': filtered_items}


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return email
    else:
        raise exception.InvalidEmailException("Invalid Email")
    