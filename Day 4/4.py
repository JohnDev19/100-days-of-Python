def sort_list(my_list):
    try:
        # Filtering out non-numeric elements...
        numeric_elements = [element for element in my_list if isinstance(element, (int, float))]

        if not numeric_elements:
            raise ValueError("The list contains no numeric elements.")

        # Sorting the list in ascending order...
        ascending_order = sorted(numeric_elements)

        # Sorting the list in descending order...
        descending_order = sorted(numeric_elements, reverse=True)

        return ascending_order, descending_order
    except ValueError as e:
        return str(e)

def main():
    # Creating a list with various data types...
    my_list = [5, 3, 8, 1.5, "hello", 2, 9, 4.5, "world"]
    print(f"Original list: {my_list}")

    result = sort_list(my_list)

    if isinstance(result, tuple):
        ascending_order, descending_order = result
        print(f"List sorted in ascending order: {ascending_order}")
        print(f"List sorted in descending order: {descending_order}")
    else:
        print(f"Error: {result}")

if __name__ == "__main__":
    main()
