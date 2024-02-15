from uplink import error_handler, retry, Consumer, Path, json, get

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
@raise_xc_error
class Client(Consumer):
    def __init__(self, tenant_url, token):
        super(Client, self).__init__(base_url=tenant_url)
        self.session.headers["Authorization"] = f'APIToken {token}'

    def ns(cls):
        


    class ns(Consumer):
        def __init__(self, parent):
            self._parent = parent

        @get("/api/web/namespaces")
        def list(self) -> json:
            """List all Namespaces"""
            pass

        @get("/api/web/namespaces/{namespace}")
        def get(self, namespace: Path) -> json:
            """Get a single Namespace"""
            pass
        
        @staticmethod
        def payload(name, description = "created by orijen") -> dict:
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



