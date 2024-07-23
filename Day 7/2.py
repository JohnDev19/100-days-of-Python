# Dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Adding key-value pairs to the dictionary...
my_dict["occupation"] = "Engineer"
my_dict["hobby"] = "Photography"

print("Dictionary after adding elements:", my_dict)

# Removing key-value pairs from the dictionary using pop()...
removed_value = my_dict.pop("age")

print("Dictionary after removing 'age':", my_dict)
print("Removed value:", removed_value)

# Removing a key-value pair using del...
del my_dict["city"]

print("Dictionary after removing 'city':", my_dict)

# Removing a key-value pair using popitem() - removes the last inserted item
last_removed = my_dict.popitem()

print("Dictionary after removing the last inserted item:", my_dict)
print("Last removed item:", last_removed)
