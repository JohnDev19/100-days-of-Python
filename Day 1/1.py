class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

def main():
    try:
        name = input("Please enter your name: ")
        if not name:
            raise ValueError("Name cannot be empty")
        
        greeter = Greeter(name)
        greeter.greet()
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
