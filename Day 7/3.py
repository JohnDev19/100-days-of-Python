# Dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}

# Accessing values using keys...
name = my_dict["name"]
age = my_dict["age"]
city = my_dict["city"]
occupation = my_dict["occupation"]

# Printing the accessed values...
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Occupation: {occupation}")

# Accessing values using the get() method...
name = my_dict.get("name")
age = my_dict.get("age")
city = my_dict.get("city")
occupation = my_dict.get("occupation")

# Printing the accessed values using get()...
print(f"Name: {name} (using get())")
print(f"Age: {age} (using get())")
print(f"City: {city} (using get())")
print(f"Occupation: {occupation} (using get())")

# Accessing a non-existent key using get() with a default value...
non_existent_key = my_dict.get("non_existent_key", "Default Value")
print(f"Non-existent key: {non_existent_key}")
