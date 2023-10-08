import pytest
from ST_Testing.projects.hw10.fruit_basket import is_it_a_fruit

"""
Assumptions:
The variable given has to exactly match one of the fruits in the list
to be true.

Testable things:
-Various input types
-Happy case inputs


"""
class TestStringMethods():

    # Happy case tests
    def test_input_happycase(self):
        assert is_it_a_fruit("apple") == True
        assert is_it_a_fruit("pear") == True
        assert is_it_a_fruit("banana") == True
        assert is_it_a_fruit("grape") == True
    
    # Int input test
    def test_input_int(self):
        assert is_it_a_fruit(1) == False

    # Float input test
    def test_input_float(self):
        assert is_it_a_fruit(1.5) == False

    # List input test
    def test_input_list(self):
        assert is_it_a_fruit([]) == False
    
    

