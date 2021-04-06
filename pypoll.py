import os
import csv 

candidates = []
vote_count = {}
percentage = {}
total_votes = 0


#open csv 
with open('Resources/election_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader, None)
    for row in csvreader[:1000]:
        if row[2] not in candidates:
            candidates.append(row[2])
            #candidates.(row[2]):
            vote_count[row[2]] = 1

print(candidates)

 # create vote counter

if row[2] in candidate and row[2] not in "Candidate":
    vote_count[row[2]] = vote_count[row[2]] + 1
        #else candidate.(row[2]):
        #    vote_count[row[2]] = 1

  # The total number of votes cast
  total_votes = int(row[0]) + vote_count    


  # The percentage of votes each candidate won
for percentages
    str(round(total_votes)*100)/(total_votes)

  # The total number of votes each candidate won
for "Kahn": len(row[2]("kahn")
    total_votes = int(row[0]) + 1
     else candidate.(row[2]):
            vote_count[row[2]] = 1

for "Correy": len(row[2]("Correy")
     total_votes = int(row[0]) + 1
     else candidate.(row[2]):
            vote_count[row[2]] = 1

for "Li": len(row[2]("Li")
     total_votes = int(row[0]) + 1
     else candidate.(row[2]):
            vote_count[row[2]] = 1

for "O'tooley":len(row[2]("O'tooley")
    total_votes = int(row[0]) + 1
     else candidate.(row[2]):
            vote_count[row[2]] = 1

  # The winner of the election based on popular vote.

for winner = winner(str)(max(vote_count))



        
eletion_output = (
f"election Results\n"
f"==================================================\n"
f"Total votes: {str(candidates)}\n"
f"==================================================\n"
f"Precentage: {percentage}%\n"
f"==================================================\n"
f"Winner: {winner}\n"
f"Greatest increase in Profits: ${str(greatest_increase)}\n"
f"Greatest decrease in Profits: ${str(greatest_decrease)}\n"
)
print(analysis_output)
with open("election_output.txt", "w") as txt_file:
    txt_file.write(election_output)








