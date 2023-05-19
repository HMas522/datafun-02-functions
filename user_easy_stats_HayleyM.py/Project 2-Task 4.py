"""
Purpose: Project 2 Task 4

Hayley M's Project 2

Today's Date 19May2023

"""

import math

import statistics

import doctest

import turtle

import sys

import matplotlib.pyplot as plt

import webbrowser

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

"Display Chart of Female Gamers vs in Previous Years. "

years = ['2017', '2018', '2019', '2020', '2021']
female_gamers_in_percent = [41, 45, 46, 41, 45]

colors = ['green', 'blue', 'purple', 'brown', 'teal']
plt.bar(years, female_gamers_in_percent, color=colors)
plt.title('Years Vs Female Gamers Precentage', fontsize=14)
plt.xlabel('Years', fontsize=14)
plt.ylabel('Female Gamers Percentage', fontsize=14)
plt.grid(True)
plt.show()

# ask more

str_response = input("Do you want to learn more about pet statistics? (y/n) ")

if str_response == "y":
    # import webbrowser at the top of the file
    webbrowser.open("https://explodingtopics.com/blog/number-of-gamers")

logger.info("Script complete. See log file for details.")

# Read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())
