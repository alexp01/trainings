import aiohttp
import asyncio
import time

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9532818#overview
# I understoof parts of what was explained, but in 5 secs i forgot everything. Its quite complex, but interesting in how it works and the results it achives

async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            return  response.status

loop = asyncio.get_event_loop()

tasks = [fetch_page('http://google.com') for i in range(50)]
start_time = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'All took {time.time() - start_time}')

# the call and wait for the response to that website takes around 1 sec, and as all 50 request are sent in paralelel, the total response time for the 50 call is a bit over 1 sec.