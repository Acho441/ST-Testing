import pytest
from ST_Testing.projects.hw10.fruit_basket import is_it_a_fruit


@pytest.mark.parametrize('key', ['apple', 'pear', 'banana', 'grape'])
def test_fruit_basket_good_key(key):
    # setup
    # disambiguate
    this_key = key

    # execute
    assert is_it_a_fruit(this_key)
