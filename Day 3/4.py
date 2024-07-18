def check_data_type(variable):
    var_type = type(variable)
    
    # Mapping...
    type_mapping = {
        int: "Integer",
        float: "Float",
        str: "String",
        bool: "Boolean",
        list: "List",
        tuple: "Tuple",
        dict: "Dictionary",
        set: "Set",
        frozenset: "Frozen Set",
        bytes: "Bytes",
        bytearray: "Byte Array",
        complex: "Complex Number",
        type(None): "NoneType"
    }
    
    # Getting...
    type_name = type_mapping.get(var_type, "Unknown Type")
    
    print(f"The variable '{variable}' is of type: {type_name}")

if __name__ == "__main__":
    # Testing...
    variables = [
        42,                    # Integer
        3.14159,               # Float
        "Hello, World!",       # String
        True,                  # Boolean
        [1, 2, 3],             # List
        (4, 5, 6),             # Tuple
        {'a': 1, 'b': 2},      # Dictionary
        {7, 8, 9},             # Set
        frozenset([10, 11]),   # Frozen Set
        b'hello',              # Bytes
        bytearray(b'world'),   # Byte Array
        2 + 3j,                # Complex Number
        None                   # NoneType
    ]
    
    for variable in variables:
        check_data_type(variable)
