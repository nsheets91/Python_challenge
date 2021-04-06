import os
import csv

financial_data = os.path.join("Resources", "budget_data.csv")

#Set Variables 
total_months = 0
net_total = 0
profit_loss_change = 0
avg_revenue_change = 0
recent_month_gross = 0
profit_loss_change = []
# Open and read csv
with open(financial_data, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    # print(f"Header: {csv_header}")
    first_row = next(csv_reader)
    previous_month = first_row[1] 

    # Read through each row of data after the header
    for row in csv_reader:
        current_month = row[0] 
        total_months = total_months + 1
        #Calculate the total revenue over the entire period
        net_total = int(row[1]) + net_total    
        previous_month = current_month
        profit_loss_change.append(int(row[1]))

# Calculate the changes in "Profit/Losses" & average revenue change as a float 
#profit_loss_change = float(row[1]) - previous_month
#previous_month = float(row[1])
avg_revenue_change = sum(profit_loss_change) / total_months

#greatest increase/decrease in revenue 
greatest_increase  = max(profit_loss_change)
greatest_decrease = min(profit_loss_change)

# Print the Results
analysis_output = (
f"Financial Analysis\n"
f"==================================================\n"
f"Total Months: {str(total_months)}\n"
f"Net Total: ${str(net_total)}\n"
f"Average Change: ${str(round(avg_revenue_change, 2))}\n"
f"Greatest increase in Profits: ${str(greatest_increase)}\n"
f"Greatest decrease in Profits: ${str(greatest_decrease)}\n"
)
print(analysis_output)
#str(profit_loss_change[avg_revenue_change.index(min(avg_revenue_change))+1])
#str(profit_loss_change[avg_revenue_change.index(max(avg_revenue_change))+1])
with open("analysis_output.txt", "w") as txt_file:
    txt_file.write(analysis_output)
