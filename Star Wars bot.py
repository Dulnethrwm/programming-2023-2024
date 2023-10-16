# Title: Star Wars Bot
# Author: Dulneth
# Date: 16 October 2023

import time

# Introduce to the user
print("Hey. I'm a Star Wars Bot!")
time.sleep(0.5)
print("I'm here to decide whether you can join the Dark Side.")

fave_colour = input("What's your favourite color?")
time.sleep(1)
fave_cape = input("Do you like capes?")

if fave_colour.lower().strip("!.,?") == "red" and fave_cape.lower().strip("!.,?") == "yes":
	print("Dark Side it is.")
elif fave_colour.lower().strip() == "red" and fave_cape.lower().strip("!.,?") == "no":
	print("Dark Side it is.")
elif fave_cape.lower().strip("!.,?") == "yes":
	print("Dark Side it is.")
else:
	print("It seems like Light Side.")

