import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score
from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

feature_colunas = ['danceability', 'energy', 'valence', 
                   'acousticness', 'instrumentalness', 'speechiness']

df = pd.read_csv(DATA_DIR / "spotify_tracks_clean.csv")

if len(df) > 100000:
    df_sample = df.sample(50000, random_state=42)
else:
    df_sample = df.copy()

X = df_sample[feature_colunas].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

best_score = -1
best_k = 8

for k in range(6, 11):
    kmeans = MiniBatchKMeans(n_clusters=k, random_state=42, batch_size=2048, n_init=3)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels, sample_size=5000)
    print(f"K={k}: {score:.3f}")
    
    if score > best_score:
        best_score = score
        best_k = k

X_full = scaler.transform(df[feature_colunas].values)
kmeans_final = MiniBatchKMeans(n_clusters=best_k, random_state=42, batch_size=4096, n_init=5)
df['personality_cluster'] = kmeans_final.fit_predict(X_full)

cluster_profiles = df.groupby('personality_cluster')[feature_colunas].mean()

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
    5: {'name': 'Maestro', 'emoji': '🎻',
        'vibe': 'Ouve a estrutura invisível da música — pensa em notas, não em hits.'},
    6: {'name': 'Sonhador', 'emoji': '☀️',
        'vibe': 'Espalha luz por onde passa — tua playlist é puro brilho.'},
    7: {'name': 'Romântico', 'emoji': '🌙',
        'vibe': 'Prefere o som suave, íntimo — música é abrigo e memória.'},
    8: {'name': 'Rebelde', 'emoji': '🔥',
        'vibe': 'Vive com atitude — o som é tua forma de dizer “eu existo”.'},
    9: {'name': 'Eclético', 'emoji': '🌈',
        'vibe': 'Não se prende a estilos — o mundo é tua playlist.'}
}

personalities = {k: v for k, v in personalities.items() if k < best_k}

model_data = {
    'kmeans': kmeans_final,
    'scaler': scaler,
    'features': feature_colunas,
    'n_clusters': best_k,
    'personalities': personalities,
    'cluster_profiles': cluster_profiles.to_dict()
}

with open(f'{DATA_DIR}/model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

df.to_csv(f'{DATA_DIR}/tracks_resumido.csv', index=False)

