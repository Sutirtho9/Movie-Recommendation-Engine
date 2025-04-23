# 🎬 Movie Recommender System

A simple and elegant web-based movie recommender app built with **Streamlit**, using content-based filtering. The app suggests similar movies based on the one selected by the user and displays movie posters using the TMDB API.

## 📦 Features

- 🔍 Recommends 10 similar movies based on the selected movie.
- 🎨 Clean and responsive UI with movie posters and titles.
- 🔗 Fetches real-time movie posters from **The Movie Database (TMDB)** API.
- 🧠 Uses pre-computed cosine similarity for fast recommendations.

---

## 🧰 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python, TMDB API
- **Machine Learning:** Cosine similarity with TF-IDF or count-based vectors (stored in `similarity.pkl`)
- **Dataset:** TMDB dataset (movie metadata)

---

## 📁 Project Structure
```
📦 movie-recommender
├── movies.pkl # Pickle file containing movie metadata
├── similarity.pkl # Pickle file containing cosine similarity matrix
├── app.py # Streamlit application
├── Data Processing
    ├── tmdb_5000_credits.csv
    ├── tmdb_5000_movies.csv
    └── Movie recommendation system #Jupyter notebook file
└── README.md # This file
```



## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
If requirements.txt is not available, manually install:

```bash
pip install streamlit pandas requests
```
### 3. Run the App
```bash
streamlit run app.py
```

##  TMDB API Key
This project uses TMDB API to fetch movie posters. Make sure to replace the API key in fetch_poster() function with your own if necessary:
```python
url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
```
## 📸 Sample UI

![image](https://github.com/user-attachments/assets/ccfce2c7-fb53-43ed-bcf3-bd819d75fc17)
