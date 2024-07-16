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

git add .
git commit -m "Finalize app.py and update requirements.txt"
git push
