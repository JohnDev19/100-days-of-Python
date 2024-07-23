# Two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Elements to a set
set_a.add(9)
set_b.add(10)

# Removing elements from a set...
set_a.remove(1)
set_b.discard(8)

# Union of two sets
union_set = set_a | set_b  # or set_a.union(set_b)

# Intersection of two sets
intersection_set = set_a & set_b  # or set_a.intersection(set_b)

# Difference of two sets
difference_set = set_a - set_b  # or set_a.difference(set_b)

# Symmetric difference of two sets
symmetric_difference_set = set_a ^ set_b  # or set_a.symmetric_difference(set_b)

# Checking if one set is a subset of another...
is_subset = {4, 5}.issubset(set_a)

# Checking if one set is a superset of another...
is_superset = set_b.issuperset({6, 7})

# Printing the sets and results of operations...
print("Set A:", set_a)
print("Set B:", set_b)
print("Union of A and B:", union_set)
print("Intersection of A and B:", intersection_set)
print("Difference of A and B:", difference_set)
print("Symmetric Difference of A and B:", symmetric_difference_set)
print("Is {4, 5} a subset of Set A?:", is_subset)
print("Is Set B a superset of {6, 7}?:", is_superset)
