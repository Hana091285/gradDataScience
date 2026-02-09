"""
In-Class Activity: Exploratory Data Analysis (EDA) with Starbucks Drinks

Dataset: starbucks_drinkMenu_expanded.csv (available in Canvas)
Goal: Understand what the dataset contains, identify patterns, and create a meaningful visualization.
"""

print("*************** Part 1 ***************")


#1. Load the CSV file into a pandas DataFrame
import pandas as pd

df = pd.read_csv('logs/starbucks_drinkMenu_expanded.csv')
"""
2. Print:
- The full DataFrame (⚠️ observe what happens)
"""
print(df)

## The first 5 rows
print(df.head())

## The last 5 rows
print(df.tail())

##3. Display:
#- Column names
print(df.columns)

#- Dataset info (data types + missing values)
df.info()

#- Descriptive statistics
print(df.describe())

""""
💡 Reflection questions:

A) Why is printing the entire DataFrame usually a bad idea?
-----printing the entire DataFrame usually is a bad idea because large datasets produce 
-----too many outputs and hard to read
B) Which columns are numeric? Which are categorical?
-----Numeric columns include values like calories, fat, sugar, protein, and caffeine. 
Categorical columns include drink names, categories, sizes, and preparation types.
C) Do the statistics make sense for food and drinks?
-----Yes, the statistics make sense because food and drink items naturally vary in calories and nutrients 
-----depending on ingredients and portion size.

"""

print("*************** Part 2 ***************")
"""
1. Select and print only these columns:
- Beverage
- Caffeine (mg)
- Sodium (mg)
"""
print(df[["Beverage", "Caffeine (mg)", "Sodium (mg)"]])

print(df.loc[10])
""""
Display:
- One specific row (your choice)
"""
print("\nOne specific row:")
#print(selected_df.iloc[3])
"""
- Two different rows (your choice)
"""
print("\nTwo different rows:")
#print(selected_df.iloc[[1, 5]])
"""
- Those same rows, but only for two columns
"""
print("\nSame rows, only two columns:")
#print(selected_df.loc[[1, 5], ["Beverage", "Caffeine (mg)"]])
"""
💡 Reflection questions:
A) When would you select rows vs columns?
"""
## Rows for specific observations and columns for specific observation


"""    
B) What kind of question would each selection help answer?
"""
## row: ("What are the nutritions values of this drink")



#Column selection → “How does caffeine or sodium vary across drinks?”

print("*************** Part 3 ***************")

"""
1. Create a table showing where missing values exist
2. Count how many missing values each column has

💡 Reflection questions:

A) Which columns have missing values?
B) Would you drop, fill, or ignore them? Why?
"""

print("*************** Part 4 ***************")
"""
1. Filter the dataset to show beverages with:
- Calories below 100
- Improve the filter to show beverages with:
- Calories below 100 AND
- Caffeine below 50 mg

⚠️ Challenge:
Make sure your condition works correctly. If it doesn’t, debug it.

💡 Reflection questions:
A) What kind of customer might this filter represent?
B) Why do we need parentheses in compound conditions?
"""

print("*************** Part 5 ***************")
"""
1. Group the dataset by Beverage_category
2. Compute the average calories per category
3. Print the result

💡 Reflection questions:
A) Which category is the most calorie-dense on average?
B) Why is the mean a reasonable (or not) choice here?
"""

print("*************** Part 6 ***************")

"""
1. Create a new DataFrame containing only numeric nutrition columns
2. Compute the correlation matrix
3. Plot a correlation heatmap using Plotly

💡 Reflection questions:

A) Which nutrients are strongly correlated?
B) Are there any surprising relationships?
C) Why does correlation not imply causation?
"""