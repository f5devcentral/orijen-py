# Project Orijen Python Client
This project defines an interface for interacting with the XC API.

Its scope is limited to CRUD against the XC API -- utility procedures like retrieving response data to clean a tenant, reporting to 3rd party systems on XC quota usage, or retieving SQS messages for labs/onboarding are handled by other tools.


## TBD
- Handle 400s with a response function
- Handle errors post retry logic
- Unified/More sane schema handling
- There is no endpoint to get a single service credential. Can they be renewed or revoked?




## Usage Examples
```shell
>>> from orijenpy import session, ns
>>> api = session(tenant_url="https://f5-gsa.console.ves.volterra.io", api_token="dLsJqnSsgxxxxxxxxxxxxxxr=")
>>> r = ns(api).list()
>>> print(r)
```

## Reference
- Based on the [Uplink](https://uplink.readthedocs.io/en/stable/user/quickstart.html) library
