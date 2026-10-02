#Name: Jerrell Amari Huffman
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.
creature_list = {
"pluh" : {"dmg" : 1, "hlth" : 2, "lvl" : 1},
"rawr" : {"dmg" : 2, "hlth" : 3, "lvl" : 1},
"scratch" : {"dmg" : 3, "hlth" : 4, "lvl" : 1},
"grugh" : {"dmg" : 4, "hlth" : 5, "lvl" : 1},
"boss1" : {"dmg" : 8, "hlth" : 10, "lvl" : 1},
}


input1 = input("Select creature: pluh, rawr, scratch, grugh, boss1 : ")
print(creature_list[input1])
input2 = input("Adjust damage : ")
print(creature_listinput2)

#dang, I couldn't finish :(