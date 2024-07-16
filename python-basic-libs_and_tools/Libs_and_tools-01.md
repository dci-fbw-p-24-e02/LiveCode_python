# Python - Libraries & Tools:01 - CLI in PYTHON

**LAST SESSION**
- pytest: automate tests
    - we test our code to prevent bugs
- pytest is a robust Python testing tool
- pytest offers powerful features such as assert rewriting, a third-party plugin model, and a powerful yet simple fixture model

## Why pytest?

- Simple tests are simple to write in pytest.
- Complex tests are still simple to write.
- Tests are easy to read.
- You can get started in seconds.
- You use assert in tests for verifications, 
    - not things like self.assertEqual() or self.assertLessThan(). 
    - Just assert.
- You can use pytest to run tests written for unittest or nose.


```python
#code_to_test.py
def my_sum(a,b):
    return a + b

# test.py
# from code_to_test import my_sum

def test_my_sum():
    result = my_sum(5, 2)
    expected_result = 7
    assert result == expected_result # self.assertEqual(result, expected_result)

if __name__ == '__main__':
    test_my_sum()

```

## Context Managers and with Blocks

- The with statement sets up a temporary context and reliably tears it down,
- This prevents errors and reduces boilerplate code,
- Context Managers exists to control a with statement
- The with statement was designed to simplify some common uses of
try/finally, which guarantees that some operation is performed after a
block of code, even if the block is terminated

classes of context manager instances have two methods:
    - `__enter__`
    - `__exit__`

- At the top of the with, Python calls the __enter__ method of
the context manager object.
- When the with block completes or terminates
for any reason, Python calls __exit__ on the context manager object.

**Example 1 of Custom Context Manager**

```python
class MyContext:
    def __enter__(self):
        print('entering')
        return 'Bla'
    def __exit__(self, exc_type, exc_value, traceback):
        print('exiting context')
        print(exc_type)
        print(exc_value)
        print(traceback)
        return True

with MyContext() as con:
    print('in context')
    raise TypeError('Hello')
print('outside of context')
print(con)
```

In this Python code, a custom context manager class `MyContext` is defined. 
When used in a `with` statement, this class allows you to manage resources (e.g., opening and closing files) and handle exceptions in a controlled way.

**Mimick pytest.raises**

```python
    with pytest.raises(TypeError):
        raise TypeError
```
```python
    with MyRaises(KeyError):
        raise KeyError
obj = MyClass('Bla')
```

```python
class MyRaises:
    def __init__(self, type_of_exception):
        self.type_of_exception = type_of_exception

    def __enter__(self):
        print('entering')

    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type)
        if exc_type == None:
            raise AssertionError(f'{self.type_of_exception} was not raised')
        elif exc_type == self.type_of_exception:
            return True # suppress the exception


with MyRaises(KeyError):
    print('hello world')
    raise IndexError
```
- The __init__ method takes the expected exception type.
- The __enter__ method is part of the context manager protocol, we need it to be able to run it in a with statement
- The __exit__ method is called when the block within the with statement exits. It checks if an exception was raised


## CLI - Command line interface

**Objectives:**
- Understanding Command Line Interface.
- Working with command line arguments libraries:
    - sys.argv
    - getopt
    - argparse

CLI provides a way for a user to interact with a program running in a text-based shell interpreter.

### Command prompt

A command prompt (or just prompt) is a sequence of (one or more) characters used in a command-line interface to indicate readiness to accept commands.

- It literally prompts the user to take action. 
- A prompt usually includes other information, such as the path of the current working directory and the hostname.

Command prompt can be characterized by the following elements:
- A command or program
- Zero or more command line arguments

- the python interpreter can also take options:

```shell
python3 -c "print('Welcome to DCI course!')"

python3 -h
```

### Command Line Arguments

The arguments that are given after the name of the program in the command line shell of the operating system are known as Command Line Arguments.
Python provides various ways of dealing with these types of arguments.
The three most common are:
    - sys.argv
    - getopt module
    - argparse module

Python command line arguments are a subset of the command line interface. They can be composed of different types of arguments:

1. **Options** modify the behavior of a particular command or program.
2. **Arguments** represent the source or destination to be processed.
3. **Subcommands** allow a program to define more than one command with the respective set of options and arguments.


### sys module

- The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. 
- It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter. 

### sys.argv

- argv is a variable provided by the sys module which holds a list of all the arguments passed to the command line (including the script name).
