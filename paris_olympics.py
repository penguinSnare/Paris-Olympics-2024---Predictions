#
# This is a data science project that involves analyzing 
# the 2021 Tokyo Olympics dataset to predict who wins the 2024 paris olympics.

#import libraries
import pandas as pd #to analyze the data

#PHASE 1: FIND DATA SET
#created a scrapper script to load dataset from kaggle
 
#PHASE 2: ANALYSE DATA

#load the actual olympics dataset
df = pd.read_csv('Tokyo 2021 dataset v3.csv')
#tkyo_1 = pandas.read_csv('Tokyo 2021 dataset v4.csv')

# print(df.head(20)) # #prints the first 10 rows
# print(df.shape) # #prints the shape of the spreadsheet
# print(df.columns) # #prints the column names of the spreadsheet
# print(df.describe()) # #Gets the summary statistics for each column

#CLEANING UP THE DATA
#dropping duplicates
df.drop_duplicates(inplace=True)
#tkyo_1.drop_duplicates(inplace=True)
#renaming columns
df.rename(columns={
    "Team/NOC": "Country", 
    "Rank by Total": "Rank", 
    "Total": "Total Medals", 
    "Gold Medal": "Gold", 
    "Silver Medal": "Silver", 
    "Bronze Medal": "Bronze", 
    "NOCCode": "NationCode"}, inplace=True)

#print to verify change worked
#print("Columns after renaming:", df.columns)

#converting data types to floats
#rank
df["Rank"] = df["Rank"].astype(float)
#gold medal
df["Gold"] = df["Gold"].astype(float)
#silver medal
df["Silver"] = df["Silver"].astype(float)
#bronze medal
df["Bronze"] = df["Bronze"].astype(float)
#total
df["Total Medals"] = df["Total Medals"].astype(float)
#rank by total
df["Rank"] = df["Rank"].astype(float)

# ANALYSIS: The countries that won the most medals.
print(" ")
print("Countries that won the most medals🥇🥈🥉")
print(" ")

df_sorted = df.sort_values(by='Total Medals', ascending=False)
# Select the top 10 countries
top_countries = df_sorted[['Country', 'Total Medals']].head(10)
print(top_countries)

#EXPORT RESULTS TO A CSV FILE
top_countries.to_csv("Top_likely_medalEarners_for2024.csv")
