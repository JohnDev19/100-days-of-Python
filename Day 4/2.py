def add_elements_to_list(my_list, elements_to_add):
    for element in elements_to_add:
        my_list.append(element)
        print(f"Added {element} to the list. Current list: {my_list}")

def remove_elements_from_list(my_list, elements_to_remove):
    for element in elements_to_remove:
        if element in my_list:
            my_list.remove(element)
            print(f"Removed {element} from the list. Current list: {my_list}")
        else:
            print(f"Element {element} not found in the list. No removal performed.")

def main():
    # Creating an initial list...
    my_list = [1, 2, 3, 4, 5]
    print(f"Initial list: {my_list}")

    # Elements to add...
    elements_to_add = [6, 7, 8, "nine", "ten"]
    add_elements_to_list(my_list, elements_to_add)

    # Elements to remove...
    elements_to_remove = [3, 5, "ten", "eleven"]
    remove_elements_from_list(my_list, elements_to_remove)

if __name__ == "__main__":
    main()
    
