# Set
my_set = {1, 2, 3, 4, 5}

# Element to check
element = 3

# Checking if the element exists in the set...
if element in my_set:
    print(f"Element {element} exists in the set.")
else:
    print(f"Element {element} does not exist in the set.")

# Checking for an element that does not exist...
element_not_in_set = 6

if element_not_in_set in my_set:
    print(f"Element {element_not_in_set} exists in the set.")
else:
    print(f"Element {element_not_in_set} does not exist in the set.")
