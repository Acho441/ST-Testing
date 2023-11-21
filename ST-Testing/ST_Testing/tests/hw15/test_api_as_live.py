import pytest
import requests
from ST_Testing.projects.hw15.api_website import app
"""
Testable Things for api:
get
    inputs
        happy path
            strings
            ints
            floats
            bools
        unhappy path (returns error/error response)
            incorrect url
            lists
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
post
    inputs
        happy path
            strings
            ints
            floats
            lists
            bools
        unhappy path (returns error/error response)
            wrong url
            non strings
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
        returns bad/error
Things I wont be extensively testing:
    Incorrect urls
        There are many different errors you can get with urls,
        and I will only test a specific part of it.
Differences between code and live testing noticed
    #
        having password with # does not create problems
        testing live
    non strings
        get live cant handle lists, and will raise
        typeError
"""


@pytest.fixture
def client_get_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def client_post_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize('bad_input', [
        ("http://127.0.0.1:5000/get_strengt"),
        ("http://127.0.0.1:5000/get_strengthh"),
        ("http://127.0.0.1:5000/get_strength=password"),
        ("http://127.0.0.1:5000/get_srength"),
    ], ids=[
        'incorrectUrlh',
        'incorrectUrlhh',
        'incorrectUrl=',
        'incorrectUrlt',
    ])
def test_strength_for_invalid_arg_get(bad_input):
    data = bad_input
    password = 'abc'
    params = {'password': password}
    res = requests.get(data, params=params)
    assert str(res) == "<Response [404]>"


@pytest.mark.parametrize('good_input', [
        # no complexity
        ('password', 'bad'),
        ('pa55word', 'bad'),

        ('@@@@@@@', 'good'),
        ('@!@b@*#a@^', 'good'),
        (42, 'bad'),
        (True, 'bad'),
        (2.3, 'bad'),
    ], ids=[
        'password',
        'pa55word',
        '@@@@@@@',
        '@!@b@*#a@^',
        '42',
        'True',
        '2.3',])
def test_strength_for_valid_str_get(good_input):
    # setup
    # disambiguate the param, by unpacking and renaming
    data, expected_strength = good_input

    # separate thet method call from the assertion
    password = data
    params = {'password': {password}}
    res = requests.get('http://127.0.0.1:5000/get_strength', params=params)
    assert str(res) == "<Response [200]>"
    result = res.json()
    assert result.get('strength') == expected_strength
    assert result.get('password') == str(password)


@pytest.mark.parametrize('bad_input_post', [
        42,
        True,
        [1],
        2.3,
    ], ids=[
        'int',
        'bool',
        'list',
        'float'
    ])
def test_strength_for_invalid_arg_post(bad_input_post):
    data = bad_input_post
    password = data
    payload = {'password': password}
    url = "http://127.0.0.1:5000/get_strength"
    res = requests.post(url, json=payload)
    assert str(res) == "<Response [500]>"


@pytest.mark.parametrize('good_input_post', [
        # no complexity
        ('password', 'bad'),
        ('pa55word', 'bad'),

        ('@@@@@@@', 'good'),
        ('@!@b@*#a@^', 'good'),
    ], ids=[
        'password',
        'pa55word',
        '@@@@@@@',
        '@!@b@*#a@^'])
def test_strength_for_valid_str_post(good_input_post):
    # setup
    # disambiguate the param, by unpacking and renaming
    data, expected_strength = good_input_post
    password = data

    payload = {'password': password}
    url = "http://127.0.0.1:5000/get_strength"
    res = requests.post(url, json=payload)
    assert str(res) == "<Response [200]>"
    result = res.json()
    assert result.get('strength') == expected_strength
    assert result.get('password') == str(password)
