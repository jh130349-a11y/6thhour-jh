import random
from operator import truediv
from selectors import SelectSelector

#Name:
#Class: 6th Hour
#Assignment: HW12


#1. Print Hello World!
print("hello world")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = True
admin = True

denator = random.randint(0, 1)
detor = random.randint(0, 1)
de = random.randint(0, 1)

if denator == 1:
    wifi = True
else:
    wifi = False

if detor == 1:
    login = True
else:
    login = False

if de == 1:
    admin = True
else:
    admin = False

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True and login == True and admin == True:
    print("Welcome")
elif wifi == False:
    print("no wifi")
elif login == False:
    print("please login")
elif admin == False:
    print("admin disabled")
