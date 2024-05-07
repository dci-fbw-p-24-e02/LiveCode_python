# Task 1 - omitting number

print("\n---TASK 1--- \n")

n = -5

while n <= 5:
    if n != 0:
        print(n, end=" ")
    else:
        print("", end="")
    n += 1


# Task 2 - capitalizing words

print("\n---TASK 2--- \n")

txt = "Overhead the albatross "
txt += "Hangs motionless upon the air "
txt += "And deep beneath the rolling waves "
txt += "In labyrinths of coral caves "

i = 0

while i < len(txt):
    if txt[i].isupper():
        print(txt[i].lower(), end="")
    else:
        print(txt[i].upper(), end="")
    i += 1


# Task 3 - average of numbers

print("\n---TASK 3--- \n")

print("Input few integers to calculate their average!")
print("Input 0 to exit!!!\n")

count = 0
sum = 0.0
number = 1

while number != 0:
    number = int(input("Type a integer: "))
    sum = sum + number
    count += 1

if count == 0:
    print("Input some integers")
else:
    print("Average of the above numbers is: ", sum / (count - 1))


# Task 4 - find a character

print("\n---TASK 4--- \n")

txt = """
She came to me one morning
One lonely Sunday morning
Her long hair flowing in the mid-winter wind
I know not how she found me
For in darkness I was walking
And destruction lay around me from a fight I could not win
"""
print("Text: \n", txt)
n = 0
to_find = input("What should be found?: ")
while n < len(txt):
    if to_find == txt[n]:
        print("Character", to_find, "found at index", n)
    n += 1


# Task 5 - find divisible numbers

print("\n---TASK 5--- \n")

c = 1
while c != 0:
    a = int(input("Type starting integer: "))
    b = int(input("Type ending integer: "))
    c = int(input("Type divisor: "))
    print("\n")

    while a < b and c != 0:
        if a % c == 0:
            print(a, " is divisible by", c)
        a += 1
    print("\n")
