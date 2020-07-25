
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9532820#overview
# the same thing as example.py but instead of having several sessions we now just have 1 to call all the 50 pages
# the time it takes to fetch all pages is now 50% faster than example.py

import aiohttp
import asyncio
import time

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

loop = asyncio.get_event_loop()

urls = ['http://google.com' for i in range(50)]
start_time = time.time()
loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'All took {time.time() - start_time}')

# the call and wait for the response to that website takes around 1 sec, and as all 50 request are sent in paralelel, the total response time for the 50 call is a bit over 1 sec.