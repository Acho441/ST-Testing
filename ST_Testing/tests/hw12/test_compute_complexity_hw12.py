import pytest
from ST_Testing.projects.hw12.compute_complexity_hw12 import compute_complexity
@pytest.mark.parametrize('test_input', ['ap&p#le=', 'b@a#n@@an_a', 'a-v#o&c++ado'])
@pytest.mark.parametrize('test_wrong_input', ['av', 'a`'])
@pytest.mark.parametrize('test_partially_wrong_input', ['av@^!k', 'a`kcs*@'])
def test_input(test_input, test_wrong_input, test_partially_wrong_input):
    """
    Testable Things:
    -test that what is returned is a float
    -test that when a incorrect input is given a 0 is returned
    -test that when a partially incorrect input is given it gives a
     partially correct answer as the wrong complexifiers are not counted
     towards complexity
    """

    result = compute_complexity(test_input)
    wrong_result = compute_complexity(test_wrong_input)
    partially_wrong_result = compute_complexity(test_partially_wrong_input)

    # Check If what is returned Is a float
    assert isinstance(result, float)

    # Check If complexity returned is larger then 0 for correct input
    assert result > 0

    # Check that when you enter the wrong input it returns a 0 for complexity
    assert wrong_result == 0

    # Check that the partially wrong input return a complexity higher then 0
    assert partially_wrong_result > 0
