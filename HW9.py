#Name: Jerrell Amari Huffman
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World!")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
lists = {
    "eye" : True,
    "iris" : "open",
    "cone_numbers" : [24800, 191613000, 241613000,  ]
}
#3. Print the keys of the dictionary from #2.
print(lists.keys())
#4. Print the values of the dictionary from #2
print(lists.values())
#5. Print one of the three numbers from the list by itself
print(lists["cone_numbers"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
lists.update({"optic_nerve" : "on"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(lists)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
list = {
  "Owyn" : {"Age" : 14, "Eye_Color" : "blue",},
  "Nate" : {"Age" : 14, "Eye_Color" : "green",},
  "Raphiel" : {"Age" : 16, "Eye_Color" : "brown",},
}
#9. Print the names of all three classmates on the same line.
print(list.keys())
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
list.pop("Raphiel")