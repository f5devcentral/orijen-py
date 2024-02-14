from uplink import error_handler, dumps, retry, returns, Consumer, Body, Path, get, post, delete

@error_handler(requires_consumer=True)
def raise_xc_error(consumer):
    if isinstance(consumer.exceptions.ServerTimeout):
        pass
    """Placeholder for now, capture all the errors"""


@retry(
    when=retry.when.status(503) | retry.when.status(429),
    stop=retry.stop.after_attempt(5) | retry.stop.after_delay(20),
    backoff=retry.backoff.jittered(multiplier=2)
)
@returns.json
@raise_xc_error
class Client(Consumer):
    def __init__(self, tenant_url, token):
        super(Client, self).__init__(base_url=tenant_url)
        self.session.headers.update({'Authorization': f'APIToken {token}'})


class Person(object):
    def __init__(self):
        pass

class Student(Person):
    def __init__(self):
        super(Student, self).__init__()

class NS(Client):
    def __init__(self):
        super(Client, self).__init__()

    @get("/api/web/namespaces")
    def list(self.client):
        """List all Namespaces"""

    @get("/api/web/namespaces/{namespace}")
    def get(self.client, namespace: Path):
        """Get a single Namespace"""
    
    @staticmethod
    def payload(name, description = "created by orijen"):
        return {
            'metadata': {
                'annotations': {},
                'description': description,
                'disable': False,
                'labels': {},
                'name': name,
                'namespace': ''
            }
        }



