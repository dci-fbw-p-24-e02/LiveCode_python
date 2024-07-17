import argparse

def main():

    parser = argparse.ArgumentParser(description="A simple CLI calculator")

    # Add arguments
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("operator", type=str, choices=["+", "-", "x", "/"], 
                            help="Operator (one of +, -, x, /)")
    parser.add_argument("num2", type=float, help="First number")

    args = parser.parse_args()

    if args.operator == '+':
        result = args.num1 + args.num2
    elif args.operator == '-':
        result = args.num1 - args.num2
    elif args.operator == 'x':
        result = args.num1 * args.num2
    elif args.operator == '/':
        if args.num2 == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit(1)
        result = args.num1 / args.num2
    else:
        print("Error: Unsupported operator. Use +, -, x, or /.")
        sys.exit(1)

    # Print the result
    print(f"The result of {args.num1} {args.operator} {args.num2} is: {result}")

if __name__=='__main__':
    main()
