# Task 1

add15 = lambda x: x + 15

# Test cases

# print(add15(1))
# print(add15(-2))


# Task 2

isOdd = lambda x: x%2 != 0
isEven = lambda x: x%2 == 0
getParity = lambda x, parity: x%2 != 0 if parity == 'odd' else x%2 == 0

# Test cases

# print(isOdd(2), isEven(2))
# print(isOdd(1), isEven(1))
# print(getParity(2, 'odd'), getParity(2, 'even'))
# print(getParity(1, 'odd'), getParity(1, 'even'))


# Task 3

starts_with_p = lambda x: True if x.lower().startswith('p') else False

# Test cases

# print(starts_with_p("Python"))
# print(starts_with_p("JavaScript"))
# print(starts_with_p("pirate"))


# Test 4

numbers = [2, 4, 5, 7, 9, 14]
factor = 2

result = []
multiply = lambda x: x * factor
for number in numbers:
    result.append(multiply(number))

# Or
# multiply = lambda x: x * factor
# result = list(map(multiply, numbers))

# Or
# multiply_list = lambda xx: [x * factor for x in xx]
# result = multiply_list(numbers)

# Test case
print(result)
