import os
import csv

save_file="save_file.txt"

vote_count=0
candidates=[]
total_vote={"candidate":[],"total votes":[],"%":[]}

row=0
winner=''
vote=0
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    print(csvreader)
    
    for o in csvreader:
#vote count
        vote_count += 1
#candidate list
        candidates.append(str(o["Candidate"]))
#candidate votes
    for p in candidates:
        if p not in total_vote["candidate"]:
            total_vote["candidate"].append(p)
            total_vote["total votes"].append(candidates.count(p))
            total_vote["%"].append((candidates.count(p)/vote_count)*100)
       


#WINNER
for win in range(len(total_vote["candidate"])):
    if total_vote["total votes"][win]> vote:
        vote=total_vote["total votes"][win]
        winner = total_vote["candidate"][win]



 #Print Values to txt file
with open(save_file, 'w') as file:
    fields=["candidate","%","total value"]
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"{total_vote['candidate'][0]}: {round(total_vote['%'][0],2)}%,({total_vote['total votes'][0]})\n")
    file.write(f"{total_vote['candidate'][1]}: {round(total_vote['%'][1],2)}%,({total_vote['total votes'][1]})\n")
    file.write(f"{total_vote['candidate'][2]}: {round(total_vote['%'][2],2)}%,({total_vote['total votes'][2]})\n")
        