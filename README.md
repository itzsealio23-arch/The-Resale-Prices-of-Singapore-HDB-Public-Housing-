Singapore HDB Resale Price Analysis

**Project Description & Overview:**

Public housing plays an important role in the real estate market in Singapore, where more than 80% of its inhabitants live in HDB (Housing & Development Board) flats. Buying an HDB resale flat can be one of the biggest financial accomplishments for many Singaporeans. Nonetheless, resale flat prices may vary greatly according to the town where the property is located, type of flat, floor area, and the year when the property was constructed.

This project is an analysis of the resale market of HDB flats in Singapore using data. Utilizing data analysis capabilities in Python, the repository accepts information from transactions at Data.gov.sg to gain insights. The objective of this project is to find out what are the answers to the following questions: What towns have the largest premiums? What influence has the floor area on the price?

I decided to build this project because HDB flats are such a huge part of life in Singapore, and I was genuinely curious why some towns like Bishan are so much more expensive than others. I wanted to use Python to find out. Since I have a idea in the future to move to Singapore, this project helps me and others figure out where to move into.

Link For Data = https://data.gov.sg

**Objectives**

To clean and manipulate large real-world datasets using Python.

To discover which Singaporean towns have the highest and lowest average HDB resale prices.

To visualize these economic trends using data visualization libraries.

Technologies Used

**Python 3**

Pandas: Used for data manipulation, grouping, and calculating averages.

Matplotlib: Used for generating data visualizations and charts.

**Data Source**

The dataset used in this project is the official Resale Flat Prices dataset, provided by the Housing & Development Board (HDB) via Data.gov.sg.

**How to Run This Project**

If you would like to run this code on your own machine, follow these steps:

Clone the repository:

git clone [https://github.com/itzsealio23-arch/The-Resale-Prices-of-Singapore-HDB-Public-Housing-.git](https://github.com/itzsealio23-arch/The-Resale-Prices-of-Singapore-HDB-Public-Housing-.git)


Install the required libraries:

pip install -r requirements.txt


Run the script:

python hdb_analysis.py


**Key Findings**

(Note: I will update this section as I explore the data more!)

Based on my initial analysis, towns like Bishan and Tampines show significantly higher average resale prices compared to others in the dataset. 

1. Overall Price vs. Unit Price($/sqm)
When analyzing housing markets, evaluating absolute prices can be misleading due to varying flat sizes. To conduct a statistical evaluation, this analysis implements feature engineering to calculate the unit price per square meter for every transaction i:
<img width="266" height="56" alt="image" src="https://github.com/user-attachments/assets/84e83f21-43ca-4b2c-a578-00cc8cea24a1" />

By grouping the data by town, I can compare the mean absolute resale price (mu resale) against the mean price per square meter (mu sqm):
<img width="104" height="59" alt="image" src="https://github.com/user-attachments/assets/bbdcefc1-5b57-49f5-a861-78e8b255ee29" />

These results emphasize an important economic difference:

- Estates such as Bishan, Bukit Merah, and Queenstown have the highest ranks regarding absolute price and unit price. This happens due to location, closeness to the CBD and well-developed infrastructure of estates.

- The Size vs. Location Paradox: There are towns which show higher ranks by absolute price while lower in unit price and vice versa. This proves the locations where the buyer pays extra for the size of flat versus those locations where the buyer pays extra just for its location.

2. Room Size Elasticity

By summarizing the mean resale prices for different flat types, we can observe the following sequence of asset price growth according to the room size:

Small-sized flats (1-Room and 2-Room flats) provide high accessibility for entering the housing market.

The sizes of the standard family flat (3-Room, 4-Room, and 5-Room flats) show constant linear growth in price.

The expensive flats (Executive and Multi-Generation flats) are characterized by price leaps. These price changes reflect not only the small number of such flats in the housing market but also their relatively large size.

3. Case Study: 4-Room Flats

Being the most popular form of residential housing in Singapore, the 4-room housing data will provide a good basis to measure the cost of living across regions. From the analysis in the python file, it is evident that the five most expensive towns to buy a 4-room flat surpass the national average and hence are competitive markets.

Further Steps in This Project:

Analysis of Spatial Distance: Incorporate geographic data containing the locations of MRT stations. Through this, one can determine the exact distance of travel on foot from each flat to the closest MRT station.

Predictive Modeling: Apply machine learning techniques (e.g., Multiple Linear Regression or Random Forest Regressor using scikit-learn) for forecasting future resale prices of HDB flats considering the past data parameters such as town, floor area, storey height, and remaining lease year.

Created as a personal data science portfolio project.
