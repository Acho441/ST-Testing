import json
import pytest
from ST_Testing.projects.hw14.api import app  # this is the flask app
"""
Testable Things:
Can the api tell good from bad passwords in strength?
Can the api read all complexifiers?
can the api handle ints, lists, floats?

Variables:
testdata1: contains strong passwords
testdata2: contains weak passwords
testdata3: to be seen
testdata4: contains ints
testdata5: contains list
testdata6: contains floats
"""

testdata1 = ['b%^^^', 'h%^@@']
testdata2 = ['av', 'a`']
testdata3 = ['av~^!k', 'a`kcs*~']
testdata4 = [1, 4, 9, 15]
testdata5 = [[]]
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


# this is an example very negative test
def test_api_error(client):
    # disambiguate
    password = '#password'

    with pytest.raises(ZeroDivisionError):
        response = client.get(f"/get_strength?password={password}")

# test that the api can handle strong string passwords
@pytest.mark.parametrize('test_input', testdata1)
def test_strong_string(client, test_input):
    password = test_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    #convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == password
    assert data.get('strength') == 'good'

# test that passwords with incorrect complexifiers get bad strength
@pytest.mark.parametrize('test_input', testdata3)
def test_strong_string(client, test_input):
    password = test_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    #convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == password
    assert data.get('strength') == 'bad'

# test that the api recognizes not strong passwords
@pytest.mark.parametrize('test_input', testdata2)
def test_weak_string(client, test_input):
    password = test_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    #convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == password
    assert data.get('strength') == 'bad'

# test that the api can handle passwords made of ints that are not strong
@pytest.mark.parametrize('test_input', testdata4)
def test_expect_bad_int(client, test_input):
    password = test_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    #convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == str(password)
    assert data.get('strength') == 'bad'

# test that the api can handle simple lists as long as turned into string
@pytest.mark.parametrize('test_input', testdata5)
def test_expect_bad_list(client, test_input):
    password = test_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    #convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == str(password)
    assert data.get('strength') == 'bad'

# test that the api can handle simple floats as long as turned into string
@pytest.mark.parametrize('test_input', testdata6)
def test_expect_bad_float(client, test_input):
    password = test_input
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200

    #convert the json payload to a dict
    data = json.loads(response.data.decode())
    assert data.get('password') == str(password)
    assert data.get('strength') == 'bad'