import pyautogui as pg
import time
import webbrowser
points = 0

# Question
answer=pg.prompt(
"""
 What do you do when you get home
a) Watch the philly's game
b) Farm beets
c) Nothing your lonely

"""
    )
#Give Points
if answer == "a":
    points += 1
elif answer == "b"
    points += 2
elif answer == "c"
    points += 3

    # Question
answer=pg.prompt(
""" Who do you hate most
a) Toby
b) Dwight
c) Ryan the temp

"""
    )
#Give Points
if answer == "a":
    points += 1
elif answer == "b"
    points += 2
elif answer == "c"
    points += 3# Question
answer=pg.prompt(
"""
Do you have any friends
a) My couisn moe's
b) Many friends
c) You have 0 friends

"""
    )
#Give Points
if answer == "a":
    points += 1
elif answer == "b"
    points += 2
elif answer == "c"
    points += 3


    #END OF SURVEY

    pg.alert("You are...")
if points <5:
    pg.alert("Dwight")
    #Dwight
if points >=5 and points <7:
    pg.alert("Kevin")
    #Kevin
if points >= 7 :
    pg.alert("Michael")
    #Michael
