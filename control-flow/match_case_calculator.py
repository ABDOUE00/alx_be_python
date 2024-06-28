# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to choose the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match-case (Python 3.10+)
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
            exit()
    case _:
        print("Invalid operation. Please choose from +, -, *, /.")
        exit()

# Output the result
print(f"The result is {result}.")
