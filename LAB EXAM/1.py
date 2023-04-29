import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('sales_data.csv')

# Convert the 'Date' column to a datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group the data by month and compute the total sales
monthly_sales = df.groupby(pd.Grouper(key='Date', freq='M'))['Total sales'].sum()

# Plot the data using a line graph
plt.plot(monthly_sales)
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()


# Group the data by product and compute the total sales
product_sales = df.groupby('Product')['Total sales'].sum()

# Plot the data using a bar graph
product_sales.plot(kind='bar')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()


# Group the data by product and compute the average price
product_price = df.groupby('Product')['Price'].mean()

# Plot the data using a bar graph
product_price.plot(kind='bar')
plt.title('Average Price by Product')
plt.xlabel('Product')
plt.ylabel('Average Price')
plt.show()


# Group the data by product and compute the total units sold
product_units_sold = df.groupby('Product')['Units sold'].sum()

# Plot the data using a bar graph
product_units_sold.plot(kind='bar')
plt.title('Total Units Sold by Product')
plt.xlabel('Product')
plt.ylabel('Total Units Sold')
plt.show()


# Compute the correlation between price and total sales for each product
product_corr = df.groupby('Product')['Price', 'Total sales'].corr().iloc[0::2,-1]

# Print the correlation coefficients
print(product_corr)


# Compute the correlation between units sold and total sales for each product
product_corr = df.groupby('Product')['Units sold', 'Total sales'].corr().iloc[0::2,-1]

# Print the correlation coefficients
print(product_corr)


# Group the data by month and compute the total sales
monthly_sales = df.groupby(pd.Grouper(key='Date', freq='M'))['Total sales'].sum()

# Find the month with the highest sales
max_month = monthly_sales.idxmax().strftime('%B %Y')
max_sales = monthly_sales.max()

# Group the data by product and month, and compute the total sales
product_monthly_sales = df.groupby(['Product', pd.Grouper(key='Date', freq='M')])['Total sales'].sum()

# Find the product that contributed the most to sales in the month with the highest sales
max_product
