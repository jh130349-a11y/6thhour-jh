#Name:
#Class: 6th Hour
#Assignment: SC3

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
import random
import time

i = 1
while i <= 100:

    time.sleep(0.3)
    if i % 3 ==0and i % 5 ==0:
        print("FizzBuzz")
    elif i % 5 ==0:
        print("Buzz")
    elif i % 3 ==0:
        print("Fizz")
    else:
        print(i)
    i += 1