#Importing all packages needed for the project (Data Extraction, Visualizations)
import pandas as pd
import matplotlib.pyplot as plt
#Makes the graphs aligned so it is clean to read
%matplotlib inline

# 1. Creating a data frame from Singapores biggest database (data.gov.sg)
print("Singapore HDB Resale Price Analysis")
df=pd.read_csv("hdb_prices.csv")

#------------DATA CLEANING--------------#

#Cleaning the Data Sheet to see if there is any missing columns
print(df.isnull().sum())
#Shows the "Data Type" of each column (e.g., if a number is accidentally saved as text)
print(df.info())
#Delete any row that has a missing value
df_clean = df.dropna()
#Fill missing 'resale_price' blanks with the average price
mean_price = df['resale_price'].mean()
df['resale_price'] = df['resale_price'].fillna(mean_price)
#This removes any rows that are exactly identical to another row
df = df.drop_duplicates()
#Convert the 'month' column into real dates so Pandas understands the flow of time
df['month'] = pd.to_datetime(df['month'])
# Save the clean data to a new file (index=False stops it from adding weird row numbers)
df.to_csv('hdb_prices_CLEANED.csv', index=False)


#------------Analyzing Data--------------#

#Prints the first few lines of the database to have an overview of the dataset
print("\n\nSeeing first five lines in the database:")
print(df.head())

#Seeing the data's description (mean,std deviation, etc)
print("\n\nSeeing the Data Description:")
print(df.describe())
#The month column in the describe command shows NaN for standard deviation because, I converted the month column into Date/Time format during our cleaning phase, which then confuses Pandas, however we only need the min and the max for the month column
  
  

