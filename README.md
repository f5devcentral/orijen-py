# Project Orijen Python Client

## TBD
- Handle 400s with a response function
- Handle errors post retry logic
- Unified/More sane schema handling


## Usage
```shell
>>> from orijenpy import session, ns
>>> api = session(tenant_url="https://f5-gsa.console.ves.volterra.io", api_token="dLsJqnSsgxxxxxxxxxxxxxxr=")
>>> r = ns(api).list()
>>> print(r)
```

## Reference
- Based on the [Uplink](https://uplink.readthedocs.io/en/stable/user/quickstart.html) library
