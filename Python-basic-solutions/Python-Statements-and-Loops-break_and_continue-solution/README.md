# Python Statements and Loops

## The break and continue statements

In this exercise, we will focus on the usage of the **break** and **continue** statements in loops.
 
## 

## Tasks

### 

### :heavy_plus_sign: Task 1 - omitting the number

Your task is to write Python program that prints in **one line** all the numbers from 0 to 8 except 3 and 6  

- Your results should look like this:


```bash
0 1 2 4 5 7 8
 ``` 

### :heavy_plus_sign: Task 2 - breaking the inner loop

Your task is to write Python program (using **break** statement),
that prints:  
- in first line the numbers from 0 to 7,
- in second line the numbers from 10 to 17,
- and in third line the numbers from 20 to 27.  

>Hint: You can use nested loops!  
Remember that the **break** statement terminates the loop containing it!

- Your results could look like this:


```bash
0 1 2 3 4 5 6 7 

10 11 12 13 14 15 16 17 

20 21 22 23 24 25 26 27  
``` 

### :heavy_plus_sign: Task 3 - break or continue

Your task is to write Python program (using **continue** and **break** statements), that reads (prompts) two integers.  

If first number is smaller than second number, then find all numbers between them that are divisible by 3 and print them out. Use `continue` statement!  

If first number is bigger than second number, then find first number between them that is divisible by 5 and print it out. Start iterating from bigger number and use `break` statement!  

If numbers are equal only print that information!

- Your results could look like this:


```bash
First number: 1
Second number: 11

3  is divisible by 3.
6  is divisible by 3.
9  is divisible by 3.

Finished iterating from 1  to 11

...


First number: 11
Second number: 1

10  is divisible by 5.

...


First number: 3
Second number: 3

Nothing to do, both numbers are equal!
``` 

### :heavy_plus_sign: Task 4 - dividor game

Your task is to write Python program (using **continue** and **break** statements), that reads (prompts) two integers.  

First integer **must** be bigger than 100 and must be odd!  
Second integer **must** be must be odd!  

If first number is divisible by second number, then you'll get one "point" (some variable increases by 1) and you can continue typing numbers. Use `continue` statement!  

If first number is not divisible by second number, then you'll quit the game. Use `break` statement!  

Print out information about points!

>Note: You can treat this exercise as a practice in dividing numbers in your head :smiley:

- Your results could look like this:


```bash
First number: 123
Second number: 3
You earned a point!

First number: 245
Second number: 5
You earned a point!

First number: 347
Second number: 7
You've made a mistake!

You gathered  2 point(s)!
``` 

### :heavy_plus_sign: Task 5 - only digits

Your task is to write a Python program using loop, that iterates over the entered string and counts sum of the digits in the string.  
User should be prompted to enter her/his characters with the keyboard, even without looking at it.  
Store the information about sum of the digits.  
Program should terminate after encountering '=' character in the string (if it is present there).

>Hint: use one of the string's method and try to type only letters and digits!  


- Your results could look like this:


```
Input your characters: gh1ghghg2huhjhjh3gghgv4gvgyg5ggygygyg6ygyg

Found a digit  1
Found a digit  2
Found a digit  3
Found a digit  4
Found a digit  5
Found a digit  6

Sum of digits:  21

...


Input your characters: ncuuuhuh2huhu3uhu4hhu5uhuhuhu6hh=hfd6def

Found a digit  2
Found a digit  3
Found a digit  4
Found a digit  5
Found a digit  6

Exit after finding '=' sign 
``` 