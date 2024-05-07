# Python Statements and Loops

## The while loop

In this exercise, we will focus on the usage of the **while** loop, including:
 - `input()` from the user,
 - `range()` function, 
 - `in` keyword.
  
## 

## Tasks

### 

### :heavy_plus_sign: Task 1 - omitting number

Your task is to write a Python program using while loop to print out numbers from -5 to 5, without 0.
You **can't** use `break` and `continue` statements! 

- Your results should look similar to this:


```bash
-5 -4 -3 -2 -1 1 2 3 4 5
 ``` 

### :heavy_plus_sign: Task 2 - Upper and lower letters

Your task is to write a Python program using **while** loop, that iterates over given string and converts the lower letters to capital letters and vice versa.  
Print it out after changes.
>Hint: use string's methods and be careful of long texts and new lines!

>Note: You can use any text, for example from lyrics. My was:  
"Overhead the albatross
Hangs motionless upon the air
And deep beneath the rolling waves
In labyrinths of coral caves" :smiley:

- Your results should look like this:

```
oVERHEAD THE ALBATROSS hANGS MOTIONLESS UPON THE AIR aND DEEP BENEATH THE ROLLING WAVES iN LABYRINTHS OF CORAL CAVES
```


### :heavy_plus_sign: Task 3 - average of numbers

Your task is to write a Python program using **while** loop, to calculate the average of n integer numbers (input from the user). Input 0 (zero) finishes entering numbers and prints out calculations.  
>Hint: Average of **n** numbers is their sum divided by **n**,   
for example average of numbers 5, 7 and 12 is (5 + 7 + 12)/3 = 24/3 = 8. 

- Your results should look like this:


```bash
Input few integers to calculate their average!
Input 0 to exit!!!

Type a integer: 5
Type a integer: 7
Type a integer: 12
Type a integer: 0
Average of the above numbers is:  8.0
``` 

### :heavy_plus_sign: Task 4 - find a character

Your task is to write a Python program using **while** loop, to find indexes of prompted character in the given text.  
>Note: Program should be case-sensitive, what means that uppercase and lowercase letters are treated as distinct!

>Hint: use string's methods and be careful of long texts and new lines!  


>Note: You can use any text, for example from lyrics. My was:  
"She came to me one morning
One lonely Sunday morning
Her long hair flowing in the mid-winter wind
I know not how she found me
For in darkness I was walking
And destruction lay around me from a fight I could not win"

- Your results should look like this:


```
Text:

She came to me one morning
One lonely Sunday morning
Her long hair flowing in the mid-winter wind
I know not how she found me
For in darkness I was walking
And destruction lay around me from a fight I could not win

What should be found?: S

Character S found at index 1
Character S found at index 39
``` 

### :heavy_plus_sign: Task 5 - find divisible numbers

Your task is to write a Python program using **while** loop, read (prompt) three numbers (a,b,c) and check how many numbers between `a` and `b` are divisible by `c`.  
Input 0 (zero) as a third number (divisor) finishes program and prints out the results.

- Your results should look like this:


```bash
Type starting integer: 1
Type ending integer: 100
Type divisor: 15


15  is divisible by 15
30  is divisible by 15
45  is divisible by 15
60  is divisible by 15
75  is divisible by 15
90  is divisible by 15


Type starting integer: 5
Type ending integer: 8
Type divisor: 0
``` 