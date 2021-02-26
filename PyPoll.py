import pandas as pd 

file = "PyPollData.csv"
df = pd.read_csv(file)
df

Total_Votes = len(df)
Total_Votes 

Votes_per_Candidate = df['Candidate'].value_counts()
Votes_per_Candidate

