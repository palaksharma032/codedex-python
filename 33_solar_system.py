''' Challenge: Solar System

Objective: Use the math module to calculate the area of circles (planets) using mathematical constants like pi. '''
# Write code below 💖
from math import pi
from random import choice as ch

planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn'
]

# Pick a random planet
random_planet = ch(planets)

# Assign radius based on the planet
if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232
else:
    print("Oops! An error occurred.")

# Calculate surface area
area = 4 * pi * r ** 2

# Print the results with rounding
print(f"{random_planet}'s surface area is approximately {round(area)} km²")
