"""
An application to generate band name for users
"""

# Import the logo
from logo import logo

# Default application displays
print(logo)
print("The following inputs will be used to generate a band name\n")

# Inputs
street = input("Name of your street?\n").title()
color = input("What is your favourite color?\n").title()

# Output
bandname = street + " " + color
print(f"Band Name generated is: {bandname}")
