# Task 1 - multiplication table

print("\n---TASK 1--- \n")

n = int(input("Input a number: "))

# use for loop to iterate 10 times
print("\nResults of multiplication by", n, ":\n")
for i in range(1, 11):
   print(n, 'x' ,i, '=' ,n*i)


# Task 2 - pattern with loop

print("\n---TASK 2--- \n")

for i in range(10):
    print(str(i) * i)


# Task 3 - reverse the word 

print("\n---TASK 3--- \n")
word = input("Input a word to reverse: ")

print("Reversed word:", end=' ')
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

# Task 4 - upper letters

print("\n---TASK 4--- \n")

txt = "Hello, I love you, won't you tell me your name?"
for i in txt:
    if i == 'o':
        print(i.upper(), end='')
    else:
        print(i, end='')

# Task 5 - count digits and letters

print("\n---TASK 5--- \n")
characters = input("Input your characters: ")

digits_counter = 0
letters_counter = 0

for c in characters:
  if c.isdigit():
      digits_counter += 1
  else:
      letters_counter += 1

print("Number of digits: ", digits_counter)
print("Number of letters: ", letters_counter)
