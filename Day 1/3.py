def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        sum_result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {sum_result}")
        
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()

### I used float(input()) to prompt the user to enter two numbers. float() is used to convert the user input to a floating-point number to handle decimal inputs.

### Compute the sum of num1 and num2 and store it in sum_result.

### Print the sum with a formatted string that displays the numbers entered by the user and their sum.
