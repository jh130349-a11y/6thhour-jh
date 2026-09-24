#Name:
#Class: 6th Hour
#Assignment: HW8


#1. Import the "random" library
import random
from random import shuffle
from webbrowser import open_new

#2. print "Hello World!"
print("Hello World!")
#3. Create three different variables that each randomly generate an integer between 1 and 10
oof = random.randint(1,10)
eauh = random.randint(1,10)
mmm = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(oof, eauh, mmm)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
ooof = oof + 2
#6. Print each result from #5 on the same line.
print(ooof)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
list = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
print(list)
#8. Sort the list in #7 and print it.
list.sort()
print(list)
#9. Add together the highest three numbers in the list from #7 and print the result.
pluh = list[1] + list[2] + list[3]
print(pluh)
#10. Create a list with 5 names of other students in this class and print the list.
studentsfive = ["Braylee", "Misa", "Jerrell", "Owyn", "Nate"]
print(studentsfive)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(studentsfive)
print(studentsfive)
#12. Print a random choice from the list of names from #10.
studentsrandom = random.choice(studentsfive)
print(studentsrandom)