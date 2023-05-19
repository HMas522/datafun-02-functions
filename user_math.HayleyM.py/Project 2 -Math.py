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

length= int(input("Enter the length of the video game house in meters: "))
width = int(input("Enter the width of the video game house in meters: "))

area = length * width

print("The total area of your video game house is", area, "square meters.")

logger.info(f"The total area of your video game house is {area}.")

# Read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())