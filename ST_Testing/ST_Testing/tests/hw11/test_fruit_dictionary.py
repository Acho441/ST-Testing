import pytest
from ST_Testing.projects.hw11.fruit_dictionary import get_formal_name


class TestFruitDictionary():    
    
    def test(self):
        assert get_formal_name('apple') == "Malus domestica"
        assert get_formal_name('banana') == 'Musa acuminata'
        assert get_formal_name('avocado') == 'Persea americana'

    """
    When I tried these previously without editing the code It would break the
    code with some of these
    """
    def test_wrong_input(self):
        assert get_formal_name('Apple') == "Try Again"
        assert get_formal_name(2) == "Try Again"
        assert get_formal_name([]) == "Try Again"
        assert get_formal_name("") == "Try Again"
        

    
    
    

    
    