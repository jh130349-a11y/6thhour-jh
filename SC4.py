#Name:
#Class: 6th Hour
#Assignment: SC4
from selectors import SelectSelector

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
rating_list = []

Pc = int(input("How many players do you want? "))
i = 1
for Pc in range(1, Pc + 1):
    rating = int(input(f"Player {i} pls rate "))
    i += 1
    if rating > 5 or rating < 1:
        print("Rating must be between 1 and 5")
        break
    else:
        rating_list.append(rating)
        pass

print(rating_list)
total = sum(rating_list) / len(rating_list)
print(total)