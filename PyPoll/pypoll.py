import os
import csv

electcsv = os.path.join("Resources","election_data.csv")
with open(electcsv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    election=list(csvreader)
    vote=election[0]
    votedata=election[1:]

total=len(votedata)
print(total)
vote_candidate={}


for x in votedata:
    if x[2] not in vote_candidate:
        vote_candidate[x[2]]=1
    else:
        vote_candidate[x[2]]+=1

winner = max(vote_candidate, key=vote_candidate.get)
print(vote_candidate)

print("Election Result")
print("----------")
print("Total Vote :"+ str(total))
print("----------")
for key in vote_candidate:
    print(f'{key}: {round((vote_candidate[key]/total)*100,2)}% ({vote_candidate[key]})')
print("Winner is:"+ " "+winner)

output_path = os.path.join("Election_Output.txt")
with open(output_path, 'w') as txt:
    txt.writelines('Election Result')
    txt.writelines('------------' + '\n')
    txt.writelines("Total Vote:" + str(total) + '\n')
    txt.writelines("------------" + '\n')
    for key in vote_candidate:
        txt.writelines(f'{key}: {round((vote_candidate[key]/total)*100,2)}% ({vote_candidate[key]})+\n')
    txt.writelines("Winner is:"+ " "+winner)    