import pandas as pd

# Load your product data
df = pd.read_csv("app/product_data.csv")

# Add a new 'views' column initialized to 0
df["views"] = 0

# Save it to a new file
df.to_csv("app/product_views.csv", index=False)

print("✅ product_views.csv created with 0 views for each product.")
# This script initializes a new CSV file with a 'views' column for tracking product views.