import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv('vehicles_us.csv')

# Fill missing values
df['model_year'].fillna(df['model_year'].median(), inplace=True)
df['cylinders'].fillna(df['cylinders'].median(), inplace=True)
df['odometer'].fillna(df['odometer'].median(), inplace=True)
df['paint_color'].fillna('unknown', inplace=True)
df['is_4wd'].fillna(0, inplace=True)

# Remove duplicates
df = df.drop_duplicates()

# Sample data for demonstration purposes
data = {
    'transmission': ['automatic', 'manual', 'other'],
    'price': [20000, 15000, 18000]
}

# Create the transmission dataFrame
avg_price_transmission = pd.DataFrame(data)

# Define a color map
color_map = {'automatic': 'blue', 'manual': 'orange', 'other': 'black'}

# Add Streamlit components
st.header("Car Sales Advertisements Dashboard")

# Histogram for price
fig_price = px.histogram(df, x='price', title='Distribution of Prices')
st.plotly_chart(fig_price)

# Histogram for odometer readings
fig_odometer = px.histogram(df, x='odometer', title='Distribution of Odometer Readings')
st.plotly_chart(fig_odometer)

# Scatter plot for price vs. odometer
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer')
st.plotly_chart(fig_scatter)

# Checkbox to show/hide another plot
if st.checkbox('Show Model Year vs. Price'):
    fig_model_year = px.scatter(df, x='model_year', y='price', title='Model Year vs. Price')
    st.plotly_chart(fig_model_year)

# Bar chart for average price by transmission type
fig_transmission_price = px.bar(
    avg_price_transmission,
    x='transmission',
    y='price',
    title='Average Price by Transmission Type',
    labels={'price': 'Average Price', 'transmission': 'Transmission Type'},
    color='transmission',  # Add color based on transmission type
    color_discrete_map=color_map  # Use the custom color map
)
st.plotly_chart(fig_transmission_price)

