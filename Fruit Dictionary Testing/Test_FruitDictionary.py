
from FruitDictionary import get_formal_name


class TestFruitDictionary():    
    
    def test(self):
        assert get_formal_name('apple') == "Malus domestica"
        assert get_formal_name('banana') == 'Musa acuminata'
        assert get_formal_name('avocado') == 'Persea americana'

    def test_wrong_input(self):
        assert get_formal_name('Apple') == "Try Again"
        assert get_formal_name(2) == "Try Again"
        assert get_formal_name([]) == "Try Again"
    
    
    

    
    