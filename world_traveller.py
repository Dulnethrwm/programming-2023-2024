# World Traveller
# Author: Dulneth
# Date: 06 November 2023

import time

# Greet the user
print("Hey! I'm a crude chatbot.")

name = input("What's your name?")

list_of_continents = ["Asia (yes or no): ", "Europe (yes or no): ", "Australia (yes or no): ", "North America (yes or no): ", "South America (yes or no):", "Africa (yes or no):" , "Antarctica (yes or no): "]

total_continents = 0

answer = ["YES"]

for continent in list_of_continents:
    time.sleep(1)
    # Get answer from the user
    answer = input(continent).lower()

    if answer == "yes":
        total_continents += 1
        time.sleep(1)

# Make the total
print(f"You have travelled to {total_continents}/7 continents")