import os
import csv 
import statistics

#Import data
budget_csv = os.path.join("budget_data.csv")

# Open and red file
with open(budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") #separate data by ,
    csv_header = next(csvfile, [0]) #skip headers

    arrDatadate = [] #save dates
    arrDataprof = [] #save profit/losses
    for row in csvreader:
        arrDatadate.append(str(row[0]))
        arrDataprof.append(int(row[1]))

#Calculate average, min, max
avrg_datapl = [] 
avrg_datadeit = []
for i in range(len(arrDataprof)-1):
    diff_datapl = arrDataprof[i+1] - arrDataprof[i] #Profit/losses for each month
    avrg_datapl.append(diff_datapl)
    avrg_datadeit.append(arrDatadate[i+1]) # Save dates in array
    
max_datapl = max(avrg_datapl) #max value
min_datapl = min(avrg_datapl) #min value
ind_min = avrg_datapl.index(min_datapl) #index for min value to look for it at Date array
ind_max = avrg_datapl.index(max_datapl) #index for max value

#Export and print data
output = ["Financial Analysis\n", "-----------------------------------------\n", "Total months: " + str(len(arrDatadate)) + "\n", "Total amount: $" + str(sum(arrDataprof)) + "\n", "Average change: $" + str(round(statistics.mean(avrg_datapl),2)) + "\n", "Greatest increase in Profits: " + str(avrg_datadeit[ind_max]) + " ($" + str(max_datapl) + ")\n", "Greatest decrease in Profits: " + str(avrg_datadeit[ind_min]) + " ($" + str(min_datapl) + ")\n"]
pybank = open("PyBank_res.txt", "w")
pybank.writelines(output)
pybank.close()

for j in range(len(output)):
    print(output[j])

