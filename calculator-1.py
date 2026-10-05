while True:
    print("\n===== Simple Calculator =====")

    num1 = float(input("Enter first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero."

    else:
        result = "Invalid operator."

    print("Result =", result)

    choice = input("Do you want to continue? (y/n): ")

    if choice.lower() != "y":
        break
