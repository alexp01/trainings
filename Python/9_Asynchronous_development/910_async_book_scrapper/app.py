import aiohttp
import asyncio
import async_timeout
import time
import logging

from bs4 import BeautifulSoup
import requests
import time

books = []
MAIN_PAGE = 'http://books.toscrape.com/'

from pages.books_page import BookPage
from locators.books_page_locators import BookPageLocators

loop = asyncio.get_event_loop()

async def fetch_page(session, url):
    page_start = time.time()
    async with session.get(url) as response:
        print(f'Page took {time.time() - page_start}')
        return  response.status

async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


urls = [f"http://books.toscrape.com/catalogue/page-{page_num+1}.html" for page_num in range(1,50)]
start = time.time()


for x in range(1, 50):
    page_content = requests.get(MAIN_PAGE + 'catalogue/page-' + str(x) + '.html').content
    page = BookPage(page_content)
    books_in_1_page = page.books
    for book in books_in_1_page:
        books.append(book)



