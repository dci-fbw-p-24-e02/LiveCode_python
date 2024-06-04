
import random

def is_Even (num):
    if num % 2 == 0:
        return True
a = 0 
b = 0 
while a < 0.9 and (b < 10 or is_Even(b) ):
    b = b + 1
    a = random.random()
    print(a)
    print(b)
    
    
print('last ',b)