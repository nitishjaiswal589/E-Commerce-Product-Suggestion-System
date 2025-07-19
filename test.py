from app.recommender import ContentBasedRecommender

# Load the recommender
recommender = ContentBasedRecommender("app/product_data.csv")

# Get top 3 similar products for product ID 3 (Black Shirt)
recommendations = recommender.get_recommendations(product_id=3)

# Show the results
print("Top similar products to 'Black Shirt':")
print(recommendations)

