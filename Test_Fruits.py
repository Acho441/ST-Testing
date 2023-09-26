
from FruitBasket import is_it_a_fruit

"""
Assumptions:
The variable given to the function is a string
The variable given has to exactly match one of the fruits in the list
to be true.

Testable things:
-The effect of lower case, and upper case letters
-The effect of miss spelling the words


"""
class TestStringMethods():

    # Testing upper case, and lower case letters
    def test_upperCase_lowercase(self):
        assert is_it_a_fruit('apple') == True
        assert is_it_a_fruit('Apple') == False

    # Testing spelling errors
    def test_spelling(self):
        assert is_it_a_fruit('bananna') == True
        assert is_it_a_fruit('bannana') == False
    
    def test_input(self):
        assert is_it_a_fruit(1) != True
        assert is_it_a_fruit(1) != False
