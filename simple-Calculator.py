def calculator():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /, % (modulus), ** (power)")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        elif op == "%":
            result = num1 % num2
        elif op == "**":
            result = num1 ** num2
        else:
            result = "Error: Invalid operator"

        print("Result:", result)

    except ValueError:
        print("Error: Invalid input, please enter numbers.")

if __name__ == "__main__":
    calculator()
