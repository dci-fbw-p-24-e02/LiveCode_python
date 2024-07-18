# Python - Libraries & Tools:03 - Scope & Modules

> Learning Goals
>- LEGB Rule
>- Modules
>- Namespaces & Symbols
>- Libraries

**LAST SESSION**

- monkey patching:
    - change behavior in runtime

1. Testing
2. Workarounds in third party libraries

```python
import my_module

my_module.some_fun = lambda x: return x**2
```

- cli:
    - argparse
    - getopt
- two  type of options:
    1. long (--)
    2. short(-)
- we can have option that require a value and option that don't require any value
- positional args don't require an option



**sys.stdout.write**

- **Purpose:** It's a method from the `sys` module that allows you to write strings to the standard output stream, which is typically the console/terminal window.
- **Functionality:** When you call `sys.stdout.write(data)`, it sends the provided `data` (a string) to the standard output.
- **Key Points:**
    - Unlike `print`, it does **not** automatically add a newline character (`\n`) at the end. 
    - You'll need to include it manually if you want a new line after the output.
    - It's generally less convenient for everyday printing compared to `print` as it lacks the newline and formatting features.

```python
import sys
sys.stdout.write('data\n')
sys.stdout.write('data')
```


**Relationship with print**

- **Underlying Mechanism:** The `print` function in Python actually leverages `sys.stdout.write` internally.
- It writes the arguments passed to `print` to the standard output stream using `sys.stdout.write` and then adds a newline character (`\n`).

```python
print('Hello', end='\n') #default
print('World')
```

**example monkey patch the print function**

```python
import sys

my_original_write = sys.stdout.write
count = 0
def count_print(text):
    global count
    count += 1
    my_original_write(text)
    my_original_write(f'{count}\n')
    
sys.stdout.write = count_print
print('a', 'b', sep='c', end='BLA')

def print_HELLO(text):
    if not text=='\n':
        my_original_write('HELLO')

# sys.stdout.write = print_HELLO  #monkey patching

```

```python
import sys

my_original_write = sys.stdout.write

def reverse_write(text):
    reverse_string = text[::-1]
    my_original_write(reverse_string)

sys.stdout.write = reverse_write

print('Hello') # olleH
print('BLa')

sys.stdout.write = my_original_write

print('Hello') # olleH
print('BLa')

```

**Example: Context Manager with reversed print**

```python
import sys

class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write # 3.

    def reverse_write(self, text):
        reverse_string = text[::-1]
        self.original_write(reverse_string)

    def __exit__(self, exc_type, exc_msg, traceback):
        sys.stdout.write = self.original_write #6.

with LookingGlass():
    print('Hello World')
    print('Greetings')

print('Back to normal')
```

1. Python invokes __enter__ with no arguments besides self.
2. Hold the original sys.stdout.write method, so we can restore it
later.
3. (**Monkey-patch**) sys.stdout.write is overwritten it with our own
method.
4. Our replacement to sys.stdout.write reverses the text argument
and calls the original implementation.
5. Python calls __exit__ with None, None, None if all went well;
6. Restore the original method to sys.stdout.write.

