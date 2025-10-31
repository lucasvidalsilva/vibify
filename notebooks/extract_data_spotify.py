import kagglehub
import shutil
import os

print("Baixando dataset do Kaggle...")
path = kagglehub.dataset_download("lehaknarnauli/spotify-datasets")
print("Dataset baixado em: ", path)

projeto_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(projeto_raiz, 'data')
raw_dir = os.path.join(data_dir, 'raw')

os.makedirs(raw_dir, exist_ok=True)
print("Diretorio de dados brutos criado em: ", raw_dir)

print("Copiando arquivos para o diretorio de dados brutos...")

arquivos = ['tracks.csv', 'artists.csv']

for arquivo in arquivos:
    origem = os.path.join(path, arquivo)
    destino = os.path.join(raw_dir, arquivo)

    if os.path.exists(origem):
        shutil.copy2(origem, destino)
        tam_arq = os.path.getsize(destino) / (1024 * 1024) # Mega bytes
        print(f"Arquivo {arquivo} copiado {tam_arq:.2f} MB")
    else:
        print(f"Arquivo {arquivo} nao encontrado.")