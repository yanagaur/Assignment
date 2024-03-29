# -*- coding: utf-8 -*-
"""assignment15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sz7WbjBKP33S3dPCYuIpSS04EEGEJxKI
"""

import pandas as pd

course_name = ["Data Science", "Machine Learning", "Big Data", "Data Engineer"]
duration = [2,3,6,4]
df = pd.DataFrame(data = {"course_name" : course_name, "duration" : duration})

df.iloc[2]

"""Loc and iloc are two functions in Pandas that are used to slice a data set in a Pandas DataFrame. The function .loc is typically used for label indexing and can access multiple columns, while .iloc is used for integer indexing.   """

new_df=df.reindex([3,0,1,2])

new_df.loc[2]

new_df.iloc[2]

"""The function .loc is typically returning for label indexing and can access multiple columns, while .iloc is returning for integer indexing."""

import pandas as pd
import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]
#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)
df1

df1.mean()

df1.iloc[2].mean()

df1['column_2'].iloc[2]="yana"
df1['column_2'].iloc[2]
df1['column_2'].mean()

"""this is giving an error because the mean can be found out out of numbers and not a string

Windows function in Pandas can be broadly divided into three categories namely- Aggregate, Ranking, and Value.

The Aggregate category of window functions can be of three types namely-

Group,
Rolling, and
Expanding.
The Ranking category of window functions can be of five types namely-

Row Numbers,
Row numbers if of two types:
reset_index()
cumcount()
Rank,
Rank is of four types:
default_rank
min_rank
NA_bottom
descending
Dense rank,
Percent, and
N-Tile / qcut().
The Value category of window functions can be of two types namely-

Lag / Lead, and
First / Last/nth.
"""

print(pd.datetime.now())

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(str(delta))

import pandas as pd

# Prompt the user for inputs
file_path = input("Enter the file path of the CSV file: ")
column_name = input("Enter the name of the column to convert: ")
category_order = input("Enter the category order (comma-separated values): ")

# Read the CSV file
data = pd.read_csv(file_path)

# Convert the specified column to categorical data type
data[column_name] = pd.Categorical(data[column_name], categories=category_order.split(','), ordered=True)

# Display the sorted data
sorted_data = data.sort_values(by=column_name)
print(sorted_data)

import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({
    'Product Category': ['Category A', 'Category B', 'Category C'],
    'Sales': [1500, 2500, 1800],
    'Year': [2019, 2019, 2019]
})

# Group the data by product category and sum the sales over time
category_sales = data.groupby('Product Category')['Sales'].sum()

# Create a stacked bar chart
category_sales.plot(kind='bar', stacked=True)

# Set labels and title
plt.xlabel('Product Category')
plt.ylabel('Sales')
plt.title('Sales by Product Category')

# Display the chart
plt.show()

import pandas as pd
from tabulate import tabulate

# Prompt the user for the file path
file_path = input("Enter the file path of the CSV file containing the student data: ")

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv(file_path)

# Calculate the mean, median, and mode of the test scores
mean_score = data['Test Score'].mean()
median_score = data['Test Score'].median()
mode_scores = data['Test Score'].mode()

# Prepare the data for the table
table_data = [
    ['Mean', mean_score],
    ['Median', median_score],
    ['Mode', ', '.join(map(str, mode_scores))]
]

# Display the results in a table
table_headers = ['Statistic', 'Value']
print(tabulate(table_data, headers=table_headers, tablefmt='pipe'))