# Food Suggestion Bot
# Author: Dulneth
# Date: 6 October 2023

# A bot that asks the user what their favourite food is
# The bot identifies the type/cuisine of the food and offer a suggestion for a restaurant.

import random
import time

# Introduce trhe bot to the user
# Ask the user what their favourite food is 
print ("Hello, I'm here to suggest a restaurant for you.")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me what your favourite food is. ")
time.sleep(1)

# If they answer with an italian dish
# Suggest an italian restaurant
# List all the italian dishes
# Add one more cuisine/type/etc.
# TEst to see if it works
italian_food = ["pizza", "pasta", "canneloni", "tiramisu"]
mexican_food = ["chilaquiles", "pozole", "tacos", "enchiladas", "mole"]

if fave_food.lower().strip(",.?! ") in italian_food:
    print("I think that you might like italian restaurants")
    time.sleep(1)
    print("I suggest Bella Roma Italian Restaurant")
    print(" You can find the address below:")
    print("4460 W 10th Ave, Vancouver, BC V6R 2H9")
elif fave_food.lower().strip(",.?! ") in mexican_food:
    print("I think that you might like mexican restaurants")
    time.sleep(1)
    print("I suggest Little Mexico Cantina")
    print(" You can find the address below:")
    print("3131 Chatham St #150, Richmond, BC V7E 2Y4")
else:
    print("My algorithm is still being worked on.")
    time.sleep(1)
    print("I can't help you, sorry.😔")
