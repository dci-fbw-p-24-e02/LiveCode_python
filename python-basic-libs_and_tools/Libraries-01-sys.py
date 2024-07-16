import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <num1> <operator> <num2>")
        sys.exit(1)

    # Read the arguments
    num1 = sys.argv[1]
    operator =sys.argv[2]
    num2 =sys.argv[3]

    # convert arguments to proper type

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error: Both num1 and num2 should be numbers.")
        sys.exit(1)

    # Perform the operation

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == 'x':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit(1)
        result = num1 / num2
    else:
        print("Error: Unsupported operator. Use +, -, x, or /.")
        sys.exit(1)

     # Print the result
    print(f"The result of {num1} {operator} {num2} is: {result}")


if __name__=="__main__":
    main()