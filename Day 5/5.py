# Tuple
animal_tuple = ('cat', 'dog', 'bird', 'fish', 'horse')

# Elements to check...
elements_to_check = ['dog', 'lion', 'fish']

# Checking if the elements exist in the tuple...
for element in elements_to_check:
    if element in animal_tuple:
        print(f"The element '{element}' exists in the tuple.")
    else:
        print(f"The element '{element}' does not exist in the tuple.")
