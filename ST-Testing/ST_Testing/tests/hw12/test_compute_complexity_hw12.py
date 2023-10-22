import pytest
from ST_Testing.projects.hw12.compute_complexity_hw12 import compute_complexity

"""
Testable Things:
Does the function return a float?

Does a complex password return at least a complexity score higher then 50?

Does a password that use the wrong complexifiers return a score below 50?

Does using anything other then a string for the password return an error?

Variables that will be used during testing:
testdata1: contains complex passwords
testdata2: contains password's that are wrong and dont have any complexity,
and using wrong complexifiers
testdata3: contains passwords that are partially correct with some of the
complexifiers being recognized, and some not
testdata4: contains ints
testdata5: contains list
testdata6: contains floats
"""

testdata1 = ['ap&p@@@#le=', 'b@a#n@@a+-n_a', 'a-@@@v#o&c++ado']
testdata2 = ['av', 'a`']
testdata3 = ['av@^!k', 'a`kcs*@']
testdata4 = [1, 4, 9, 15]
testdata5 = [[]]
testdata6 = [1.4, 2.5, 6.7]


# Check that the returned complexity is a float for correct passwords
@pytest.mark.parametrize('test_input', [testdata1, testdata2, testdata3])
def test_check_float_result(test_input):
    assert isinstance(compute_complexity(test_input), float)


# Check If complexity returned is larger then 50 for complex password
@pytest.mark.parametrize('test_input', testdata1)
def test_check_result_complexity(test_input):
    assert compute_complexity(test_input) > 50


# Check that when you enter a non complex password returns a 0 for complexity
@pytest.mark.parametrize('test_input', testdata2)
def test_check_result_complexity_noncomplex_password(test_input):
    assert compute_complexity(test_input) == 0


# Check that the partially complex password has a complexity less then 50
@pytest.mark.parametrize('test_input', testdata3)
def test_check_result_complexity_partially_complex_password(test_input):
    assert compute_complexity(test_input) < 50


# Check that when you enter a int an TypeError is raised
@pytest.mark.parametrize('test_input', testdata4)
def test_check_result_complexity_int_input(test_input):
    with pytest.raises(TypeError):
        compute_complexity(test_input)


# Check that when you enter a list an ZeroDivisionError is raised
@pytest.mark.parametrize('test_input', testdata5)
def test_check_result_complexity_list_input(test_input):
    with pytest.raises(ZeroDivisionError):
        compute_complexity(test_input)


# Check that when you enter a float an TypeError is raised
@pytest.mark.parametrize('test_input', testdata6)
def test_check_result_complexity_float_input(test_input):
    with pytest.raises(TypeError):
        compute_complexity(test_input)
