import pandas as pd 

file = "PyPollData.csv"
df = pd.read_csv(file)
df

Total_Votes = len(df)
Total_Votes 

Votes_per_Candidate = df['Candidate'].value_counts()
v = Votes_per_Candidate.to_dict()


print("Election Results")
print("-----------------")
print("Total Votes: " + str(Total_Votes))
print("-----------------")

for key,val in v.items():
    print(key,": ",str(round((val/Total_Votes)*100)) + "%","(",val,")")

winner = max(v,key=v.get)
print("-----------------")
print("Winner: " + winner)
print("-----------------")

text_file = open("PyPoll.txt","w")
text_file.write("Election Results\n")
text_file.write("-----------------\n")
text_file.write("Total Votes: " + str(Total_Votes)+"\n")
text_file.write("-----------------\n")   

for key,val in v.items():
    text_file.write((key + ": " + str(round((val/Total_Votes)*100)) + "% " + "(" + str(val) + ")\n"))

text_file.write("-----------------\n")
text_file.write("Winner: " + winner + "\n")
text_file.write("-----------------\n")
