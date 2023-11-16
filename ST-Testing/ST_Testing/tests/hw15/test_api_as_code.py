import json
import pytest
from ST_Testing.projects.hw15.api_website import app
"""
Testable Things for api:
get/post
    inputs
        happy path
            strings
            ints
            floats
            lists
            bools
        unhappy path (returns error/error response)
            key error
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
        ("passwordx=", ZeroDivisionError),
        ("passwordx=abc", ZeroDivisionError),
        ("password", ZeroDivisionError),
        ("passwor=", ZeroDivisionError),
    ], ids=[
        'incorrectKeyx',
        'incorrectKeyabc',
        'incorrectKeyno=',
        'incorrectKeyr',
    ])
def test_strength_for_invalid_arg_get(client_get_endpoint, bad_input):
    data, expected_error = bad_input
    password = 'abc'
    with pytest.raises(expected_error):
        client_get_endpoint.get(f"/get_strength?{data}{password}")


@pytest.mark.parametrize('good_input', [
        # no complexity
        ('password', 'bad'),
        ('pa55word', 'bad'),

        ('@@@@@@@', 'good'),
        ('@!@b@*@@', 'good'),

        (42, 'bad'),
        (True, 'bad'),
        ([1], 'bad'),
        (2.3, 'bad'),


    ], ids=[
        'password',
        'pa55word',
        '@@@@@@@',
        '@!@b@*@@',
        '42',
        'True',
        '[1]',
        '2.3'])
def test_strength_for_valid_str_get_jj(client_get_endpoint, good_input):
    data, expected_strength = good_input
    response = client_get_endpoint.get(f"/get_strength?password={data}")
    data2 = json.loads(response.data.decode())
    assert data2.get('password') == str(data)
    assert data2.get('strength') == expected_strength


@pytest.mark.parametrize('bad_input_post', [
        ("passwordx=", ZeroDivisionError),
        ("passwordx=abc", ZeroDivisionError),
        ("password", ZeroDivisionError),
        ("passwor=", ZeroDivisionError),
    ], ids=[
        'incorrectKeyx',
        'incorrectKeyabc',
        'incorrectKeyno=',
        'incorrectKeyr',
    ])
def test_strength_for_invalid_arg_post(client_post_endpoint, bad_input_post):
    data, expected_strength = bad_input_post
    password = 'abc'
    with pytest.raises(expected_strength):
        client_post_endpoint.get(f"/get_strength?{data}{password}")


@pytest.mark.parametrize('good_input_post', [
        # no complexity
        ('password', 'bad'),
        ('pa55word', 'bad'),

        ('@@@@@@@', 'good'),
        ('@!@b@*@@k', 'good'),
        (42, 'bad'),
        (True, 'bad'),
        ([1], 'bad'),
        (2.3, 'bad'),
    ], ids=[
        'password',
        'pa55word',
        '@@@@@@@',
        '@!@b@*@@k',
        '42',
        'True',
        '[1]',
        '2.3'])
def test_strength_for_valid_str_post(client_post_endpoint, good_input_post):
    data, expected_strength = good_input_post
    response = client_post_endpoint.get(f"/get_strength?password={data}")
    data2 = json.loads(response.data.decode())
    assert data2.get('password') == str(data)
    assert data2.get('strength') == expected_strength
