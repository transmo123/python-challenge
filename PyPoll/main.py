

import os
import csv
file_path= os.path.join('Resources', 'election_data.csv')

# Initialize variables to store analysis results
total_votes = 0
candidate_votes = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 

    for row in csvreader:
    # Extract voter ID, county, and candidate from the current row
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        # Count total votes
        total_votes += 1

        # Count votes for each candidate
        if candidate in candidate_votes:
                        candidate_votes[candidate] += 1
        else:
                        candidate_votes[candidate] = 1

    # Find winner
    for candidate, votes in candidate_votes.items():
        if votes > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = votes

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner['name']} with {winner['votes']} votes")
print("-------------------------")


