import os
import csv
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
#Open the elections result file and read it.
#with open (file_to_load) as election_data:
    #print the file 
#    print(election_data)

#write data to a file 
file_to_save = os.path.join("analysis" , "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as text_file:
    #text_file.write("Hello World")
    text_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")


#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election.
#comapre the votes of each candiate and output the winner based on the popular votes 

