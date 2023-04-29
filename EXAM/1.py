import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('sales_data.csv')

# Group the data by product and compute the average price for each product
product_avg_price = df.groupby('PRODUCT')['PRICE'].mean()

# Plot the data as a line graph
plt.plot(product_avg_price.index, product_avg_price.values)
plt.title('Average Price by Product')
plt.xlabel('Product')
plt.ylabel('Average Price')
plt.xticks(rotation=45) # Rotate the x-axis labels for better visibility
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('sales_data.csv')

# Group the data by product and compute the total units sold for each product
product_units_sold = df.groupby('PRODUCT')['UNITS'].sum()

# Plot the data as a line graph
plt.plot(product_units_sold.index, product_units_sold.values)
plt.title('Total Units Sold by Product')
plt.xlabel('Product')
plt.ylabel('Total Units Sold')
plt.xticks(rotation=45) # Rotate the x-axis labels for better visibility
plt.show()



 import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('sales_data.csv')

# Group the data by product and compute the correlation between price and total sales for each product
product_corr = df.groupby('PRODUCT')['PRICE', 'TOTAL SALES'].corr().iloc[0::2,-1]

print(product_corr)
[9:20 AM, 4/27/2023] Nikhil Singh: import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('sales_data.csv')

# Group the data by product and compute the correlation between units sold and total sales for each product
product_corr = df.groupby('PRODUCT')['UNITS', 'TOTAL SALES'].corr().iloc[0::2,-1]

print(product_corr)



import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('sales_data.csv')

# Convert the 'DATE' column to datetime format and create a new column for the month
df['DATE'] = pd.to_datetime(df['DATE'])
df['MONTH'] = df['DATE'].dt.month

# Group the data by month and compute the total sales for each month
monthly_sales = df.groupby('MONTH')['TOTAL SALES'].sum()

# Find the month with the highest sales
highest_month = monthly_sales.idxmax()

# Filter the data to include only the month with the highest sales
highest_month_data = df[df['MONTH'] == highest_month]

# Group the data by product and compute the total sales for each product in the highest sales month
product_sales = highest_month_data.groupby('PRODUCT')['TOTAL SALES'].sum()

# Group the data by month and compute the total sales for each month
monthly_sales = df.groupby('MONTH')['TOTAL SALES'].sum()

# Find the month with the highest sales
highest_month = monthly_sales.idxmax()

# Filter the data to include only the month with the highest sales
highest_month_data = df[df['MONTH'] == highest_month]

# Group the data by product and compute the total sales for each product in the highest sales month
product_sales = highest_month_data.groupby('PRODUCT')['TOTAL SALES'].sum()

# Find the product that contributed the most to the sales in the highest sales month
top_product = product_sales.idxmax()

print("Total sales made for each month:\n", monthly_sales)
print("\nMonth with the highest sales:", highest_month)
print("\nProduct that contributed the most to the sales in the highest sales month:", top_product)