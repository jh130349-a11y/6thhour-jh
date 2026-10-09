#Name: Jerrell Amari Huffman
#Class: 6th Hour
#Assignment: HW10
import random
#1. Print "Hello World!"
print("hello world")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
A = (random.randint(1,10))
B = (random.randint(1,10))
C = (random.randint(1,10))
#3. Print A, B, and C on the same line.
print(A, B, C)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if A > 5 or A < 5 or A == 5:
        print("yippe it worked")
else:
    print("dang")
#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if B < 7 or B < 3 or B == 7 or B == 3:
        print("yippe it worked")
else:
    print("dang")
#6. Make an if statement that prints if variable C is even or odd.
if C % 2 == 0:
    print("yippe it worked")
else:
    print("dang")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
var = 3 + random.randint(1,10)
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
if var == A or var == B or var == C or var > A or var > B or var > C or var < A or var < B or var < C:
    print("yippe it worked")
else:
    print("dang")