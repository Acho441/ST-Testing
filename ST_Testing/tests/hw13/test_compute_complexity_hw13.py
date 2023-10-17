import pytest
from ST_Testing.projects.hw13.compute_complexity_hw13 import evaluate_strength
from xmlrpc.client import boolean


@pytest.mark.parametrize('test_input', ['ap&p#le=+++',
                         'b@a#n@@an_a@+', 'a-v#o&c++ado+@@'])
@pytest.mark.parametrize('test_non_string_input', [1, [], 1.2])
@pytest.mark.parametrize('test_wrong_input',
                         ['av', 'a`'])
@pytest.mark.parametrize('test_partially_wrong_input',
                         ['a**v@^!*k**', 'a`k*cs**@'])
def test_input(test_input, test_wrong_input,
               test_partially_wrong_input, test_non_string_input):
    """
    Testable Things:
    -test that what is returned is a True or False
    -test that when a non string is given that it raises a type error
    -test that when a partially incorrect input is given or wrong input
    is given it returns False as it is not strong enough.
    """

    result = evaluate_strength(test_input)
    wrong_result = evaluate_strength(test_wrong_input)
    partially_wrong_result = evaluate_strength(test_partially_wrong_input)

    # Check that what is returned is a bool
    assert isinstance(result, boolean)

    # Check that complex passwords are strong enough
    assert result is True

    # check that non string inputs return error
    with pytest.raises(TypeError):
        evaluate_strength(test_non_string_input)

    # check that false input isnt strong enough
    assert wrong_result is False

    # check that partially wrong input isnt strong enough
    assert partially_wrong_result is False
