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

import maltplotlib

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

"Display Chart of Female Gamers vs in Previous Years. "

country = ['A', 'B', 'C', 'D', 'E']
gdp_per_capita = [45000, 42000, 52000, 49000, 47000]

colors = ['green', 'blue', 'purple', 'brown', 'teal']
plt.bar(country, gdp_per_capita, color=colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()


# Read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())
