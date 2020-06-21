import json
import re
import requests
from behave import *


@given("I have mocked an endpoint")
def step_impl(context):
    # set up a mocked endpoint and response
    mocked_response = """
    {
        "request": {
            "method": "GET",
            "urlPath": "/some/thing"
        },
        "response": {
            "status": 200,
            "jsonBody": {
                "aBool": true,
                "aString": "Hello world!",
                "anInt": 5
            },
            "headers": {
                "Content-Type": "application/json"
            }
        }
    }
    """

    mapping = json.loads(mocked_response)
    requests.post(url='http://wiremock:8080/__admin/mappings', headers={'Content-Type': 'application/json'},
                  json=mapping)


@when("I call the mock endpoint")
def step_impl(context):
    context.response = requests.get('http://wiremock:8080/some/thing')


@then("I get the mocked response")
def step_impl(context):
    res = context.response
    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json'

    body = json.loads(res.text)
    assert len(body) == 3

    assert body['aBool']
    assert re.search("Hello world", body['aString'])
    assert body['anInt'] == 5
