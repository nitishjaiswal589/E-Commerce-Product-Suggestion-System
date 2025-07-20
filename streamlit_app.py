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

    # Read the views data
    views_df = pd.read_csv("app/product_views.csv")

    # Increment the view count for the selected product
    views_df.loc[views_df['product_id'] == product_id, 'views'] += 1

    # Save the updated views file
    views_df.to_csv("app/product_views.csv", index=False)


    
    # Get recommendations
    results = recommender.get_recommendations(product_id, top_n)
    
    st.subheader("🔎 Recommended Products:")

    for idx, row in results.iterrows():
        # Create columns for layout
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**{row['name']}**")
            st.markdown(f"🧢 Brand: `{row['brand']}`")
            st.markdown(f"📦 Category: `{row['category']}`")
            st.markdown(f"💬 {row['description']}")

        with col2:
            st.markdown(f"💰 **₹{int(row['price'])}**")
            # Render star rating
            stars = "⭐" * int(row['rating'])
            st.markdown(f"Rating: {stars} ({row['rating']})")

        st.markdown("---")

st.subheader("🔥 Trending Products (Most Viewed)")

# Load updated views
views_df = pd.read_csv("app/product_views.csv")

# Sort by views in descending order and pick top 5
top_trending = views_df.sort_values(by="views", ascending=False).head(5)

# Display each trending product
for idx, row in top_trending.iterrows():
    st.markdown(f"**{row['name']}** — {int(row['views'])} views")


# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Scikit-learn")
