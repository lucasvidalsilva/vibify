import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MiniBatchKMeans
from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

feature_colunas = ['danceability', 'energy', 'valence', 
                   'acousticness', 'instrumentalness', 'speechiness']

df = pd.read_csv(DATA_DIR / "spotify_tracks_clean.csv")

X = df[feature_colunas].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Treinando modelo com K=7 (melhor score)...")
kmeans = MiniBatchKMeans(n_clusters=7, random_state=42, batch_size=4096, n_init=10)
df['personality_cluster'] = kmeans.fit_predict(X_scaled)

cluster_profiles = df.groupby('personality_cluster')[feature_colunas].mean()
print("\nPerfis dos clusters:")
print(cluster_profiles.round(2))

# 7 personalidades otimizadas
personalities = {
    0: {'name': 'Explorador', 'emoji': '⚡',
        'vibe': 'Busca sons que te movem — intensidade é tua bússola.'},
    1: {'name': 'Serenista', 'emoji': '🍃',
        'vibe': 'Valoriza o som puro, o silêncio e a leveza do acústico.'},
    2: {'name': 'Melancólico', 'emoji': '🌧️',
        'vibe': 'Sente fundo — a dor também canta dentro de ti.'},
    3: {'name': 'Poeta', 'emoji': '🎤',
        'vibe': 'As letras te definem — a música é tua confissão.'},
    4: {'name': 'Ritualista', 'emoji': '💃',
        'vibe': 'O ritmo te domina — dançar é tua forma de existir.'},
    5: {'name': 'Sonhador', 'emoji': '☀️',
        'vibe': 'Espalha luz por onde passa — tua playlist é puro brilho.'},
    6: {'name': 'Romântico', 'emoji': '🌙',
        'vibe': 'Prefere o som suave, íntimo — música é abrigo e memória.'}
}

model_data = {
    'kmeans': kmeans,
    'scaler': scaler,
    'features': feature_colunas,
    'n_clusters': 7,
    'personalities': personalities,
    'cluster_profiles': cluster_profiles.to_dict()
}

with open(DATA_DIR / 'model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

cols_save = ['id', 'name', 'artists', 'personality_cluster'] + feature_colunas
df[cols_save].to_csv(DATA_DIR / 'tracks_clustered.csv', index=False)

print("\nDistribuição:")
print(df['personality_cluster'].value_counts().sort_index())