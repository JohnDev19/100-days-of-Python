# Method 1: Using a temporary variable
def swap_with_temp(a, b):
    print(f"Before swap (using temp): a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swap (using temp): a = {a}, b = {b}\n")
    return a, b

# Method 2: Using arithmetic operations
def swap_with_arithmetic(a, b):
    print(f"Before swap (using arithmetic): a = {a}, b = {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After swap (using arithmetic): a = {a}, b = {b}\n")
    return a, b

# Method 3: Using Python's tuple unpacking
def swap_with_tuple_unpacking(a, b):
    print(f"Before swap (using tuple unpacking): a = {a}, b = {b}")
    a, b = b, a
    print(f"After swap (using tuple unpacking): a = {a}, b = {b}\n")
    return a, b

# Method 4: Using bitwise XOR (only for integers)
def swap_with_xor(a, b):
    print(f"Before swap (using XOR): a = {a}, b = {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After swap (using XOR): a = {a}, b = {b}\n")
    return a, b

# Test the swap functions
if __name__ == "__main__":
    a = 10
    b = 20

    a, b = swap_with_temp(a, b)
    a, b = swap_with_arithmetic(a, b)
    a, b = swap_with_tuple_unpacking(a, b)
    a, b = swap_with_xor(a, b)

    # Swapping of different types
    x = "Hello"
    y = "World"
    print(f"Before swap: x = {x}, y = {y}")
    x, y = swap_with_tuple_unpacking(x, y)
    print(f"After swap: x = {x}, y = {y}")

    p = 3.14
    q = 2.71
    print(f"Before swap: p = {p}, q = {q}")
    p, q = swap_with_tuple_unpacking(p, q)
    print(f"After swap: p = {p}, q = {q}")
