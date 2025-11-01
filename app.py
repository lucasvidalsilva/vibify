import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
import numpy as np

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

def simulate_user_taste():
    """Simula gosto do usuário pegando músicas aleatórias"""
    sample = df_tracks.sample(10)
    features = ['danceability', 'energy', 'valence', 'acousticness', 'instrumentalness', 'speechiness']
    return sample[features].mean()

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

if 'analyzed' not in st.session_state:
    st.session_state.analyzed = False

if not st.session_state.analyzed:
    st.info("🎲 Clique abaixo para descobrir sua personalidade musical")
    st.caption("_(Simulando análise com músicas aleatórias para demonstração)_")
    
    if st.button("🎵 Analisar Meu Gosto Musical", type="primary"):
        st.session_state.analyzed = True
        st.rerun()

else:
    with st.spinner("Analisando suas músicas..."):
        user_avg = simulate_user_taste()
        user_cluster = classify_user(user_avg)
        personality = model_data['personalities'][user_cluster]
    
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
    
    st.header("🔮 Músicas Recomendadas Para Você")
    
    recommendations = recommend_tracks(user_cluster, 10)
    
    for idx, row in recommendations.iterrows():
        col1, col2, col3 = st.columns([3, 2, 1])
        
        with col1:
            st.markdown(f"**{row['name']}**")
        with col2:
            st.markdown(f"_{row['artists']}_")
        with col3:
            st.markdown(f"[▶️](https://open.spotify.com/track/{row['id']})")
    
    if st.button("🔄 Nova Análise"):
        st.session_state.analyzed = False
        st.rerun()