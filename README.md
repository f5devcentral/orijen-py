# Project Orijen Python Client
This project defines an interface for interacting with the XC API.

Its scope is limited to low level CRUD against the XC API -- utility procedures like retrieving response data to clean a tenant, reporting to 3rd party systems on XC quota usage, or retieving SQS messages for labs/onboarding are out of scope and should be handled by other tools (using this package as a dependency).

## Usage Examples
```shell
>>> from orijenpy import session, ns
>>> api = session(tenant_url="https://tenant.console.ves.volterra.io", api_token="dLsJqnSsgxxxxxxxxxxxxxxr=")
>>> r = ns(api).list()
>>> print(r)
```

## Reference
- Based on the [uplink](https://uplink.readthedocs.io/en/stable/user/quickstart.html) library
