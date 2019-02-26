import os
import csv

bankcsv = os.path.join("Resources","budget_data.csv")

# List to  store data
all_months = []
pl = []

with open(bankcsv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        all_months.append(row[0])
        pl.append(int(row[1]))

 #count total no of months
        total_month = len(all_months)
        print(total_month)

 #total net profit and loss
        net_pl = sum(pl)
        print(net_pl)

    #max increase and decrease
        revenue_change=[]

        
for x in range (len(pl)-1):

         revenue_change.append(pl[x+1] - pl[x])

#Avg revenue
avg_rev=round(sum(revenue_change)/len(revenue_change),2)

max_profit = revenue_change[0]
min_profit = revenue_change[0]

for x in range(len(revenue_change)):
     if revenue_change[x]> max_profit:
        max_profit=revenue_change[x]
        max_profit_month=all_months[x+1]

     elif revenue_change[x]<min_profit:
         min_profit=revenue_change[x]
         min_profit_month=all_months[x+1]

print ("Financial Analysis")
print("----------------------------------")
print("Total No of Months:" + str(total_month))
print("Net Profit and Loss:" + str(net_pl))
print("Average Change in P/L:" + str(avg_rev))
print ("Maximum Profit:" + str(max_profit)+" " + "Month:" + " " +str(max_profit_month))
print ("Minimum Profit:" + str(min_profit) + " " +"Month:"+" "+ str(min_profit_month))

output_path = os.path.join("budget.txt")
with open(output_path, 'w') as txt:
    txt.writelines('Financial Analysis\n')
    txt.writelines('----------------------------' + '\n')
    txt.writelines("Total No of Months:" + str(total_month) + '\n')
    txt.writelines("Net Profit and Loss:" + str(net_pl) + '\n')
    txt.writelines("Average Change in P/L:" + str(avg_rev) + '\n')
    txt.writelines("Maximum Profit:" + str(max_profit)+" " + "Month:" + " " +str(max_profit_month)+ '\n')
    txt.writelines("Minimum Profit:" + str(min_profit) + " " +"Month:"+" "+ str(min_profit_month))