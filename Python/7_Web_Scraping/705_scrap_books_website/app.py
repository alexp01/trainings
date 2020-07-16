from pages.books_page import BookPage
from bs4 import BeautifulSoup
import requests

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477964#questions
# http://books.toscrape.com/

page = requests.get('http://books.toscrape.com/').content
page_content = BookPage(page)

#for page in page_content.books:
#    print(page)

soup = BeautifulSoup(page, 'html.parser')
stock = soup.select_one('div.product_price p.instock').string
print (stock)

