
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477876#questions

import re
from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
            <p class="price_color">£51.77</p>
            <p class="instock availability">
                <i class="icon-ok"></i>
                    In stock
            </p>
            <form>
                <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
             </form>
            </div>
    </article>
</li>
</body></html>
'''

# <i> is for icon
# <div> is just a container of something
# <a> a url

simple_soup = BeautifulSoup(ITEM_HTML, 'html.parser')

def find_book_title():
    selector = 'article.product_pod h3 a' # This is a CSS selector. You give the path of a tag, by starting from its parents. article.product_pod means a tag called article with a class = product_pod
    finder = simple_soup.select_one(selector)
    #return finder.attrs['title']
    return finder.attrs.get('title') # we access the atribute of that tag, called title

def find_book_url():
    selector = 'article.product_pod h3 a'
    finder = simple_soup.select_one(selector).attrs.get('href')
    return finder

def extract_book_price():
    selector = 'article.product_pod p.price_color'
    finder = simple_soup.select_one(selector).string
    expression = '£([0-9\.]+)'
    matches = re.search(expression, finder)
    return float(matches[1])

def find_product_rating():
    selector = 'article.product_pod p.star-rating' # we could locate the p tag with both classes like : p.star-rating.Three. But if the start rating value will be changes, we can not find the class anymore
    finder = simple_soup.select_one(selector).attrs['class'] # this will give : ['star-rating', 'Three']
    return [e for e in finder if e != 'star-rating']
    #value = filter(lambda x: x != 'star-rating', finder) # this is the trainer solution to fetch only the second class name from that p tag
    #return value

print(find_book_title())
print((find_book_url()))
print(extract_book_price())
print(find_product_rating()[0])