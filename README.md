# api-load-test

## Requirements

Install `Locust`, refer to [Locust Installation](http://docs.locust.io/en/latest/installation.html)
`virtualenv` is recommended.

```bash
pip install locustio

# verify
locust --help
```

## Usage

+ Get your api running somewhere
+ Run `locust -f locustfile.py --host=api-host-server` e.g. `locust -f locustfile.py --host=https://localhost:8080`
+ Go to `http://localhost:8089/`, start load testing
