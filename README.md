# 🎬 IMDb Async Scraper

Projeto de web scraping assíncrono com Python, que coleta automaticamente dados de filmes populares e dos melhores avaliados no IMDb, utilizando `asyncio`, `aiohttp`, `BeautifulSoup` e `tqdm`.

## 🚀 Funcionalidades

- 📊 Coleta de duas listas separadas:
  - Filmes mais populares (IMDb Moviemeter)
  - Top 25 melhores filmes avaliados (IMDb Top Chart)
- Para cada filme são extraídos:
  - Título
  - Data de lançamento
  - Avaliação (nota)
  - Sinopse
- Resultados salvos em arquivos `.csv`
- Barra de progresso visual com `tqdm`
- Execução assíncrona com controle de concorrência

## 📁 Arquivos Gerados

- `movies_popular.csv` — Filmes populares em alta
- `movies_top_rated.csv` — Top 25 filmes melhor avaliados da história

## 💻 Tecnologias Utilizadas

- Python 3.7+
- `aiohttp`
- `beautifulsoup4`
- `tqdm`

## 📦 Instalação

```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

```bash
python imdb_scraper_async.py
```

Durante a execução, barras de progresso serão exibidas para cada lista processada.

## ⚠️ Aviso Legal

Este projeto é apenas para fins educacionais. Scraping de sites como IMDb deve respeitar seus termos de uso. Para uso comercial ou em larga escala, utilize APIs oficiais ou licenciadas.

## 👨‍💻 Autor

Mateus Mendonça [linkedin](https://www.linkedin.com/in/devmateusmalves/)