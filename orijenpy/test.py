from uplink import error_handler, dumps, retry, returns, Consumer, Body, Path, get, post, delete
from resources import NS, NSSchema


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
class XC(Consumer):
    def __init__(self, tenant_url, token):
        super(XC, self).__init__(base_url=tenant_url)
        self.session.headers.update({'Authorization': f'APIToken {token}'})

    class NS(Consumer):
        @get("/api/web/namespaces")
        def list(self):
            """List all Namespaces"""

        @get("/api/web/namespaces/{namespace}")
        def get(self, namespace: Path):
            """Get a single Namespace"""

        @json
        @post("/api/web/namespaces")
        def create_ns(self, ns: Body(type=NS)):
            """Create a Namespace"""

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



