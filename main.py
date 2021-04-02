"""
An application to generate several names
"""

# Import the logo
from logo import logo
import random

# Default application displays
print(logo)
print('The application generates three name combinations, choose your preferred one.')
print('The following inputs will be used to generate a band name.')
print('The following are examples of expected inputs: purple, 4, four, influx\n')


def start_generating():
    is_continue = True
    while is_continue:

        # Add the inputs to a list
        response = []

        for _ in range(3):
            user_input = input('Enter a word or number: ').capitalize()

            if " " in user_input:
                print('\nSpace not allowed, input must be a word or number\nStarting again...')
                response.clear()
                break
            else:
                response.append(user_input)

        else:
            is_continue = False
            print(response)


start_generating()
