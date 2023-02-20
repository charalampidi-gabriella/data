import csv
import random

# Define the file name and column headers
filename = "random_data.csv"
headers = [ "age", "gender", "music_genre"]

# Open the file for writing
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the headers to the file
    writer.writerow(headers)

    # Write 15000 lines of random data
    for i in range(1, 15001):
        age = random.randint(18, 60)
        gender = random.randint(0, 1)
        music_genre = random.choice(["Rock", "Pop", "Hip-Hop", "Jazz", "Classical"])
        writer.writerow([age, gender, music_genre])
