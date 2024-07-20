def count_occurrences(my_list, element):
    try:
        # Counting the occurrences of the element...
        count = my_list.count(element)
        return count
    except TypeError as e:
        return f"Error: {e}"

def main():
    # Creating a list with repeated elements...
    my_list = [5, 3, 8, 5, 2, 9, 3, 5, 1, 3, 5, 8, "hello", "world", "hello", 5]
    print(f"Original list: {my_list}")

    element_to_count = 5
    result = count_occurrences(my_list, element_to_count)

    if isinstance(result, int):
        print(f"The element '{element_to_count}' occurs {result} times in the list.")
    else:
        print(result)

    element_to_count = "hello"
    result = count_occurrences(my_list, element_to_count)

    if isinstance(result, int):
        print(f"The element '{element_to_count}' occurs {result} times in the list.")
    else:
        print(result)

    # Testing with an element not in the list...
    element_to_count = 10
    result = count_occurrences(my_list, element_to_count)

    if isinstance(result, int):
        print(f"The element '{element_to_count}' occurs {result} times in the list.")
    else:
        print(result)

if __name__ == "__main__":
    main()
