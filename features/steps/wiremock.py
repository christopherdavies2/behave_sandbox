import json
import re
import requests
from behave import *


@given("I have mocked an endpoint")
def step_impl(context):
    # set up a mocked endpoint and response
    file = open("../wiremock/responses/get_some_thing.json", "r")
    mocked_response = file.read()
    mapping = json.loads(mocked_response)
    requests.post(url='http://wiremock:8080/__admin/mappings', headers={'Content-Type': 'application/json'},
                  json=mapping)


@when("I call the mock endpoint")
def step_impl(context):
    context.response = requests.get('http://wiremock:8080/some/thing')


@then("I get the mocked response")
def step_impl(context):
    response = context.response
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

    file = open("../expected/responses/get_some_thing.json")
    contents = file.read()

    exp_body = json.loads(contents)
    act_body = json.loads(response.text)

    assert len(act_body) == 3
    assert act_body == exp_body

    # Example of assertion using regex
    assert re.search("Hello world", act_body['aString'])

