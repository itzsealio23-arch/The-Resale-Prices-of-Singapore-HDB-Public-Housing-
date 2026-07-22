Singapore HDB Resale Price Analysis: Finding Value in the Market

**My Passion & Motivation**

As I look toward university and my future career, housing affordability is one of the most frequent topics of debate I hear among young Singaporeans. I am deeply interested in economics and urban planning, and I wanted to stop just reading the news about high housing prices and actually explore the data that influences housing affordability.

I built this project to combine my passion for data science with a real-world issue, with a goal to find out where the true value lies in our housing market.

**The Process of Data Science**

To ensure a rigorous and structured investigation, I built this project using the core 5-step data science lifecycle:

1. Ask a Question

The Problem: With record-breaking million-dollar flats making headlines, first-time homebuyers often feel fear by "affordability anxiety."

The Question: How can a young buyer know if they are overpaying for a flat, and which neighborhoods offer the most space for the lowest price?

2. Data Collection

The Source: I sourced the official Resale Flat Prices dataset provided by the Housing & Development Board (HDB) via the Singapore government's open data portal (Data.gov.sg).

The Scope: The dataset contains over 170,000 real-world transaction records spanning from 2017 to the present day. 

3. Exploration and Cleaning

Data Scrubbing: I used the Pandas library in Python to identify and drop duplicate records. I also converted text-based 'month' columns into proper Datetime formats for accurate time-series tracking.

Standard prices can be misleading due to varying flat sizes. To fix this, I coded a new feature—Price per Square Meter ($/sqm)—to standardize the data and fairly compare different towns.

4. Analysis

Statistical Grouping: By aggregating the data by town and flat type, I uncovered the "Space vs. Location Trade-off." Mature estates command a massive premium for location, but non-mature estates offer significantly more living space for a fraction of the cost.

Machine Learning: I developed a Multiple Linear Regression model using Scikit-Learn. The AI was trained on an 80/20 train/test split to learn the mathematical relationship between a flat's size (floor_area_sqm), its age (lease_commence_date), and its final resale_price.

5. Present Results

Visualizations: I used Matplotlib to generate a dual-chart visualization (saved in this repository) that allows users to instantly compare absolute total costs versus space-efficiency values across all Singaporean towns.

Interactive Application: I packaged my machine learning model into a First-Time Buyer Price Predictor (hdb_price_predictor.py). Users can input their desired flat size and age, and the trained AI will present an estimated fair-market price to help them avoid overpaying.

🚀 How to Run This Project

If you would like to run this code on your own machine, follow these steps:

Clone the repository:

git clone [https://github.com/YOUR-USERNAME/hdb-resale-analysis.git](https://github.com/YOUR-USERNAME/hdb-resale-analysis.git)


Install the required libraries:

pip install pandas scikit-learn matplotlib


Run the Data Analysis Script:

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

**Further Steps in This Project**:

Predictive Modeling: Apply machine learning techniques (e.g., Multiple Linear Regression or Random Forest Regressor using scikit-learn) for forecasting future resale prices of HDB flats considering the past data parameters such as town, floor area, storey height, and remaining lease year.

Created as a personal data science portfolio project.
