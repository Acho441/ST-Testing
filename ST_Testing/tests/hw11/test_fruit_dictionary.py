import pytest
from ST_Testing.projects.hw11.fruit_dictionary import get_formal_name, get_formal_name_updated
@pytest.mark.parametrize('test_input, expected_output', 
                        [
                             ('apple', 'Malus domestica'),
                             ('banana', 'Musa acuminata'),
                             ('orange', 'Citrus × sinensis'),
                             ('strawberry', 'Fragaria × ananassa'),
                             ('grape', 'Vitis vinifera'),
                             ('pineapple', 'Ananas comosus'),
                             ('mango', 'Mangifera indica'),
                             ('blueberry', 'Vaccinium corymbosum'),
                             ('peach', 'Prunus persica'),
                             ('watermelon', 'Citrullus lanatus'),
                             ('cherry', 'Prunus avium'),
                             ('pear', 'Pyrus'),
                             ('plum', 'Prunus domestica'),
                             ('raspberry', 'Rubus idaeus'),
                             ('kiwi', 'Actinidia deliciosa'),
                             ('lemon', 'Citrus limon'),
                             ('avocado', 'Persea americana'),
                             ('pomegranate', 'Punica granatum'),
                             ('cranberry', 'Vaccinium macrocarpon'),
                             ('grapefruit', 'Citrus × paradisi')
                        ]
)

def test_happpycase_input_updated(test_input, expected_output):
        result = get_formal_name_updated(test_input)
        assert result == expected_output

class TestFruitDictionary():
    
    def test_happycase_input(self):
        assert get_formal_name('apple') == "Malus domestica"
        assert get_formal_name('banana') == 'Musa acuminata'
        assert get_formal_name('avocado') == 'Persea americana'

    def test_int_input(self):
        assert get_formal_name(1) != str
    
    def test_list_input(self):
        assert get_formal_name([]) != str
    
    def test_float_input(self):
        assert get_formal_name(1.5) != str
    
    def test_string_input(self):
        assert get_formal_name("aappplee") != str
    
    """Tests for updated version"""
    def test_happycase_input(self):
        assert get_formal_name_updated('apple') == "Malus domestica"
        assert get_formal_name_updated('banana') == 'Musa acuminata'
        assert get_formal_name_updated('avocado') == 'Persea americana'

    def test_int_input_updated(self):
        assert get_formal_name_updated(1) == "What you entered was not a string try again"
    
    def test_list_input_updated(self):
        assert get_formal_name_updated([]) == "What you entered was not a string try again"
    
    def test_float_input_updated(self):
        assert get_formal_name_updated(1.5) == "What you entered was not a string try again"
        
    def test_string_input_updated(self):
        assert get_formal_name_updated("applee") == "What you entered was not one of the fruits in the dictionary"
    
    
    

    
    