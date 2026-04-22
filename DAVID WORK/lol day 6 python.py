def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Choose operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero is undefined.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator.")
                continue

            print(f"Result: {result}")

            cont = input("Do you want to calculate again? (yes/no): ").strip().lower()
            if cont!= 'yes':
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()

    

    

            







