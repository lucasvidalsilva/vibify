from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

tracks = pd.read_csv(DATA_DIR / "tracks.csv")

print(f"Dataset limpo: {len(tracks):,} dados lidos")

print("\nColunas do tracks:")
print(tracks.columns.to_list())

required_columns = ['id', 'name', 'artists', 'danceability', 'energy', 
                   'valence', 'acousticness', 'instrumentalness', 'speechiness']

verified_columns = [col for col in required_columns if col in tracks.columns]
tracks_clean = tracks[verified_columns].copy()

feature_columns = ['danceability', 'energy', 'valence',
                  'acousticness', 'instrumentalness', 'speechiness']

tracks_clean = tracks_clean.dropna(subset=feature_columns)
tracks_clean = tracks_clean.drop_duplicates(subset=['id'])

tracks_clean.to_csv("data/spotify_tracks_clean.csv", index=False)

print(f"Dataset limpo: {len(tracks_clean):,} dados validos salvos em 'data/spotify_tracks_clean.csv'")