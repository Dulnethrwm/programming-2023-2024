# Olympic Judging
# Author: Dulneth
# Date: 03 November 2023

import time
# Greet the user
print("Hey!")
judges = [
    "Judge 1: ", "Judge 2: ", "Judge 3: ", "Judge 4: ", "Judge 5: "
]

total_score = 0
time.sleep(1)

# Give the judge's score individually
for judge in judges:
    time.sleep(1)
    # Get score from judge
    score = input(judge)

    # Calculate the total score
    total_score += float(score)

# Calculate the average
average_score = total_score / len(judges)
print(f"Your averag score is {average_score}")