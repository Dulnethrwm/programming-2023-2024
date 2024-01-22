# Spotify Analyzer
# Author: Dulneth
# Date: 16 Jaanuary 2024

# Version 0.1
# - From the data set, get all the songs performed by Drake

import csv

def find_all_songs(artist: str) -> list:
    """Returns a list of all songs from a given artist"""

# Open up the file
with open("./spotify.csv") as f:
    # ---- Look for all songs performed by Drake
    #      Use linearr search
    # Create a csv reader object
    csv_reader = csv.DictReader(f)

    # Create a list to store all Drake's songs
    drake_songs = []
 
    # for every song in the .csv file
    for line in csv_reader:
        if 'artist'.lower() in line["artist"].lower():
            # add it to the Drake's songs list
            drake_songs.append(line["artist"], line["song_title"], line["danceability"])

for song in drake_songs:
    if float(song[-1]) >= 0.6:
        print(song)

# --- Sorting Algorithm
# --- Selection Sort
# Starting at the begnning of the list moving to the end
for i in range(len(drake_songs)):
    # Set the current to the smallest value
    smallest_danceability = drake_songs[i][-1]
    smallest_index = i
    # For the rest of the list
    for j in range(i + 1, len(drake_songs)):
        # Check to see if this is smaller
        if drake_songs[j][-1] < smallest_danceability:
            smallest_danceability = drake_songs[j][-1]
            smallest_index = j
# Swap the current position with the smallest number we found
drake_songs[i], drake_songs[smallest_index] = drake_songs[smallest_index], drake_songs[i]