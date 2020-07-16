
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477886#questions
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477888#questions

# The purpose of this is to reuse the same code for multiple articles

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

class Locators():
    # List of all nedded locators inside a narticle
    title = 'article.product_pod h3 a'
    url = 'article.product_pod h3 a'
    price = 'article.product_pod p.price_color'
    rating = 'article.product_pod p.star-rating'

class verify_article():
    def __init__(self, page):
        self.simple_soup = BeautifulSoup(page, 'html.parser')
        self.locator = Locators()

    @property
    def title(self):
        selector = self.locator.title # This is a CSS selector. You give the path of a tag, by starting from its parents. article.product_pod means a tag called article with a class = product_pod
        finder = self.simple_soup.select_one(selector)
        #return finder.attrs['title']
        return finder.attrs.get('title') # we access the atribute of that tag, called title

    @property
    def url(self):
        selector = self.locator.url
        finder = self.simple_soup.select_one(selector).attrs.get('href')
        return finder

    @property
    def price(self):
        selector = self.locator.price
        finder = self.simple_soup.select_one(selector).string
        expression = '£([0-9\.]+)'
        matches = re.search(expression, finder)
        return float(matches[1])

    @property
    def rating(self):
        selector = self.locator.rating # we could locate the p tag with both classes like : p.star-rating.Three. But if the start rating value will be changes, we can not find the class anymore
        finder = self.simple_soup.select_one(selector).attrs['class'] # this will give : ['star-rating', 'Three']
        return [e for e in finder if e != 'star-rating']


# to scan and get all aritcle you could do :
# all_articles = [verify_article[p] for p in simple_soup_selector.find_all('article')]
article = verify_article(ITEM_HTML)
print (article.title)

