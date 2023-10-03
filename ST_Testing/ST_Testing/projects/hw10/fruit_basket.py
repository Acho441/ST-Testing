
"""
I added an if statement to check whether or not the entered variable is a string
in case somebody tries putting in a list
"""

def is_it_a_fruit(fruit_candidate):
    if not isinstance(fruit_candidate,str):
        return('Fruit candidate entered Is not a string please try again')
    
    fruits = ['apple', 'pear', 'bananna', 'grape']

    if fruit_candidate in fruits:
        return True
    else:
        return False

#Here I am testing calling the method a couple times to make sure there arent any bugs
print(is_it_a_fruit('pear'))
print(is_it_a_fruit([]))
print(is_it_a_fruit('Pear'))

