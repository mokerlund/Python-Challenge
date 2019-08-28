#  The goal is to analyze and find:
#   * The total number of months included in the dataset
#   * The net total amount of "Profit/Losses" over the entire period
#   * The average of the changes in "Profit/Losses" over the entire period
#   * The greatest increase in profits (date and amount) over the entire period (Assuming Between Months)
#   * The greatest decrease in losses (date and amount) over the entire period (Assuming Between Months)

import csv
import sys
sys.stdout = open('profit_loss_results.txt', 'w')

#Includes Header: (Date, Profits/Losses)
budget_csv_path = "PyBank/budget_data.csv"

with open(budget_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Skip past header
    next(csv_reader)

    # counter for months:
    months = 0
    # Running total of profit/loss
    total = 0
    # Assign highest and lowest beginning value
    high_increase = 0
    low_decrease = 0
    # Assign a variable to store last month's profit/loss
    prev_row_value = 0
    # Assign Variable for average change
    avg_total = 0

    # For each row, separate the first column into two
    for row in csv_reader:

        # Increment months and add totals 
        months += 1
        total += int(row[1])
        
        if prev_row_value == 0:
            pass
        else:
            difference_value = int(row[1]) - prev_row_value

            # Find highest values
            if (difference_value > high_increase):
                high_increase = difference_value
                high_mon = row[0]
        
        # Find lowest values
            if (difference_value < low_decrease):
                low_decrease = difference_value
                low_mon = row[0]


            avg_total += difference_value

        prev_row_value = int(row[1])
        
    average = round(avg_total / (months - 1), 2)
    

    ### Print Financial Analysis ###
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average  Change: ${average}")
    print(f"Greatest Increase in Profits: {high_mon} (${high_increase})")
    print(f"Greatest Decrease in Profits: {low_mon} (${low_decrease})")