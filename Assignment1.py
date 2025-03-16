# Simple Calculator Program

# Get user input for the first number
num1 = float(input("Enter the first number: "))

# Get user input for the second number
num2 = float(input("Enter the second number: "))

# Get user input for the operation
operation = input("Enter the operation (+, -, *, /): ")


# Perform the operation based on the user's input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Display the result
print(f"{num1} {operation} {num2} = {result}")
