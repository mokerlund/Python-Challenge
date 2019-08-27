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

        # Split date by "-" and re-add columns
        new_row =  row[0].split("-")
        new_row.append(row[1])

        # Increment months and add totals 
        months += 1
        total += int(new_row[2])
    
        # Find highest values
        if (int(new_row[2]) > high_increase):
             high_increase = int(new_row[2])
             high_mon = new_row[0]
             high_year = new_row[1]
       
       # Find lowest values
        if (int(new_row[2]) < low_decrease):
            low_decrease = int(new_row[2])
            low_mon = new_row[0]
            low_year = new_row[1]
            

    average = total / months
    
    # print(average)
    # print(low_decrease)
    # print(months)
    # print(total)
    # print(new_row[2])

    ### Print Financial Analysis ###
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average  Change: ${}")
    print(f"Greatest Increase in Profits: {high_mon}-{high_year} (${high_increase})")
    print(f"Greatest Decrease in Profits: {low_mon}-{low_year} (${low_decrease})")