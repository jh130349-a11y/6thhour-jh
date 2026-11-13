#Name: Jerrel Amari Huffman
#Class: 6th Hour
#Assignment: HW15

import time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.

i = "Hello World!"
for i in range(5, 0, -1):
    time.sleep(0.4)
    print(i)

#2. Create a for loop that counts up and prints only even numbers between 1 and 30.

for i in range(0, 32, 2 ):
    time.sleep(0.3)
    print(i)

#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.

for i in range(1, 31):
    time.sleep(0.3)
    print(i)
    if i % 3:
        print(" ")
    else:
        continue

#4. Create a for loop that prints 5 different animals from a list.

animals = ["cat", "dog", "parrot", "turtle", "bull"]

for c in animals:
    time.sleep(0.4)
    print(c)

#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")

word = "Pluh"

for letter in word[::-1]:
    print(letter)
    time.sleep(0.3)

#6. Create a list containing 10 integers of your choice and print the list.

iNTint = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(iNTint)

#7. Create two empty variables named evenNumbers and oddNumbers.

evenNumbers = []
oddNumbers = []

#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.

for number in iNTint:
    if number % 2 == 0:
        evenNumbers.append(number)
    else:
        oddNumbers.append(number)

print(evenNumbers)
print(oddNumbers)

#9. Create a variable that asks the user for an integer and an empty integer variable.
empTInt = int(input("I need an integer. (number) / "))
z3ro = 0
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)

for i in range(1, empTInt):
    empTInt *= i
print(empTInt)


