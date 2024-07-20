def find_largest_and_smallest(my_list):
    try:
        # Filtering out non-numeric elements...
        numeric_elements = [element for element in my_list if isinstance(element, (int, float))]

        if not numeric_elements:
            raise ValueError("The list contains no numeric elements.")

        # Finding the largest and smallest elements...
        largest_element = max(numeric_elements)
        smallest_element = min(numeric_elements)

        return largest_element, smallest_element
    except ValueError as e:
        return str(e)

def main():
    # Creating a list with various data types...
    my_list = [5, 3, 8, 1.5, "hello", 2, 9, 4.5, "world"]
    print(f"Original list: {my_list}")

    result = find_largest_and_smallest(my_list)

    if isinstance(result, tuple):
        largest, smallest = result
        print(f"Largest element in the list: {largest}")
        print(f"Smallest element in the list: {smallest}")
    else:
        print(f"Error: {result}")

if __name__ == "__main__":
    main()
