
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result: ", add(n1, n2))
    elif choice == '2':
        print("Result: ", subtract(n1, n2))
    elif choice == '3':
        print("Result: ", multiply(n1, n2))
    elif choice == '4':
        print("Result: ", divide(n1, n2))
    else:
        print("Invalid input")

# Run the calculator
while True:
    calculator()
    another= input("Do you want to perform another calculation? (yes/no): ")
    if another.lower() != 'yes':
        break
