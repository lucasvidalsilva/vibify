import os
import shutil
from pathlib import Path
import kagglehub
from dotenv import load_dotenv

load_dotenv()

os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")

RAW_DIR = Path("../data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

print("baixando dataset...")
path =  kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")

for arquivo in Path(path).glob("*.csv"):
    destino = RAW_DIR / arquivo.name
    shutil.copy2(arquivo, destino)
    print(f"arquivo copiado para {destino}")