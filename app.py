import streamlit as st
import pandas as pd
import pickle
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import plotly.graph_objects as go
import numpy as np
from notebooks.config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

st.set_page_config(page_title="Vibify", page_icon="🎵", layout="wide")

@st.cache_resource
def load_model():
    with open('data/model.pkl', 'rb') as f:
        return pickle.load(f)

@st.cache_data
def load_tracks():
    return pd.read_csv('data/tracks_clustered.csv')

model_data = load_model()
df_tracks = load_tracks()

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="user-top-read user-library-read",
        cache_path=".spotify_cache"
    ))

def get_user_features(sp):
    results = sp.current_user_top_tracks(limit=50, time_range='medium_term')
    track_ids = [item['id'] for item in results['items']]
    
    features = sp.audio_features(track_ids)
    
    df_features = pd.DataFrame([{
        'danceability': f['danceability'],
        'energy': f['energy'],
        'valence': f['valence'],
        'acousticness': f['acousticness'],
        'instrumentalness': f['instrumentalness'],
        'speechiness': f['speechiness']
    } for f in features if f])
    
    return df_features.mean()

def classify_user(user_avg):
    user_scaled = model_data['scaler'].transform([user_avg])
    cluster = model_data['kmeans'].predict(user_scaled)[0]
    return cluster

def recommend_tracks(user_cluster, n=10):
    cluster_tracks = df_tracks[df_tracks['personality_cluster'] == user_cluster]
    return cluster_tracks.sample(min(n, len(cluster_tracks)))

# UI
st.title("🎵 Vibify")
st.markdown("### Descubra sua personalidade musical")

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.info("Conecte sua conta Spotify para começar")
    
    if st.button("🎵 Conectar Spotify", type="primary"):
        try:
            sp = get_spotify_client()
            st.session_state.sp = sp
            st.session_state.authenticated = True
            st.rerun()
        except Exception as e:
            st.error(f"Erro: {e}")

else:
    sp = st.session_state.sp
    
    with st.spinner("Analisando suas músicas..."):
        user_avg = get_user_features(sp)
        user_cluster = classify_user(user_avg)
        personality = model_data['personalities'][user_cluster]
    
    # Resultado
    st.success("✨ Análise completa!")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"## {personality['emoji']}")
        st.markdown(f"# {personality['name']}")
        st.markdown(f"_{personality['vibe']}_")
    
    with col2:
        st.markdown("### 🎯 Seu Perfil Musical")
        
        categories = model_data['features']
        values = [user_avg[cat] for cat in categories]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            line_color='#1DB954'
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Recomendações
    st.header("🔮 Músicas Recomendadas")
    
    recommendations = recommend_tracks(user_cluster, 10)
    
    for idx, row in recommendations.iterrows():
        col1, col2, col3 = st.columns([3, 2, 1])
        
        with col1:
            st.markdown(f"**{row['name']}**")
        with col2:
            st.markdown(f"_{row['artists']}_")
        with col3:
            if 'id' in row:
                st.markdown(f"[▶️]({f'https://open.spotify.com/track/{row.id}'})")
    
    if st.button("🔄 Nova análise"):
        st.session_state.authenticated = False
        st.rerun()