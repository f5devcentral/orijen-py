from urllib.parse import urlparse
from uplink import retry, error_handler, response_handler, ratelimit, returns
from orijenpy import exception


def common_decorators(cls):
    common_decorators = [
        retry(
            when=retry.when.status(503) | retry.when.status(429),
            stop=retry.stop.after_attempt(5) | retry.stop.after_delay(20),
            backoff=retry.backoff.jittered(multiplier=2) 
        ),
        returns.json,
        ratelimit(calls=50, period=50),
        error_handler(exception.raise_xc_error),
        response_handler(exception.xc_status)
    ]
    for decorator in common_decorators:
        cls = decorator(cls)
    return cls


def filter_items(dict: dict, keys: list) -> dict:
    items = dict.get('items', [])
    filtered_items = [{key: d[key] for key in keys if key in d} for d in items]
    return {'items': filtered_items}
