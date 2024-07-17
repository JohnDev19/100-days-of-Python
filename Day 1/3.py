class NamePrinter:
    def __init__(self, name):
        self.name = name

    def print_name(self, format_choice):
        if format_choice == 1:
            print(f"Hello, {self.name}!")
        elif format_choice == 2:
            print(f"Name in uppercase: {self.name.upper()}")
        elif format_choice == 3:
            print(f"Name in lowercase: {self.name.lower()}")
        elif format_choice == 4:
            print(f"Name reversed: {self.name[::-1]}")
        else:
            print("Invalid choice. Please select a valid format option.")

def main():
    try:
        name = input("Please enter your name: ")
        if not name:
            raise ValueError("Name cannot be empty")

        print("\nChoose a format for displaying your name:")
        print("1. Normal")
        print("2. Uppercase")
        print("3. Lowercase")
        print("4. Reversed")
        
        format_choice = int(input("\nEnter the number of your choice: "))

        name_printer = NamePrinter(name)
        name_printer.print_name(format_choice)
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()


## Class Definition:

## NamePrinter: A class with a constructor (__init__) that initializes the name attribute.
  
## print_name: A method that prints the name in different formats based on the user's choice. It supports normal, uppercase, lowercase, and reversed formats.
