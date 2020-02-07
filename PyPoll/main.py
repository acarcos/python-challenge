import os
import csv 

#Import data
budget_csv = os.path.join("election_data.csv")

#Open and read file
with open(budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") #separate data by ,
    csv_header = next(csvfile, [0]) #skip headers

    #Save data in lists
    voter = []
    #county = []
    candidate = []
    for row in csvreader:
        voter.append(row[0])
        #county.append(row[1])
        candidate.append(row[2])
    # Total voters
    num_voters = len(voter)

# Using dictionaries to know the candidates and votes number
cand_dict = {
}

for i in range(len(candidate)):
    candt = candidate[i]
    
    if candt in cand_dict:
        cand_dict[candt] = cand_dict[candt] + 1
    else:
        cand_dict[candt] = 1

# To manipulate the data using lists
perc_votes = [] # Percentage of votes
values_vote = [] # Total number of votes per candidate
for values in cand_dict.values():
    values_vote.append(values)
    perc_votes.append(round((values/num_voters)*100,3))

name_cands = []  # Name of candidates  
for keys in cand_dict.keys():
    name_cands.append(keys)

max_income = max(perc_votes) # Maximum value of votes
ind_max = perc_votes.index(max_income) # Index of max value
max_candt = name_cands[ind_max] # To know which candidate has max value

# Display results
res = ["Election Results\n", "------------------------------\n", "Total votes: " + str(num_voters) + "\n", "------------------------------\n"]
win = ["------------------------------\n", "Winner: " + str(max_candt) + "\n", "------------------------------\n"]

# Pypoll variable to export and print data
pypoll = open("PyPoll_res.txt", "w")
pypoll.writelines(res)

for jj in range(len(res)):
    print(res[jj])

for ii in range(len(perc_votes)):
    pypoll.write(name_cands[ii] + ": " + str(perc_votes[ii]) + "% (" + str(values_vote[ii]) + ")\n" )
    print(name_cands[ii] + ": " + str(perc_votes[ii]) + "% (" + str(values_vote[ii]) + ")")

for kk in range(len(win)):
    print(win[kk])

pypoll.writelines(win)
pypoll.close()
