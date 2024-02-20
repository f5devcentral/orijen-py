"""Package helpers"""
from uplink import retry, error_handler, response_handler, ratelimit, returns
from orijenpy import exception


def common_decorators(cls):
    """Function to package all uplink decorators for reuse"""
    decorators = [
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
    for decorator in decorators:
        cls = decorator(cls)
    return cls


def filter_items(d: dict, keys: list) -> dict:
    """Fuction to filter XC reponse with 'items' dict"""
    items = d.get('items', [])
    filtered_items = [{key: d[key] for key in keys if key in d} for d in items]
    return {'items': filtered_items}

