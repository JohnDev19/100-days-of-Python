def print_list_elements(my_list):
  print("The elements in the list are:")
  for index, element in enumerate(my_list):
      print(f"Element at index {index}: {element}")

if __name__ == "__main__":
  
  my_list = [42, "Hello, World!", 3.14159, True, [1, 2, 3], (4, 5, 6), {'a': 1, 'b': 2}, {7, 8, 9}]

  print(f"Original list: {my_list}")
  print_list_elements(my_list)
