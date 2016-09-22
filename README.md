# api-load-test

## Requirements

Install `Locust`, refer to [Locust Installation](http://docs.locust.io/en/latest/installation.html)

```
pip install locustio
```

## Usage

+ Copy `config-example.py` to `config.py`, modify as needed
+ Get your api running somewhere
+ Run `locust -f locustfile.py --host=api-host-server`
+ Go to `http://localhost:8089/`, start load testing
