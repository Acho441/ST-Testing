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
        assert is_it_a_fruit("apple") is True

    # Wrong string test
    def test_input_wrongstring(self):
        assert is_it_a_fruit("aaappple") is False

    # Int input test
    def test_input_int(self):
        assert is_it_a_fruit(1) is False

    # Float input test
    def test_input_float(self):
        assert is_it_a_fruit(1.5) is False

    # List input test
    def test_input_list(self):
        assert is_it_a_fruit([]) is False

    # String from list input test
    def test_input_from_list(self):
        s = ["apple"]
        assert is_it_a_fruit(s[0]) is True
