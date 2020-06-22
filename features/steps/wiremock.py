import json
import re
import os
from typing import TextIO

import requests
from behave import *


@given("I have mocked an endpoint")
def step_impl(context):
    # set up a mocked endpoint and response
    with open("wiremock/responses/get_some_thing.json") as json_data_file:
        mocked_response = json_data_file.read()
    mapping = json.loads(mocked_response)
    requests.post(url=f'http://{os.environ["WIREMOCK_BASE_URI"]}/__admin/mappings', headers={'Content-Type': 'application/json'},
                  json=mapping)


@when("I call the mock endpoint")
def step_impl(context):
    context.response = requests.get(f'http://{os.environ["WIREMOCK_BASE_URI"]}/some/thing')


@then("I get the mocked response")
def step_impl(context):
    response = context.response
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

    with open("expected/responses/get_some_thing.json") as json_data_file:
        contents = json_data_file.read()

    exp_body = json.loads(contents)
    act_body = json.loads(response.text)

    assert len(act_body) == 3
    assert act_body == exp_body

    # Example of assertion using regex
    assert re.search("Hello world", act_body['aString'])

