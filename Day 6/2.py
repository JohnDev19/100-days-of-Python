# Empty set
my_set = set()

# Adding elements to the set...
my_set.add(10)
my_set.add(20)
my_set.add(30)

# Adding multiple elements at once using update()...
my_set.update([40, 50, 60])

# Printing the set after additions...
print("Set after adding elements:", my_set)

# Removing elements from the set using remove()...
my_set.remove(20)

# Removing elements from the set using discard()...
my_set.discard(30)

# Removing an element using pop() - removes and returns an arbitrary element...
popped_element = my_set.pop()

# Printing the set after removals...
print("Set after removing elements:", my_set)

# Printing the popped element...
print("Popped element:", popped_element)
