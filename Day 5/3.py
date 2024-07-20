# A tuple with nested elements
nested_tuple = ((10, 20), [30, 40], 'tuple to list')

# Tuple to list...
nested_list = list(nested_tuple)
print(f"List: {nested_list}")

# Modifying the list...
nested_list[1].append(50)

# List back to tuple...
new_tuple = tuple(nested_list)
print(f"Tuple: {new_tuple}")
