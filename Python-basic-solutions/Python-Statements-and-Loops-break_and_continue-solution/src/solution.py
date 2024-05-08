# Task 1 - omitting the number

print("\n---TASK 1--- \n")

for x in range(9):
    if (x == 3 or x == 6):
        continue
    print(x, end=' ')
print("\n")


# Task 2 - breaking the inner loop

print("\n---TASK 2--- \n")

for x in range(3):
    for y in range(10):
        if (y == 8):
            print("\n")    
            break
        print(10 * x + y, end=' ')


# Task 3 - break or continue

print("\n---TASK 3--- \n")

a = int(input("First number: "))
b = int(input("Second number: "))
print("")

if a < b:
    for i in range(a, b):
        if i % 3 == 0:
            print(i, " is divisible by 3.")
            continue
    else:
        print("\nFinished iterating from", a, " to", b)
elif a > b:
    for i in range(a, b, -1):
        if i % 5 == 0:
            print(i, " is divisible by 5.")
            break
    else:
        print("\nFinished iterating from", b, " to", a)
else:
    print("Nothing to do, both numbers are equal!")


# Task 4 - dividor game

print("\n---TASK 4--- \n")

a = 101
b = 3
points = 0

while True:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    if a > 100 and a % 2 != 0 and b % 2 != 0 and a % b == 0:
        points += 1
        print("You earned a point!\n")
        continue
    else:
        print("You've made a mistake!\n")
        break
print("You gathered ", points, "point(s)!")


# Task 5 - only digits

print("\n---TASK 5--- \n")
characters = input("Input your characters: ")
print("")

sum_of_digits = 0

for c in characters:
  if c.isdigit():
      print("Found a digit ", c)
      sum_of_digits += int(c)
      continue
  if c == '=':
      print("\nExit after finding '=' sign ")
      break

print("\nSum of digits: ", sum_of_digits)
