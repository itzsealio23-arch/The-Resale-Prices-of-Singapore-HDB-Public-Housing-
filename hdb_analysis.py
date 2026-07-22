#Importing all packages needed for the project (Data Extraction, Visualizations)
import pandas as pd
import matplotlib.pyplot as plt
#Makes the graphs aligned so it is clean to read
%matplotlib inline

#------------DATA COLLECTION--------------#
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


#------------Exploratory Data Analysis (EDA)--------------#

#Prints the first few lines of the database to have an overview of the dataset
print("\n\nSeeing first five lines in the database:")
print(df.head())

#Seeing the data's description (mean,std deviation, etc)
print("\n\nSeeing the Data Description:")
print(df.describe())
#The month column in the describe command shows NaN for standard deviation because, I converted the month column into Date/Time format during our cleaning phase, which then confuses Pandas, however we only need the min and the max for the month column

# Now that I have finished looking at the basics of analyzing the data its time to move onto the more advanced analyzing

#------------Analysis--------------#
#Data Manipulation: Find average price by town
print("\n\nCalculating average prices by town:")
# Group the towns, calculate the mean resale price, and sort from highest to lowest
avg_price_by_town = df.groupby('town')['resale_price'].mean().sort_values(ascending=False)
    
print("\nTop 5 Most Expensive Towns (Average Price):")
print(avg_price_by_town.head())

#Calculate price per square meter
#This standardizes the price so large houses don't bias our view of a town's value
df['price_per_sqm'] = df['resale_price']/df['floor_area_sqm']
#Now we have created the price per sqm variable

#Calculate overall averages for comparison
avg_total_price = df['resale_price'].mean()
avg_sqm_price = df['price_per_sqm'].mean()
print(f"Overall Average Resale Price: S${avg_total_price:,.2f}")
print(f"Overall Average Price/Sqm: S${avg_sqm_price:,.2f}/sqm\n")

#Grouping by Flat Type: See how pricing scales with room sizes
print("Average Prices by Flat Type:")
avg_price_by_type = df.groupby('flat_type')['resale_price'].mean().sort_values()
for ftype, price in avg_price_by_type.items():
    print(f"{ftype}: S${price:,.2f}")
    
#Filtering Data: I'm gonna isolate 4 room flats (Singapore's most popular type)
#and find which towns have the most expensive 4-room flats.
four_room_df = df[df['flat_type'] == '4 ROOM']
avg_4room_by_town = four_room_df.groupby('town')['resale_price'].mean().sort_values(ascending=False)
print("\n\nTop 5 Towns for 4-Room Flats:")
print(avg_4room_by_town.head())

#Group towns by average overall price and average price per sqm
avg_price_by_town = df.groupby('town')['resale_price'].mean().sort_values(ascending=False)
avg_sqm_by_town = df.groupby('town')['price_per_sqm'].mean().loc[avg_price_by_town.index]
  
  

