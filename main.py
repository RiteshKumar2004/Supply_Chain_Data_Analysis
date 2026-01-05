import pandas as pd
import streamlit as st
from eda import eda

st.title("Supply Chain Data Analysis")

st.header("1. Welcome")
st.write("Welcome to the Supply Chain Data Analysis app! This application allows you to explore and analyze a dataset of products to uncover insights and trends.")

st.header("2. Dataset Overview")
st.write("This dataset includes essential information about various products. Key columns include:")
st.write("- **Product type**: The type of product")
st.write("- **SKU**: Stock Keeping Unit, a unique identifier for the product")
st.write("- **Price**: The price of the product")
st.write("- **Availability**: The availability status of the product")
st.write("- **Number of products sold**: Total units sold")
st.write("- **Revenue generated**: Total revenue from sales")
st.write("- **Customer demographics**: Information about the customer base")
st.write("- **Stock levels**: Current stock levels of the product")
st.write("- **Lead times**: Time taken from order to delivery")
st.write("- **Order quantities**: Typical order quantities")
st.write("- **Shipping times**: Time taken for shipping")
st.write("- **Shipping carriers**: Carriers used for shipping")
st.write("- **Shipping costs**: Costs associated with shipping")
st.write("- **Supplier name**: Name of the supplier")
st.write("- **Location**: Location of the supplier or warehouse")
st.write("- **Manufacturing lead time**: Time taken for manufacturing")
st.write("- **Manufacturing costs**: Costs associated with manufacturing")
st.write("- **Inspection results**: Results from product inspections")
st.write("- **Defect rates**: Rate of defects in the products")
st.write("- **Transportation modes**: Modes of transportation used")
st.write("- **Routes**: Delivery routes used")
st.write("- **Costs**: Various costs associated with logistics and operations")

st.header("3. How to Use This App")
st.write("• Explore the data overview, descriptive statistics, and a variety of visualizations.")
st.write("• Navigate through the sections to understand trends related to pricing, product availability, sales performance, and more.")

st.header("4. Visualizations Explained")
st.write("• **Histogram**: Displays the distribution of product prices, helping you understand the pricing landscape.")
st.write("• **Bar Chart**: Illustrates the number of products sold across different product types, giving insight into sales performance.")
st.write("• **Pie Charts**: Show the distribution of products based on availability and defect rates.")

df = pd.read_csv("supply_chain.csv")
eda(df)