import math
import cmath

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to calculate the power of a number
def power(x, y):
    return x ** y

# Function to calculate the square root
def square_root(x):
    return math.sqrt(x)

# Function to calculate the trigonometric functions (sin, cos, tan)
def trigonometric_functions(x, func):
    if func == 'sin':
        return math.sin(math.radians(x))
    elif func == 'cos':
        return math.cos(math.radians(x))
    elif func == 'tan':
        return math.tan(math.radians(x))
    else:
        return "Invalid function"

# Function to calculate logarithms
def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm undefined for non-positive numbers."
    return math.log(x, base)

# Function to handle complex numbers (real and imaginary)
def complex_operations(real, imag, operation):
    complex_num = complex(real, imag)
    if operation == 'abs':
        return abs(complex_num)  # Absolute value of a complex number
    elif operation == 'arg':
        return cmath.phase(complex_num)  # Argument (angle) of a complex number
    else:
        return "Invalid operation"

# Main function to run the calculator
def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Trigonometric (sin, cos, tan)")
    print("8. Logarithm")
    print("9. Complex Number Operations (abs, arg)")

    # Take user input for operation choice
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

    # Handle operations based on user choice
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")

    elif choice == '6':
        num = float(input("Enter number to find the square root: "))
        print(f"Square root of {num} is {square_root(num)}")

    elif choice == '7':
        angle = float(input("Enter angle in degrees: "))
        func = input("Choose trigonometric function (sin/cos/tan): ").lower()
        print(f"{func}({angle}) = {trigonometric_functions(angle, func)}")

    elif choice == '8':
        num = float(input("Enter number to find the logarithm: "))
        base = float(input("Enter base (default is 10): ") or 10)
        print(f"log({num}) base {base} = {logarithm(num, base)}")

    elif choice == '9':
        real = float(input("Enter real part of complex number: "))
        imag = float(input("Enter imaginary part of complex number: "))
        operation = input("Choose operation (abs/arg): ").lower()
        print(f"Result: {complex_operations(real, imag, operation)}")

    else:
        print("Invalid input! Please choose a valid operation (1-9).")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
