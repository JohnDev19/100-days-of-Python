# Two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union of two sets...
union_set = set_a | set_b  # or set_a.union(set_b)

# Intersection of two sets
intersection_set = set_a & set_b  # or set_a.intersection(set_b)

# Difference of two sets (elements in set_a but not in set_b)
difference_set = set_a - set_b  # or set_a.difference(set_b)

# Symmetric difference of two sets (elements in set_a or set_b but not in both)
symmetric_difference_set = set_a ^ set_b  # or set_a.symmetric_difference(set_b)

# Printing the sets and results of operations...
print("Set A:", set_a)
print("Set B:", set_b)
print("Union of A and B:", union_set)
print("Intersection of A and B:", intersection_set)
print("Difference of A and B:", difference_set)
print("Symmetric Difference of A and B:", symmetric_difference_set)
