# Chatbot
# Author: Dulneth
# Date: 21 September 2023

import random
import time

# Greet the user
# Pause in between lines of dialogue
print("Hello There!")
time.sleep(2)

print ("I'm a crude chatbot, here to talk to you.")
time.sleep(1.5)

# Get the user's name and store in a variable
user_name = input("So... what's your name?")
# Respond with the user's name
print(f"It's nice to meet you, {user_name}")
time.sleep(2)

# Ask the user what their favourite food is
favourite_food = input("What's your favourite food?")
time.sleep(0.5)

#If they answer pasta, respond with something related
if favourite_food == "pasta":
    print("🍝")
    print("I think I love pasta too!")
elif favourite_food == "burgers" or favourite_food == "Burgers":
    print("🍔")
    print("Mmmmmmmmm, Burgers!")
elif favourite_food == "Pizza" or favourite_food == "pizza":
    print("🍕")
    print("Pizza is delicious!")
else:
    # Respond with something that is not repetitive
    # Create a list of appropriate responses
    list_of_fave_food_responses = [
        "Mmmmmmm, That sounds delicious.", 
        f"Yes, {favourite_food} is one of my favourites, too!",
        "Cool.",
        "Interesting, I've never tried that before."
    ]
    # Choose one response randomly from the list

    random_response = random.choice(list_of_fave_food_responses)

    # Print out the chosen response
    print(random_response)