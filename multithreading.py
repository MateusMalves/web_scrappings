import asyncio
import aiohttp
import csv
import random
from bs4 import BeautifulSoup
from aiohttp import ClientSession
import time
import os
from tqdm.asyncio import tqdm_asyncio

# Configurações globais
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
}
BASE_URL = 'https://www.imdb.com'
CONCURRENT_REQUESTS = 10

# Delay aleatório para simular comportamento humano
async def delay():
    await asyncio.sleep(random.uniform(0.1, 0.3))

# Requisição HTTP com tratamento de erro
async def fetch_html(session: ClientSession, url: str) -> str:
    await delay()
    try:
        async with session.get(url, headers=HEADERS, timeout=aiohttp.ClientTimeout(total=15)) as response:
            response.raise_for_status()
            return await response.text()
    except Exception as e:
        print(f"[ERRO] Falha ao buscar {url}: {e}")
        return ""

# Extração de detalhes do filme
async def extract_movie_details(session: ClientSession, url: str, writer, counter):
    html = await fetch_html(session, url)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')
    try:
        title_tag = soup.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else 'N/A'

        date_tag = soup.find('a', href=lambda x: x and 'releaseinfo' in x)
        release_date = date_tag.get_text(strip=True) if date_tag else 'N/A'

        rating_tag = soup.find('div', attrs={'data-testid': 'hero-rating-bar__aggregate-rating__score'})
        rating = rating_tag.get_text(strip=True) if rating_tag else 'N/A'

        plot_tag = soup.find('span', attrs={'data-testid': 'plot-xs_to_m'})
        plot = plot_tag.get_text(strip=True) if plot_tag else 'N/A'

        writer.writerow([title, release_date, rating, plot])
        counter['count'] += 1

    except Exception as e:
        print(f"[ERRO] Problema ao processar {url}: {e}")

# Extração dos links dos filmes de uma página de chart
async def extract_movie_links(session: ClientSession, url: str) -> list:
    html = await fetch_html(session, url)
    soup = BeautifulSoup(html, 'html.parser')

    try:
        table = soup.select_one('div[data-testid="chart-layout-main-column"] ul') or soup.find('tbody')
        movie_items = table.find_all('li') if table.name == 'ul' else table.find_all('tr')
        links = [BASE_URL + item.find('a')['href'] for item in movie_items if item.find('a')]
        print(f"[INFO] {len(links)} filmes encontrados em {url}.")
        return links
    except Exception as e:
        print(f"[ERRO] Falha ao extrair links de {url}: {e}")
        return []

# Processamento completo de um conjunto de links
async def process_chart(session: ClientSession, chart_url: str, output_csv: str):
    links = await extract_movie_links(session, chart_url)

    if not links:
        print(f"[AVISO] Nenhum link encontrado em {chart_url}.")
        return

    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)
    counter = {'count': 0}

    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Release Date', 'Rating', 'Plot'])

        async def sem_task(link):
            async with semaphore:
                await extract_movie_details(session, link, writer, counter)

        await tqdm_asyncio.gather(*(sem_task(link) for link in links), desc=f"Processando {output_csv}")

    print(f"[FINALIZADO] Total de filmes salvos em '{output_csv}': {counter['count']}")

# Função principal
async def main():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        await process_chart(
            session,
            chart_url='https://www.imdb.com/chart/moviemeter/',
            output_csv='movies_popular.csv'
        )

        await process_chart(
            session,
            chart_url='https://www.imdb.com/chart/top/',
            output_csv='movies_top_rated.csv'
        )

    total = time.time() - start_time
    print(f"[FINALIZADO GERAL] Tempo total: {total:.2f} segundos")

if __name__ == '__main__':
    asyncio.run(main())
