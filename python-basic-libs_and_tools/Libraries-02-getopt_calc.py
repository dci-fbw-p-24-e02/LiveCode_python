import sys
import getopt

def main(argv):
    num1 = None
    num2 = None
    operator = None

    # Define the command-line options
    short_options = "a:b:o:"
    long_options = ["num1=", "num2=", "operator="]

    try:
        opts, args = getopt.getopt(argv, short_options, long_options)
        print(opts)
    except getopt.GetoptError:
        print("Usage: python calculator_getopt.py -a <num1> -b <num2> -o <operator>")
        sys.exit(2)  # Command-line syntax error

    for opt, arg in opts:
        if opt in ("-a", "--num1"):
            num1 = arg
        elif opt in ("-b", "--num2"):
            num2 = arg
        elif opt in ('-o', '--operator'):
            operator = arg

    if num1 == num2 == operator == None:
        print("Usage: python calculator_getopt.py -a <num1> -b <num2> -o <operator>")
        sys.exit(2)  # Command-line syntax error

    print(num1, num2)
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
    main(sys.argv[1:])