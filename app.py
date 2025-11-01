import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Vibify", page_icon="🎵", layout="wide")

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #1DB954 0%, #191414 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    .contact-card {
        background: linear-gradient(135deg, #1DB95422 0%, #19141422 100%);
        border-left: 4px solid #1DB954;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    .contact-card h3 {
        color: #1DB954;
        margin-bottom: 0.5rem;
    }
    .contact-card a {
        color: #191414;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
    }
    .contact-card a:hover {
        color: #1DB954;
    }
    .cert-badge {
        background: linear-gradient(135deg, #1DB954 0%, #191414 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        margin: 0.3rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
page = st.sidebar.radio(
    "Navegação",
    ["🎵 Vibify", "👨‍💻 Sobre o Autor"]
)

# Página Sobre o Autor
if page == "👨‍💻 Sobre o Autor":
    st.markdown('<h1 class="main-header">Lucas Vidal Silva</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.5rem; color: #666;">Data Engineer</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Intro
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <div style='width: 150px; height: 150px; border-radius: 50%; 
                        background: linear-gradient(135deg, #1DB954 0%, #191414 100%);
                        margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center;
                        font-size: 4rem;'>
                👨‍💻
            </div>
            <h2>Transformando Dados em Valor</h2>
            <p style='color: #666; font-size: 1.1rem;'>
                Especialista em construir pipelines de dados escaláveis e modelos de ML que resolvem problemas reais.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Estatísticas
    st.markdown("## 📊 Vibify em Números")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Músicas Analisadas", "500K+")
    with col2:
        st.metric("Personalidades", "7")
    with col3:
        st.metric("Tempo de Treino", "5min")
    with col4:
        st.metric("Otimização", "50x")
    
    st.markdown("---")
    
    # Certificações
    st.markdown("## 🎓 Certificações")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='contact-card'>
            <h3>🧱 Databricks Certified</h3>
            <p><strong>Data Engineer Associate</strong></p>
            <p style='color: #666; font-size: 0.95rem;'>
                Apache Spark • Delta Lake • ETL Pipelines • Lakehouse Architecture
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='contact-card'>
            <h3>☁️ Google Cloud Certified</h3>
            <p><strong>Professional Data Engineer</strong></p>
            <p style='color: #666; font-size: 0.95rem;'>
                BigQuery • Dataflow • Cloud Storage • Vertex AI
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tech Stack
    st.markdown("## 💻 Tech Stack")
    
    skills = ['Python', 'Pandas', 'Scikit-Learn', 'SQL', 'Spark', 'Airflow', 
              'Docker', 'Git', 'GCP', 'Databricks', 'Streamlit', 'FastAPI']
    
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    for skill in skills:
        st.markdown(f'<span class="cert-badge">{skill}</span>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Contato
    st.markdown("## 📬 Vamos Conversar?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='contact-card'>
            <h3>📱 WhatsApp</h3>
            <a href='https://wa.me/5569999007817' target='_blank'>
                +55 69 99900-7817
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='contact-card'>
            <h3>💻 GitHub</h3>
            <a href='https://github.com/lucasvidalsilvah' target='_blank'>
                @lucasvidalsilvah
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='contact-card'>
            <h3>🎵 Vibify</h3>
            <a href='https://github.com/lucasvidalsilvah/vibify' target='_blank'>
                Ver Projeto
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0; color: #666;'>
        <h3>"Dados não são apenas números, são histórias esperando para serem contadas."</h3>
        <br>
        <p>Disponível para projetos, consultorias e oportunidades de colaboração.</p>
        <br>
        <p style='font-size: 0.9rem;'>Feito com ❤️ usando Streamlit • 2024</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.stop()

# Página Principal (Vibify)
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