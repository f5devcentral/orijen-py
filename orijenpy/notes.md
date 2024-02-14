# Notes

```python
try:
    repo = github.create_repo(name="myproject", auto_init=True)
except github.exceptions.ConnectionError:
    # Handle client socket error:
    ...
```

Here are the HTTP client exceptions that are exposed through the _exceptions_ property:
_BaseClientException:_ Base exception for client connection errors.
_ConnectionError_: A client socket error occurred.
_ConnectionTimeout_: The request timed out while trying to connect to the remote server.
_ServerTimeout_: The server did not send any data in the allotted amount of time.
_SSLError_: An SSL error occurred.
_InvalidURL_: URL used for fetching is malformed.