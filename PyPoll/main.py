# Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

import csv

# Includes Header: (Voter ID, County, Candidate)
election_csv_path = "PyPoll/election_data.csv"


with open(election_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Starting votes = 0
    votes_cast = 0

    # Skip past header
    next(csv_reader)

    candidates = {}

    for row in csv_reader:
        
        # Increment for each vote cast
        votes_cast += 1

        # Need to create a dictionary to add new name each time one comes up
        # And add the value +1 per vote
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates.update({row[2]: 1})

        # candidates = {candidate1:vote, candidate2:vote}
        # candidates[candidate1] == vote
    print(candidates)
    print(votes_cast)

    # winner = max(candidates[candidate1], candidates[candidate2], candidates[candidate3])