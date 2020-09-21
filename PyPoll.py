# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# Assign a variable for a file to load and the path 
#

#add our dependencies.
import csv
import os
#Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save a file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize the total vote counter 
total_votes = 0

#Candidate options
candidate_options = []
#Declare a empty dictionary
candidate_votes = {}
#Winning candidate and winning count tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0
    

#Open the election results and read the file.
with open(file_to_load) as election_data:
#Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Read and print the header row.
    headers = next(file_reader)

    #Print each row in tht CSV file
    for row in file_reader:
        print(row)
        #Add to the total vote count.
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name = row[2]

        #If candidate name does not match an existing candidate...
        if candidate_name not in candidate_options:
            #Add it to a list of candidates.    
            candidate_options.append(candidate_name)
            #Begin counting candidate vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to the candidates count
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate
    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count for a candidate
        votes = candidate_votes[candidate_name]

        #calculate the percentage of voters
        vote_percentage = float(votes)/float(total_votes) *100

        #Determine if the votes are greater than the winning counts
        #Determine winning vote count and candidate
        #Determine if votes is greater than winning count

        print (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-----------------------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------------------------------\n")
    print (winning_candidate_summary)
        
    





    