import pytest
from ST_Testing.projects.hw12.compute_complexity_hw12 import compute_complexity
@pytest.mark.parametrize('test_input',['ap&p#le=', 'b@a#n@@an_a','a-v#o&c++ado'])


def test_happycase_input(test_input):
    """
    Assumptions:
    an float will be returned that represents complexity
    a string with allowed complexifiers will be entered

    Testable:
    Whether or not it returns a float
    , and works.
    """
    result = compute_complexity(test_input)
    assert isinstance(result,float)