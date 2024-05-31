# Task 1

def countdown(number):
    """Print a countdown starting from the given number."""
    print(number)
    if number > 0:
        countdown(number - 1)


# Test cases

# countdown(5)


# Task 2

def factorial(number):
    """Return the factorial of a positive number."""
    return 1 if number <= 1 else number * factorial(number - 1)

# Or
# def factorial(number):
#     """Return the factorial of a positive number."""
#     if number <= 1:
#         return 1
#     else:
#         return number * factorial(number - 1)



# Test cases

# print(factorial(0))
# print(factorial(1))
# print(factorial(10))


# Task 3

def harmonic_sum(number):
    """Calculates the harmonic sum of an integer."""
    if number < 1:
        return 0
    else:
        return 1 / number + harmonic_sum(number - 1)

# Test cases
#
print(harmonic_sum(7))
print(harmonic_sum(4))
