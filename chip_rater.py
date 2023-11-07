# Chip Rate
# Author: Dulneth
# Date: 02 November 2023

# Interview people about their perception of thwe deliciousness of potato chips
# We will ask them a sett of questions.
# In the end, we will give an aggregate score.

# Greet the user
print("Please answer the following qquestions on the chip you just ate.")

# Create a list if questions to ask
questions = [
    "How crispy is the chip on a scale from 1 to 5? 5 is very crispy. 1 is mushy.",
    "How would you rate the taste from 1 to 5? 5 is the best taste ever. 1 is I would rather eat dirt.",
    "From 1 to 5, how would you rate the packaging? 5 is I would buy this JUST for the packing. 1 is Someone got paid to put this together?"
]

total_rating = 0
# For every question in that list, ask the questiopn, 
for question in questions:
    print(question)

# Get the user's rating
user_rating = int(input().strip(",.?! "))

# Add the rating to somer total-rating.
total_rating += user_rating

# Do some math on the results
# Use the average score to represent the chip's raing
average_rating = total_rating / len(questions)

# Present it.
print(f"The average rating for this chip is: {average_rating:.2f} / 5")