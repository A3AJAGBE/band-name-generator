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


def generate_names(response_list):
    """This function uses the input list to generate names."""
    generated_list = []
    for _ in range(3):
        generated_list.append(random.sample(response_list, 2))

    print('\nGenerated Names: ')
    num = 0
    for name in generated_list:
        num += 1
        gen = ' '.join(map(str, name))
        print(f'{num}. {gen}')


def start_generating():
    is_continue = True
    while is_continue:

        # Add the inputs to a list
        response = []

        # Initial 3 prompts for the user
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
            print(f'Your Inputs: {response}')
            generate_names(response)


start_generating()
