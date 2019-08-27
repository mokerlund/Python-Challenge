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

    # Skip past header
    next(csv_reader)

    for row in csv_reader:
