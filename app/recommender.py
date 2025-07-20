import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class ContentBasedRecommender:
    def __init__(self, csv_path):
        # Step 1: Load product catalog from CSV
        self.products = pd.read_csv(csv_path)

        # Step 2: Vectorize product descriptions using TF-IDF
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.products['description'])

        # Step 3: Compute cosine similarity between product vectors
        self.similarity_matrix = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

    def get_recommendations(self, product_id, top_n=3):
        # Step 4: Get index of the selected product
        idx = self.products[self.products['product_id'] == product_id].index[0]

        # Step 5: Compute similarity scores with all products
        sim_scores = list(enumerate(self.similarity_matrix[idx]))

        # Step 6: Sort by similarity score (skip the product itself)
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

        # Step 7: Get the indices of similar products
        product_indices = [i[0] for i in sim_scores]

        # Step 8: Return similar products as a DataFrame
        return self.products.iloc[product_indices][['product_id', 'name', 'brand', 'category', 'price', 'rating', 'description']]

