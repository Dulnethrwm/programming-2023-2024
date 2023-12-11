#AOC Day 1
# Author: Dulneth
# Date: 30 November 2023

# Get the biggest amount

# Create a list to hold all the calories of elves
elves = []

# Open the file
with open("./aocday1.txt") as f:
    # Calories of the current elf
    current_cals = 0
    
    for line in f:
        # If there's anything in the line
        if line.strip():
            current_cals += int(line.strip())
        else:
            # dump current_cals into elves list
            elves.append(current_cals)

            # reset currrent_cals for next elf
            current_cals = 0

print(elves)   
print(max(elves))

# Get the top three and sum them
print(sum(sorted(elves)[-3:]))