# 🎵 VIBIFY

**Descubra sua personalidade Musical**

[![Last Commit](https://img.shields.io/github/last-commit/lucasvidalsilvah/vibify)](https://github.com/lucasvidalsilvah/vibify)
[![Python](https://img.shields.io/badge/python-100%25-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Um sistema inteligente de análise de personalidade musical usando Machine Learning para recomendar músicas baseado no seu perfil único.

---

## 🎯 O Problema

Com mais de **100 milhões de músicas** disponíveis no Spotify, como descobrir aquelas que realmente combinam com você? 

**Vibify resolve isso!**

---

## ✨ Features

- **Machine Learning**: K-Means clustering com 500k+ músicas
- **7 Personalidades Musicais**: Classificação automática do seu perfil
- **Visualização Interativa**: Gráficos radar do seu DNA musical
- **Recomendações Personalizadas**: Músicas que combinam com você
- **Ultra Rápido**: Análise em < 2 segundos
- **Interface Moderna**: UI intuitiva com Streamlit

---

## 🚀 Como Rodar

### 1. Clone o repositório
```bash
git clone https://github.com/lucasvidalsilvah/vibify.git
cd vibify
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute o app
```bash
streamlit run app.py
```

### 4. Acesse no navegador
```
http://localhost:8501
```

---

## 📊 Pipeline de Dados

### 1. **Extração** 📥
```python
# Via Spotify API
500.000+ músicas com 6 features de áudio
```

### 2. **Transformação** 🧹
```python
# Limpeza e normalização
- Remove duplicatas
- StandardScaler (média=0, std=1)
- Remove outliers
```

### 3. **Modelagem** 🤖
```python
# K-Means Clustering
- Testou K=6 até K=10
- Melhor resultado: K=7 (Silhouette=0.267)
- Otimização: 50x mais rápido com MiniBatchKMeans
```

### 4. **Deploy** 🚀
```python
# Streamlit Cloud
- Tempo de resposta < 2s
- Interface interativa
- Recomendações em tempo real
```

---

## 🎭 As 7 Personalidades Musicais

| Personalidade | Emoji | Características |
|---------------|-------|-----------------|
| **Explorador** | ⚡ | Alta energia, busca intensidade |
| **Serenista** | 🍃 | Acústico, contemplativo |
| **Melancólico** | 🌧️ | Profundidade emocional |
| **Poeta** | 🎤 | Valoriza letras e mensagens |
| **Ritualista** | 💃 | Feito para dançar |
| **Sonhador** | ☀️ | Energia positiva e otimismo |
| **Romântico** | 🌙 | Suave, íntimo, envolvente |

---

## 📈 Métricas de Performance

| Métrica | Valor |
|---------|-------|
| **Dataset** | 500.000+ músicas |
| **Silhouette Score** | 0.267 (bom) |
| **Tempo de Treino** | ~5 minutos |
| **Otimização** | 50x mais rápido |
| **Tempo de Resposta** | < 2 segundos |
| **Features** | 6 (audio features) |

---

## 🧪 Tecnologias e Algoritmos

### Machine Learning
- **Algoritmo**: K-Means Clustering (MiniBatchKMeans)
- **Normalização**: StandardScaler
- **Validação**: Silhouette Score
- **Otimização**: Batch processing + sampling estratégico

### Features de Áudio
```python
[
    'danceability',      # 0-1: Quão dançável
    'energy',            # 0-1: Intensidade
    'valence',           # 0-1: Positividade
    'acousticness',      # 0-1: Orgânico vs eletrônico
    'instrumentalness',  # 0-1: Vocal vs instrumental
    'speechiness'        # 0-1: Quantidade de fala
]
```

---

## 📸 Screenshots

### Tela Principal
![Vibify Home](docs/images/home.png)

### Análise de Personalidade
![Personality Analysis](docs/images/analysis.png)

### Recomendações
![Recommendations](docs/images/recommendations.png)

---

## 🎓 Aprendizados

### Ciência de Dados
- ✅ Pipeline completo de dados (ETL)
- ✅ Clustering não-supervisionado
- ✅ Feature engineering
- ✅ Validação de modelos

### Engenharia de Dados
- ✅ Otimização de performance (50x)
- ✅ Processamento em lote
- ✅ Caching inteligente
- ✅ Deploy em produção

### Machine Learning
- ✅ K-Means clustering
- ✅ Normalização de dados
- ✅ Métricas de avaliação
- ✅ Interpretabilidade de modelos

---

## 👨‍💻 Autor

**Lucas Vidal Silva**

### 📬 Contato

[![GitHub](https://img.shields.io/badge/GitHub-lucasvidalsilvah-181717?style=for-the-badge&logo=github)](https://github.com/lucasvidalsilvah)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5569999007817)

<div align="center">

**AOBA**

[⬆ Voltar ao topo](#-vibify)

</div>