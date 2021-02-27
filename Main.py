import pandas as pd

#Give file a temporary name
file = "PybankData.csv"


#Save file as a DataFrame
df = pd.read_csv(file)

df
#Check data types for each column
df.dtypes


#Print all data in first column to check if any 
unique_months = df["Date"].unique()
unique_months


#Assuming no data is repeated, the number of months is the length of the first column
total_months = len(df["Date"])


#Sum Second Column
Net_Total = df["Profit/Losses"].sum()
print("Total: $" + str(Net_Total))


#Store column 2 in dummy data frame
#store difference between each row in column 2
difference = df['Profit/Losses'].diff()
df['difference'] = difference
difference

#average the difference 
Average_Change = round(df['difference'].mean(),2)


#maximum 
Max_Value = int(difference.max())
Max_index = difference.idxmax()
MaxDate = df.iloc[Max_index,0]
MaxDate
difference



#minimum difference
Min_Value = int(difference.min())
Min_index = difference.idxmin()
MinDate = df.iloc[Min_index,0]

print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Average Change: $" + str(Average_Change))
print("Greatest Increase in Profits: " + str(MaxDate) + " ($" + str(Max_Value) + ")")
print("Greatest Decrease in Profits: " + str(MinDate) + " ($" + str(Min_Value) + ")")


