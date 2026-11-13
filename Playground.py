import random

joketeller = input("Do you want to hear a joke? (y/n)? ")
if joketeller == "y" or joketeller == "Y":
    JokeFramer = random.randint(2,2)
    if JokeFramer == 1:
        print("What did the other wave say to the other?")
        print("Nothing! They just waved.")
    elif JokeFramer == 2:
         r1 = input("Would you remember me after a year? ")
         if r1 == "y" or r1 == "Y":
              r2 = input("Would you remember me after a month? ")
              if r2 == "y" or r2 == "Y":
                  r3 = input("Would you remember me after a week? ")
                  if r3 == "y" or r3 == "Y":
                      knockknock1 = input("Knock knock ")
                      if knockknock1 == "Who's there" or knockknock1 == "Whos there" or knockknock1 == "who's there" or knockknock1 == "whos there?" or knockknock1 == "Who's there?" or knockknock1 == "Whos there?" or knockknock1 == "who's there?" or knockknock1 == "whos there?" or knockknock1 == "Who's there." or knockknock1 == "Whos there." or knockknock1 == "who's there." or knockknock1 == "whos there.":
                          print("Bro, you already forgot me?")
    elif JokeFramer == 3:
        knockknock2 = input("Knock knock ")
        if knockknock2 == "Who's there" or knockknock2 == "Whos there" or knockknock2 == "who's there" or knockknock2 == "whos there?" or knockknock2 == "Who's there?" or knockknock2 == "Whos there?" or knockknock2 == "who's there?" or knockknock2 == "whos there?" or knockknock2 == "Who's there." or knockknock2 == "Whos there." or knockknock2 == "who's there." or knockknock2 == "whos there.":
            whojoke = input("Who. ")
