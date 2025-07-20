# 🛍️ Live E-Commerce Product Recommender

A content-based product recommendation system with a Streamlit web front-end.  
Built using pandas, scikit-learn, and Streamlit.

## 🔍 Features

- Recommend similar products using product descriptions
- "Because you viewed..." style recommendations
- View tracking with popularity analytics
- Trend list based on most-viewed products
- Simple, clean UI in Streamlit

## 📦 Tech Stack

- Python
- pandas, scikit-learn
- Streamlit
- (Optional) Flask, LightFM

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/ecommerce-recommender.git
cd ecommerce-recommender

# (Optional) Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
