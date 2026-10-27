# Vibify — exploração de dados do Spotify

Estudo inicial de um dataset público de faixas do Spotify, com download via KaggleHub e análise exploratória em notebooks.

**Estado:** experimento em andamento. O repositório contém o dataset, um script de extração e notebooks executados parcialmente; não há modelo, aplicação, pipeline automatizado ou testes.

## Conteúdo atual

- `src/extract_dataset.py`: baixa o dataset `maharshipandya/-spotify-tracks-dataset` pelo KaggleHub;
- `data/raw/dataset.csv`: cópia atualmente versionada;
- `notebooks/00_test.ipynb`: teste inicial de leitura;
- `notebooks/01_ead.ipynb`: tipos, nulos, duplicidades, estatísticas, gêneros e seleção inicial de audio features.

## Executar

O `requirements.txt` é um snapshot amplo do ambiente de notebook. Para reproduzir o download:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

Configure as credenciais Kaggle apenas no ambiente:

```dotenv
KAGGLE_USERNAME=seu_usuario
KAGGLE_KEY=sua_chave
```

O script usa um caminho relativo pensado para execução dentro de `src/`:

```bash
cd src
python extract_dataset.py
cd ../notebooks
jupyter lab
```

## Limitações

- o EDA termina logo após selecionar as features de áudio;
- não há pergunta analítica definida nem resultado consolidado;
- o dataset bruto está versionado sem documentação de licença, versão ou checksum;
- o script sobrescreve/copia arquivos sem manifesto de origem;
- o caminho de saída depende do diretório corrente;
- não há testes ou CI;
- o manifesto inclui toda a stack Jupyter e várias bibliotecas não usadas pelo código atual.

Próximo passo recomendado: definir uma pergunta, registrar licença e versão do dataset, enxugar dependências e produzir uma análise reproduzível com conclusões e limites.
