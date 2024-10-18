def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nSelect the operation:")
        print("1. Addition ")
        print("2. Subtraction ")
        print("3. Multiplication ")
        print("4. Division ")

        choice = input("Enter the number (1/2/3/4): ")

        if choice == '1':
            result = num1 + num2
            operation = '+'
        elif choice == '2':
            result = num1 - num2
            operation = '-'
        elif choice == '3':
            result = num1 * num2
            operation = '*'
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                operation = '/'
            else:
                return "Error: Division by zero"
        else:
            return "Invalid choice."

        return f"The result of {num1} {operation} {num2} = {result}"

    except ValueError:
        return "Invalid input. Please enter valid numbers."

print(calculator())
