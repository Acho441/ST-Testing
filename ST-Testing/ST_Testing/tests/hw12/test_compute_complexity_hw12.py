import pytest
from ST_Testing.projects.hw12.compute_complexity_hw12 import compute_complexity

"""
Testable Things for compute_complexity:
inputs
    happy path
        strings
    unhappy path (returns error)
        anything other than a string
outputs
    returns correct float
logic
    complex passwords
        returns float > 50
    completely complex passwords
        returns float == 100
    partially-complex
        returns float < 50
    non-complex
        returns == 0


Variables that will be used during testing:
testdata1: contains complex passwords
testdata2: contains password's that are wrong and dont have any complexity,
and using wrong complexifiers
testdata3: contains passwords that are partially correct with some of the
complexifiers being recognized, and some not
testdata4: contains ints
testdata5: contains list
testdata6: contains floats
testdata7: contains complexity 100 passwords
"""

testdata1 = ['ap&p@@@#le=', 'b@a#n@@a+-n_a', 'a-@@@v#o&c++ado']
testdata2 = ['av', 'a`']
testdata3 = ['av@^!k', 'a`kcs*@']
testdata4 = [1, 4, 9, 15]
testdata5 = [[]]
testdata6 = [1.4, 2.5, 6.7]
testdata7 = ['######', '@@@@@@@@@']


# Check that the returned complexity is a float for correct passwords
@pytest.mark.parametrize('password_input', [testdata1, testdata2, testdata3])
def test_check_float_result(password_input):
    assert isinstance(compute_complexity(password_input), float)


# Check that returned complexity is the correct math
@pytest.mark.parametrize('password_input', [testdata1, testdata2, testdata3])
def test_check_result(password_input):
    complexifiers = ['~', '@', '#', '$', '%', '^', '&', '-', '_', '+', '=']

    num_complexifiers = 0

    for char in password_input:
        if char in complexifiers:
            num_complexifiers = num_complexifiers + 1

    # compute the complexity
    length_of_data = len(password_input)
    complexity = (num_complexifiers * 100) / length_of_data
    assert compute_complexity(password_input) == complexity


# Check If complexity returned is larger then 50 for complex password
@pytest.mark.parametrize('complex_password_input', testdata1)
def test_check_result_complexity(complex_password_input):
    assert compute_complexity(complex_password_input) > 50


# Check that when you enter a non complex password returns a 0 for complexity
@pytest.mark.parametrize('non_complex_password', testdata2)
def test_check_result_complexity_noncomplex_password(non_complex_password):
    assert compute_complexity(non_complex_password) == 0


# Check that the compute complexity method is returning 100
@pytest.mark.parametrize('check_complexity_password', testdata7)
def test_check_result_complexity_complex(check_complexity_password):
    assert compute_complexity(check_complexity_password) == 100


# Check that the partially complex password has a complexity less then 50
@pytest.mark.parametrize('partially_complex_password', testdata3)
def test_complexity_partially_complex(partially_complex_password):
    assert compute_complexity(partially_complex_password) < 50


# Check that when you enter a int an TypeError is raised
@pytest.mark.parametrize('int_input', testdata4)
def test_check_result_complexity_int_input(int_input):
    with pytest.raises(TypeError):
        compute_complexity(int_input)


# Check that when you enter a list an ZeroDivisionError is raised
@pytest.mark.parametrize('list_input', testdata5)
def test_check_result_complexity_list_input(list_input):
    with pytest.raises(ZeroDivisionError):
        compute_complexity(list_input)


# Check that when you enter a float an TypeError is raised
@pytest.mark.parametrize('float_input', testdata6)
def test_check_result_complexity_float_input(float_input):
    with pytest.raises(TypeError):
        compute_complexity(float_input)
