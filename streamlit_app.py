import streamlit as st
import pandas as pd
from app.recommender import ContentBasedRecommender

# Load the recommender
recommender = ContentBasedRecommender("app/product_data.csv")

# Page title
st.title("🛍️ Live E-Commerce Product Recommender")

# Load product list
products = pd.read_csv("app/product_data.csv")
product_names = products['name'].tolist()

# Product selection
selected_product = st.selectbox("Select a product:", product_names)

# Number of recommendations
top_n = st.slider("Number of recommendations:", min_value=1, max_value=10, value=3)

# Recommend button
if st.button("Show Recommendations"):
    # Get product_id from selected product name
    product_id = products[products['name'] == selected_product]['product_id'].values[0]
    
    # Get recommendations
    results = recommender.get_recommendations(product_id, top_n)
    
    st.subheader("🔎 Recommended Products:")
    st.table(results)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Scikit-learn")
