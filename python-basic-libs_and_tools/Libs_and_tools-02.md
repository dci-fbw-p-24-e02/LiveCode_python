# Python - Libraries & Tools:02 - CLI in PYTHON II

> Learning Goal
>- cli
>       - getopt
>       - argparse

**LAST SESSION**
- pytest and unittest:
    - pytest is more userfriendly
    - in unittest you have to write your test cases in a class
    - in pytest you can write only function
    - pytest has very helpful assert rewrites (visual support: green and red character)
    - `with pytest.raise(KeyError)` expects that a keyerror is raised, other this would fail a test
- a context manager contain following dunder methods:
    - `__enter__` : is called when a context with a the `with` statement is opend/entered
    - `__exit__`: called when a context is terminated or exited
- cli:
    - the sys module provides us with the `argv` method
    - it returns a list with the script name and the following arguments
    - sys.argv()


**monkey patching**
In Python, monkey patching refers to the technique of dynamically modifying a module, class, or object's behavior at runtime.
It's like tinkering with a car engine while it's running!


**Functionality:**
- You can modify existing attributes or methods of a module or class.
- You can even add new attributes or methods that weren't there before.

**Common Use Cases:**
1. **Testing**
2. **Workarounds**


**Modifying Game Logic via monkey patching**

The game has a function `roll_dice()` that simulates rolling a die and 
returns a random number between 1 and 6.

- **Original Logic:**

```python
import random

def roll_dice():
    return random.randint(1, 6)

result = roll_dice()
if result == 1:
    print('critical hit')
else:
    print("You rolled a", result)
```

- **Monkey Patching for Easy Wins**

You can monkey patch the `roll_dice()` function to always return a high number:


```python
import random

def roll_dice():
    return random.randint(1, 6)

def always_six():
    return 6


roll_dice = always_six # monkey_patch roll_dice (function object) with always_six (another function object)

result = roll_dice()
if result == 1:
    print('critical hit')
else:
    print("You rolled a", result)
```

### getopt module

- getopt provides us with features that make it easier to process command line arguments in Python.
- getopt is a module that comes bundled with any standard python installation and therefore you need not install it explicitly.
- A major advantage of getopt over just using sys.argv is getopt supports switch style options ( for example: -s or --sum).
- Hence getopt supported options are position-independent.

The example $ ls -li works the same as $ ls -il

- The options are of two types:
    - Options that need a value to be passed with them. 
    - Options that behave as a flag and do not need a value.

The options can have two variations:
    - shortopts are one letter options, denoted by prefixing a single - to an option name (for example, $ ls -l)
    - longopts are a more descriptive representation of an option, denoted by prefixing two – to an option name (for example, $ ls --long-list)

```python
import sys 
import getopt

def sum_args(a, b):
    return a + b

args = sys.argv[1:]

output = getopt.getopt(args, 'a:b:', ['Number1=', 'Number2='])
opts = output
print(opts) # ([], ['1', '2'])

# positional args:
print(opts[1])
```

We can now call our script as follows:

**positional arguments:**
```shell
python Libraries-02-getopt.py 1 2
```

**short options**
```shell
python Libraries-02-getopt.py -a 1 -b 2
```

**long options**
```shell
python Libraries-02-getopt.py --Number 1 --Number2 2
```

**calculator with getopt**

```python
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
```

**Notes**
- `argv`: This parameter will hold the list of command-line arguments passed to the script (excluding the script name).
-  `short_options`: Defines short command-line options (`-a`, `-b`, `-o`), A colon `:` after an option indicates that the option requires a value.
- `long_options`: Defines long command-line options  (`--num1`, `--num2`, `--operator`)
An equal sign `=` indicates that the option requires a value.
- `getopt.getopt()`: Parses command-line options and arguments. 
- If there is an error while parsing, `getopt.GetoptError` is raised


### Introduction to `argparse`

- `argparse` is a powerful module in Python's standard library for creating command-line interfaces.
- It allows you to define what arguments your program requires, handles parsing those arguments, and automatically generates help and usage messages.

### Updated Script: `Libraries-02-calc_argparse.py`

```python
import argparse



```