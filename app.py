from flask import Flask, request, jsonify
from app.recommender import ContentBasedRecommender

# Initialize Flask app
app = Flask(__name__)

# Initialize the recommender (loads data and computes similarity)
recommender = ContentBasedRecommender("app/product_data.csv")

@app.route("/")
def home():
    return "Welcome to the E-Commerce Product Recommender API!"

@app.route("/recommend", methods=["GET"])
def recommend():
    try:
        # Get product_id from URL query parameter (default to 1)
        product_id = int(request.args.get("product_id", 1))
        top_n = int(request.args.get("top_n", 3))

        # Get recommendations
        recommendations = recommender.get_recommendations(product_id, top_n)

        # Convert DataFrame to JSON and return
        return jsonify(recommendations.to_dict(orient="records"))
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
