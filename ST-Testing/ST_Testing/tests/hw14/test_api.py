import json
import pytest
import requests
from ST_Testing.projects.hw14.api import app  # this is the flask app
"""
Testable Things for api:
inputs
    happy path
        strings
    unhappy path (returns error/error response)
        live api will return error for certain things like
        #

outputs
    returns whether the password is good or bad
logic
    strong passwords
        returns good
    partially-complex passwords
        returns bad
    non-complex
        returns bad
    non-string
        returns bad

Variables:
testdata1: contains strong passwords
testdata2: contains weak passwords
testdata3: to be seen
testdata4: contains ints
testdata5: contains list
testdata6: contains floats
"""

testdata1 = ['b^^^^', 'h^^@@']
testdata2 = ['av', 'a`']
testdata3 = ['av~^!k', 'a`kcs*~']
testdata4 = [1, 4, 9, 15]
testdata5 = [[1]]
testdata6 = [1.4, 2.5]


# this is a pytest fixture
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# this is a simplified happy path test
def test_expect_good(client):
    # call the API, get the server response
    response = client.get('/get_strength?password=r%^')
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == 'r%^'
    assert data.get('strength') == 'good'


# Happy path test for getting a request
def test_live_happypath(client):
    url = "http://127.0.0.1:5000/get_strength?password=abcd"
    res = requests.get(f"{url}/get_strength?password=example")
    assert str(res) == "<Response [200]>"


# this is an example very negative test
def test_api_error(client):
    # disambiguate
    password = '#password'

    with pytest.raises(ZeroDivisionError):
        client.get(f"/get_strength?password={password}")


# Negative test for getting a request
def test_live_negative(client):
    url = "http://127.0.0.1:5000/get_strength?password=#####"
    res = requests.get(f"{url}/get_strength?password=example")
    assert str(res) == "<Response [500]>"


# test that the api can handle strong string passwords
@pytest.mark.parametrize('strong_string_input', testdata1)
def test_strong_string(client, strong_string_input: str):
    password = strong_string_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == password
    assert data.get('strength') == 'good'


# test that the live api can handle strong string passwords
@pytest.mark.parametrize('strong_string_input_live', testdata1)
def test_live_strong_string(strong_string_input_live):
    params = {'password': {strong_string_input_live}}
    url = "http://127.0.0.1:5000/get_strength"
    res = requests.get(url, params=params)
    assert str(res) == "<Response [200]>"
    result = res.json()
    assert result.get('strength') == 'good'


# test that passwords with incorrect complexifiers get bad strength
@pytest.mark.parametrize('partially_bad_string_input', testdata3)
def test_incorrect__complexifiers_string(client, partially_bad_string_input):
    password = partially_bad_string_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == password
    assert data.get('strength') == 'bad'


# test that the live api given a password with incorrect complexifiers
# gets bad strength
@pytest.mark.parametrize('partially_bad_string_input_live', testdata3)
def test_live_wrong_complexifier_string(partially_bad_string_input_live):
    params = {'password': {partially_bad_string_input_live}}
    url = "http://127.0.0.1:5000/get_strength"
    res = requests.get(url, params=params)
    assert str(res) == "<Response [200]>"
    result = res.json()
    assert result.get('strength') == 'bad'


# test that the api recognizes not strong passwords
@pytest.mark.parametrize('bad_string_input', testdata2)
def test_weak_string(client, bad_string_input: str):
    password = bad_string_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == password
    assert data.get('strength') == 'bad'


# test that the live api given a non complex password
# gets bad strength
def test_live_no_strength_string(client):
    url = "http://127.0.0.1:5000/get_strength?password=abc$defg"
    res = requests.get(f"{url}/get_strength?password=")
    assert str(res) == "<Response [200]>"
    result = res.json()
    assert result.get('strength') == 'bad'


# test that the api can handle ints but that
# it wont count them as complexifiers
@pytest.mark.parametrize('int_input', testdata4)
def test_expect_bad_int(client, int_input: int):
    password = int_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == str(password)
    assert data.get('strength') == 'bad'


# test that the api can handle simple lists
# but wont count them as complexifiers
@pytest.mark.parametrize('list_input', testdata5)
def test_expect_bad_list(client, list_input: list):
    password = list_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == str(password)
    assert data.get('strength') == 'bad'


# test that the api can handle simple floats but will
# not count them as complexifiers
@pytest.mark.parametrize('float_input', testdata6)
def test_expect_bad_float(client, float_input: float):
    password = float_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == str(password)
    assert data.get('strength') == 'bad'


# test that the live api given ints
# gets bad strength
@pytest.mark.parametrize('int_live_inputs', testdata4)
def test_live_no_strength_int(int_live_inputs):
    params = {'password': {int_live_inputs}}
    url = "http://127.0.0.1:5000/get_strength"
    res = requests.get(url, params=params)
    assert str(res) == "<Response [200]>"
    result = res.json()
    assert result.get('strength') == 'bad'


# test that the live api given a list
# gets bad strength
@pytest.mark.parametrize('list_live_inputs', testdata5)
def test_live_no_strength_list(list_live_inputs):
    params = {'password': list_live_inputs}
    url = "http://127.0.0.1:5000/get_strength"
    res = requests.get(url, params=params)
    assert str(res) == "<Response [200]>"
    result = res.json()
    assert result.get('strength') == 'bad'


# test that the live api given floats
# gets bad strength
@pytest.mark.parametrize('float_live_inputs', testdata6)
def test_live_no_strength_float(float_live_inputs):
    params = {'password': {float_live_inputs}}
    url = "http://127.0.0.1:5000/get_strength"
    res = requests.get(url, params=params)
    assert str(res) == "<Response [200]>"
    result = res.json()
    assert result.get('strength') == 'bad'
