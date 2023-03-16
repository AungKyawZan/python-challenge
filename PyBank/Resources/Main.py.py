import os
import csv

months=0
Revenue=0
avg=0
val_increase=0
val_decrease=0

diff={"date":[],"Profit/Losses":[]}
l=diff["Profit/Losses"]
diff_between_months={"date":[],"difference_between_months":[]}

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    print(csvreader)

#Total Months
    for o in csvreader:
       months += 1

#Total Revenue  (REVISIT)
       Total_Revenue = Revenue + int(o['Profit/Losses'])

#Average Change [1] Adding values to Dictionary
       diff['Profit/Losses'].append(o['Profit/Losses'])
       diff['date'].append(o['Date'])

#Average Change [2] Calculating change beweeen months
    for x, y in zip(l[0::], l[1::]):
       diff_between_months["difference_between_months"].append(int(y)-int(x))

#Average Change [3] Finding Average
    avg=sum(diff_between_months["difference_between_months"])/len(diff_between_months["difference_between_months"])

#Greatest Increase In Profit
    for i in diff_between_months["difference_between_months"]:
       if i > val_increase:
          val_increase = i
       else:
          val_increase=val_increase

#Greatest Decrease In Profit
    for i in diff_between_months["difference_between_months"]:
       if i < val_decrease:
          val_decrease = i
       else:
          val_decrease=val_decrease





#Print Values
print("Total Months:",months)
print("Total:",Total_Revenue)
print("Average Change:",avg)
print("Greatest Increase in Profits:", val_increase)
print("Greatest Decrease in Profits:", val_decrease)
       
       
       
       
       
       
       
       

    


    


