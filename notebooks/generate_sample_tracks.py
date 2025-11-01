# notebooks/generate_sample_tracks.py

import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

np.random.seed(42)

artists = [
    "The Weeknd", "Billie Eilish", "Drake", "Taylor Swift", "Ed Sheeran",
    "Ariana Grande", "Post Malone", "Dua Lipa", "Bad Bunny", "Olivia Rodrigo",
    "Harry Styles", "Justin Bieber", "BTS", "Coldplay", "Imagine Dragons",
    "Maroon 5", "Bruno Mars", "Adele", "Sam Smith", "Shawn Mendes"
]

song_templates = [
    "Blinding Lights", "Bad Guy", "Shape of You", "Someone Like You",
    "Levitating", "Peaches", "Stay", "Heat Waves", "As It Was",
    "Anti-Hero", "Flowers", "Calm Down", "Unholy", "Kill Bill"
]

tracks = []

for i in range(100):
    artist = np.random.choice(artists)
    song = f"{np.random.choice(song_templates)} {i}" if i > 13 else np.random.choice(song_templates)
    
    tracks.append({
        'id': f'track_{i:03d}',
        'name': song,
        'artists': artist,
        'danceability': np.random.uniform(0.3, 0.9),
        'energy': np.random.uniform(0.2, 0.95),
        'valence': np.random.uniform(0.1, 0.9),
        'acousticness': np.random.uniform(0.05, 0.8),
        'instrumentalness': np.random.uniform(0, 0.3),
        'speechiness': np.random.uniform(0.03, 0.4),
        'personality_cluster': np.random.randint(0, 7)
    })

df = pd.DataFrame(tracks)
df.to_csv(DATA_DIR / 'tracks_clustered.csv', index=False)

print(f"✅ Gerado {len(df)} músicas de exemplo")
print(df.head())