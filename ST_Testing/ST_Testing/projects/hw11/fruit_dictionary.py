def get_formal_name(fruit):
    """
    Get the scientific name for the supplied `fruit` common name.
    If supplied name is not a string, or is not on the list
    return a message saying "Try again"


    
    :param fruit: str, common name for a fruit
    :return formal_name: str, the formal name for the supplied fruit 
    """
    fruit_dict = {
        'apple': 'Malus domestica',
        'banana': 'Musa acuminata',
        'orange': 'Citrus × sinensis',
        'strawberry': 'Fragaria × ananassa',
        'grape': 'Vitis vinifera',
        'pineapple': 'Ananas comosus',
        'mango': 'Mangifera indica',
        'blueberry': 'Vaccinium corymbosum',
        'peach': 'Prunus persica',
        'watermelon': 'Citrullus lanatus',
        'cherry': 'Prunus avium',
        'pear': 'Pyrus',
        'plum': 'Prunus domestica',
        'raspberry': 'Rubus idaeus',
        'kiwi': 'Actinidia deliciosa',
        'lemon': 'Citrus limon',
        'avocado': 'Persea americana',
        'pomegranate': 'Punica granatum',
        'cranberry': 'Vaccinium macrocarpon',
        'grapefruit': 'Citrus × paradisi'
    }

    """
    The code belowe helps prevent error's, and reduce the 
    amount of tests required
    """
    if not isinstance(fruit, str) or len(fruit) == 0:
        return("Try Again")
    try:
        formal_name = fruit_dict[fruit]
    except:
        return("Try Again")
    return formal_name


print(get_formal_name('Apple'))