# Importing Library
import pandas as pd

# Reading data
df = pd.read_csv('Resources/election_data.csv')

# Calulating the total number of votes
votes = df['Ballot ID'].count()

# Calculating the candidates
candidates = df['Candidate'].unique()

# Calculating candidate votes and their percentages
candidate_votes = {}
candidate_percentages = {}
for i in candidates:
    candidate_votes[i] = df[df['Candidate'] == i]['Ballot ID'].count()
    candidate_percentages[i] = (candidate_votes[i] / votes) * 100

# Finding the winner
winner_candidate = max(candidate_votes, key=candidate_votes.get)

# Printing the results
print("Election Results")
print(f"Total Votes: {votes}")
for i in candidates:
    print(f"{i}: {candidate_percentages[i]:.3f}% ({candidate_votes[i]})")
print(f"Winner: {winner_candidate}")
