
def is_it_a_fruit(fruit_candidate):
    
    fruits = ['apple', 'pear', 'bananna', 'grape']

    if fruit_candidate in fruits:
        return True
    else:
        return False

"""Here I am testing calling the method a couple times to make
   sure there arent any program breaking errors"""

print(is_it_a_fruit('pear'))
print(is_it_a_fruit([]))
print(is_it_a_fruit('Pear'))

