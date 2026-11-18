#Name: Jerrell Amari Huffman
#Class: 6th Hour
#Assignment: HW16


#1. import the "random" library
import random
import time
from pickle import APPEND

#2. print "Hello World!"

print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
#4. Add a and b together, then divide the sum by c. Print the result.
Lst = A + B / C
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(round(Lst))

if Lst % 2 == 0:
    print("Lst is even")
else:
    print("Lst is odd")

#6. Create a list of five different random integers between 1 and 10.

Sy = [random.randint(1, 100), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),]
print(Sy)
#7. Print the 4th number in the list.
print(Sy[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
Sy.append(random.randint(1, 10))
print(Sy)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
Sy.sort()
print(Sy)
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print(i)
    i += 1
    time.sleep(3)
    if i > 100:
        break
#11. Create a list containing the names of five other students in the classroom.
STUDENT_LIST = ["Owyn", "Misa", "Nate", "Jacob", "Eden"]
#12. Create a for loop that individually prints out the names of each student in the list.
for student in STUDENT_LIST:
    print(student)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
b = 1
while i <= 100:
    print(i)
    i += 1
    time.sleep(3)
    if i % 10:
        break
#14. Free space. Do something creative. :)
animal_list = ["Penguin","Cat","Dog","Parrot","Armadillo","Owyn","Nate","Whale","Cow","Chicken","Fly","Wombat","Rhinoceros","Chinchilla","Yak","Fawn","Burro","Parastratiosphecomyiastratiosphecomyioides","Ox","Cat","Dog","Ant","Rat","Bee","Jellyfish","Snail","Squid","Your_Mom"]
print(animal_list)

