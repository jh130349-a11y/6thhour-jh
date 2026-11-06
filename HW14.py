#Name:
#Class: 6th Hour
#Assignment: HW14
import random
from time import process_time_ns

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
#i = 5
#while i >= 0:
#    print(i)
#    i -= 1
#else:
#    print("Hello World")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
#k = 1
#while k <= 30:
#    if k % 2 == 0:
#        print(k)
#    k += 1
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
#k = 1
#while k <= 30:
#    if k % 3 == 0:
#        print(k)
#    k += 1
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.

while True:
    h = random.randint(1, 6)
    print(h)
    if h == 1:
        break
#5. Create a while loop that asks for a number input until the user inputs the number 0.

while True:
    b = int(input("Input a number "))
    print(b)
    if b == 0:
        break
