import os
import csv

financial_data = os.path.join("Resources", "budget_data.csv")

#Set Variables 
total_months = 0
net_total = 0
profit_loss_change = 0
avg_revenue_change = 0
recent_month_gross = 0

# Open and read csv
with open(financial_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    # print(f"Header: {csv_header}")
    first_row = next(csv_reader)
    previous_month = first_row[1] 

    # Read through each row of data after the header
    for row in csv_reader:
        current_month = row[1] 
        difference = (int(current_month) - (int(previous_month))

        
 #Calculate the total revenue over the entire period

     
    net_total = int(row[1]) + 1   
    previous_month = current_month
    

# Calculate the changes in "Profit/Losses" & average revenue change as a float 
profit_loss_change = float(row[1]) - previous_month
previous_month = float(row[1])
avg_revenue_change = sum(profit_loss_change) / sum(total_months)

#greatest increase/decrease in revenue 
greatest_increase  = max(profit_loss_change)
greatest_decrease = min(profit_loss_change)

# Print the Results
print("Financial Analysis")

print("==================================================")

print("total months" + str(total_months))
print("net_total:" + "$" + str(sum(net_total)))
print("Average change:" + "$" + str(avg_revenue_change))
print("Greatest Increase in Profits:" +str(profit_loss_change[avg_revenue_change.index(max(avg_revenue_change))+1]) +  "$" + str(greatest_increase))
print("Greatest decrease in Profits:" +str(profit_loss_change[avg_revenue_change.index(min(avg_revenue_change))+1]) + "$" + str(greatest_decrese))

#Text File 
file = open("export.txt")

file.write("Financial Analysis")
file.write("===============================================")
file.write("Total: " + "$" + str(sum(net_total)))
file.write("Average change:" + "$" + str(avg_revenue_change))
file.write("Greatest Increase in Profits:" +str(profit_loss_change[avg_revenue_change.index(max(avg_revenue_change))+1]) + "" + "$" + str(greatest_increase))
file.write("Greatest decrease in Profits:" +str(profit_loss_change[avg_revenue_change.index(min(avg_revenue_change))+1]) + "" + "$" + str(greatest_decrease))

file.closed()
