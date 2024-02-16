from uplink import error_handler

@error_handler(requires_consumer=True)
def raise_xc_error(consumer):
    if isinstance(consumer.exceptions.BaseClientException):
        pass
    if isinstance(consumer.exceptions.ConnectionError):
        pass
    if isinstance(consumer.exceptions.ConnectionTimeout):
        pass
    if isinstance(consumer.exceptions.ServerTimeout):
        pass
    if isinstance(consumer.exceptions.SSLError):
        pass
    if isinstance(consumer.exceptions.InvalidURL):
        pass
        

class InvalidURLException(Exception):
    pass

class InvalidEmailException(Exception):
    pass

