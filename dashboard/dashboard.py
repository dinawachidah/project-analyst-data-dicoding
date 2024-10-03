import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the dashboard
st.title("E-Commerce Sales Dashboard")

# Load the dataset
url = "https://raw.githubusercontent.com/dinawachidah/project-analyst-data-dicoding/refs/heads/main/dashboard/all_data.csv"
data = pd.read_csv(url)

# Display the dataset
st.subheader("Data Overview")
st.dataframe(data.head())

# Sales by Product Category
st.subheader("Sales Distribution by Product Category")
# Use the column 'order_id_count' to display the number of sales
category_sales = data[['product_category_name_english', 'order_id_count']].set_index('product_category_name_english').head(10)

# Create a bar plot for product categories
plt.figure(figsize=(10, 6))
sns.barplot(x=category_sales.index, y=category_sales['order_id_count'])
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Product Categories by Sales')
plt.xlabel('Product Category')
plt.ylabel('Number of Sales')

# Show the plot in Streamlit
st.pyplot(plt)

# Revenue by Geographical Region
st.subheader("Total Revenue by Geographical Region")
# Use the column 'total_revenue' to display total revenue by city
geo_revenue = data[['geolocation_city', 'total_revenue']].set_index('geolocation_city').head(10)

# Create a bar plot for geographical revenue
plt.figure(figsize=(10, 6))
sns.barplot(x=geo_revenue.index, y=geo_revenue['total_revenue'])
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Cities by Total Revenue')
plt.xlabel('City')
plt.ylabel('Total Revenue')

# Show the plot in Streamlit
st.pyplot(plt)

# Run the Streamlit app
if __name__ == "__main__":
    st.write("E-commerce Dashboard built using Streamlit.")
