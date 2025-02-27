import pickle
import streamlit as st

# Load data
df = pickle.load(open('dataFrame.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to get recommendations
def recommend(movie_name):
    if movie_name not in df['title'].values:
        return ["Movie not found!"]
    
    movie_index = df[df['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    return [df.iloc[movie[0]]['title'] for movie in movies]

# Streamlit UI
st.title("Movie Recommendation System")

# Dropdown for movie selection
selected_movie = st.selectbox("Select a movie:", sorted(df['title'].values))

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
