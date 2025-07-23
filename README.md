# 🛍️ Live E-Commerce Product Recommender

A content-based product recommendation system with a polished Streamlit frontend and click-tracking analytics.
---

Deploy Link :- [Live Product Suggestion Recommender](https://e-commerce-appuct-suggestion-system-nfgnhmoam7vappqhrhfn6mn.streamlit.app/)

## 🔍 Project Overview

This system recommends products based on both product content and user viewing behavior, featuring:

- **Content-based recommendations** — finds similar items using natural-language processing (TF-IDF on product descriptions).
- **Session-aware suggestions** — "Because you viewed..." recommendations adapt based on products you've already seen.
- **Click analytics & trending** — tracks view counts and displays the most-viewed products dynamically.
- **Interactive frontend** — Streamlit UI with product selection, recommendation display, trending list, and reset history.

---

## 🚀 Features

1. **Content-based filtering**  
   Computes similarity between product descriptions and recommends items with similar text.

2. **Session history tracking**  
   Keeps track of products viewed during a session and adjusts recommendations accordingly.

3. **Click/view analytics**  
   Tracks view counts per product and stores them in `product_views.csv`.

4. **Trending products**  
   Displays top 5 most-viewed products to highlight what's popular.

5. **Elegant interface**  
   Streamlit frontend includes features like star-based ratings, product categories, and price tags.

---


## ⚙️ How It Works

1. **Data Initialization**  
   Run `views_initializer.py` to create `product_views.csv`, initializing view counts for all products.

2. **Recommendations Engine** (`app/recommender.py`)  
   - Loads product catalog from CSV  
   - Converts descriptions into TF-IDF vectors  
   - Calculates cosine similarity between products  
   - Offers `get_recommendations(product_id, top_n)` for personalized suggestions

3. **Frontend UI** (`streamlit_app.py`)  
   - Provides a dropdown to select products  
   - Button to fetch recommendations  
   - Updates click count on each view  
   - Displays viewed-product history  
   - Shows recommendations and a trending list in real-time

---
Screenshots
![image alt](https://github.com/nitishjaiswal589/E-Commerce-Product-Suggestion-System/blob/7c7cceeb6cd00af5a86d8ce8904a05781ded8ead/img%20(1).png)

![image alt](https://github.com/nitishjaiswal589/E-Commerce-Product-Suggestion-System/blob/091bdecf24a549cb8b2b5c37b44231042bebd587/img%20(2).png)

![image alt](https://github.com/nitishjaiswal589/E-Commerce-Product-Suggestion-System/blob/139868be7cd802e47d2256b55cc9009523c150f0/img%20(3).png)

![image alt](https://github.com/nitishjaiswal589/E-Commerce-Product-Suggestion-System/blob/1d60f0af52afcb0dcb0f9382c10eecd7d1c08e3f/img%20(4).png)

![image alt](https://github.com/nitishjaiswal589/E-Commerce-Product-Suggestion-System/blob/8d603802b42a2aa1c5bd40872025ac1870ce39a4/img%20(5).png)


## 🏁 Installation & Usage

```bash
# 1. Clone the repo
git clone https://github.com/nitishjaiswal589/ecommerce-recommender.git
cd ecommerce-recommender

# 2. Install dependencies
pip install -r requirements.txt

# 3. Initialize click tracking
python views_initializer.py

# 4. Run the UI
streamlit run streamlit_app.py

