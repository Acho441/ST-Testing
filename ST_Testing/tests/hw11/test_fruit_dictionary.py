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
                            ('grapefruit', 'Citrus × paradisi')])

def test_happpycase_input_parameterize_updated(test_input, expected_output):
    result = get_formal_name_updated(test_input)
    assert result is expected_output


class TestFruitDictionary():

    def test_happycase_input(self):
        assert get_formal_name('apple') == "Malus domestica"

    def test_int_input(self):
        with pytest.raises(KeyError):
            get_formal_name(1)

    def test_list_input(self):
        with pytest.raises(TypeError):
            get_formal_name([])

    def test_float_input(self):
        with pytest.raises(KeyError):
            get_formal_name(1.1)

    def test_wrong_string_input(self):
        with pytest.raises(KeyError):
            get_formal_name("aaplllee")

    """Tests for updated version"""
    def test_happycase_input_updated(self):
        assert get_formal_name_updated('apple') == "Malus domestica"

    def test_int_input_updated(self):
        check1 = "What you entered was not a string try again"
        assert get_formal_name_updated(1) == check1

    def test_list_input_updated(self):
        check1 = "What you entered was not a string try again"
        assert get_formal_name_updated([]) == check1

    def test_float_input_updated(self):
        check1 = "What you entered was not a string try again"
        assert get_formal_name_updated(1.5) == check1

    def test_string_input_updated(self):
        check2 = "What you entered was not one of the fruits in the dictionary"
        assert get_formal_name_updated("applee") == check2
