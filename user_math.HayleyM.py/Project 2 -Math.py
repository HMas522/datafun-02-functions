"""
Purpose: Project 2 Functions and Statistics

Hayley M's Project 2

Today's Date 19May2023

"""

import math

import statistics

import doctest

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

"""In the game Monster Hunter, you are given a house to change equipment and re-stock items. How big is your video game house?"""

length= int(input("Enter the length of the video game house in meters: "))
width = int(input("Enter the width of the video game house in meters: "))

area = length * width

print("The total area of your video game house is", area, "square meters.")

logger.info(f"The total area of your video game house is {area}.")

"""Another weapon type in Monster Hunter, is the Great Sword. This is slow hits, but large damage. 
Please input the number of hits and the damanage dealt to get the total damange to the monster """

#list of hits
arr1 = [1, 150]
arr2 = [2, 100]
#calculate the product
product1 = math.prod(arr1)
product2 =math.prod(arr2)
sum = product1 + product2
print(sum)

logger.info(f"You hit once for 150 damage, then you hit twice for 100 damage. {arr1, arr2}")
logger.info(f"The total damage done to the monster is {sum}.")

"""Let's say the game input can only understand radians, not degrees. If your character moves 1 radian, how many degrees does your character turn?"""
#moving the slightly tells the charcter to move. 
print(math.degrees(1.1))

logger.info("You slightly move the joystick. The game reads this move as 1.1 radians")
logger.info(f"The character moves {math.degrees(1.1)} degrees.")


# Read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())