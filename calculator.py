def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Simple Calculator")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Choose the operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice = input("Enter the number corresponding to the operation: ")
        
        if choice == '1':
            result = add(num1, num2)
            operation = "Addition"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "Multiplication"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "Division"
        else:
            result = "Invalid operation choice."
            operation = "None"
        
        print(f"{operation} result: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
