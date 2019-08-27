#  The goal is to analyze and find:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period (Assuming Between Months)

#   * The greatest decrease in losses (date and amount) over the entire period (Assuming Between Months)


import csv

#Includes Header: (Date, Profits/Losses)
budget_csv_path = "budget_data.csv"

with open(budget_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    next(csv_reader)

    # counter for months:
    months = 0

    # Running total of profit/loss
    total = 0

    # Assign highest and lowest beginning value
    high_increase = 0
    low_decrease = 0

    # For each row, separate the first column into two
    for row in csv_reader:

        # Increment months and add totals 
        months += 1
        total += int(row[1])
    
        # Find highest values
        if (int(row[1]) > high_increase):
             high_increase = int(row[1])
             high_mon = row[0]
       
       # Find lowest values
        if (int(row[1]) < low_decrease):
            low_decrease = int(row[1])
            low_mon = row[0]
            

    average = total / months
    
    # print(average)
    # print(low_decrease)
    # print(months)
    # print(total)
    # print(row[1])

    ### Print Financial Analysis ###
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average  Change: ${average}")
    print(f"Greatest Increase in Profits: {high_mon} (${high_increase})")
    print(f"Greatest Decrease in Profits: {low_mon} (${low_decrease})")