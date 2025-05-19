
# 🎬 **IMDb Async Scraper**

Projeto de web scraping assíncrono com Python, que coleta dados de filmes populares e top-rated do IMDb.  
Alta performance, fácil manutenção e extensibilidade, com suporte a Docker.

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  
![Status](https://img.shields.io/badge/Status-Ativo-brightgreen)

---

## 📚 **Funcionalidades**
- 📊 Coleta dados de **filmes populares** e **Top 25 melhores avaliados**.
- 📅 Extração de: Título, Data de Lançamento, Nota e Sinopse.
- ⚙️ Controle de concorrência via `.env`.
- 📂 Resultados exportados em `.csv`.
- 📈 Barra de progresso visual com `tqdm`.
- 🧩 Estrutura modular e suporte a Docker.
- 📝 Logs organizados com `logging`.

---

## 🚀 **Como Executar**

### 1️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

### 2️⃣ Execute o script principal:
```bash
python web_scrapping/main.py
```

### 3️⃣ Configurações no `.env`:
```env
HEADERS_USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64)
CONCURRENT_REQUESTS=10
```

### 🐳 **Executar com Docker:**
```bash
docker build -t imdb_scraper .
docker run imdb_scraper
```

---

## 📁 **Estrutura de Pastas**
```
web_scrapping/
├── __init__.py
├── main.py
├── scraper.py
├── utils.py
├── .env
├── Dockerfile
requirements.txt
README.md
tests/
└── test_scraper.py
```

---

## 🧪 **Testes**
```bash
pytest tests/
```

---

## 📜 **Licença**
Distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

## 👨‍💻 **Autor**

**Mateus Mendonça**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue)](https://www.linkedin.com/in/devmateusmalves/)  
