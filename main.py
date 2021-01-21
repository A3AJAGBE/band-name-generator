"""
An application to generate band name for users
"""

# Import the logo
from logo import logo
import random

# Default application displays
print(logo)
print('The application generates three band name combinations, choose your preferred one.')
print("The following inputs will be used to generate a band name\n")

# Add the inputs to a list
response = []

# Inputs
street = input("Name of your street?\n").title()
response.append(street)
color = input("What is your favourite color?\n").title()
response.append(color)
band_num = int(input("How many people are in the band?\n"))
response.append(band_num)
description = input('Describe your band in one word\n').title()
response.append(description)
flower = input('What is your favourite flower\n').title()
response.append(flower)

# Generating band names
first = random.sample(response, 2)
second = random.sample(response, 2)
third = random.sample(response, 2)

# Prevent the combination of the same word twice
if first == second or first == third:
    first = random.sample(response, 2)
elif second == first or second == third:
    second = random.sample(response, 2)
else:
    third = random.sample(response, 2)

# Convert the generated band names using list comprehension
first_bandname = ' '.join(map(str, first))
second_bandname = ' '.join(map(str, second))
third_bandname = ' '.join(map(str, third))

print(f'The Band Name generated are: {first_bandname}, {second_bandname}, {third_bandname}')

