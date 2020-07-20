
from locators.quotes_page_locators import QuotePageLocators
from parsers.quote import QuoteParser

class QuotePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        locator = QuotePageLocators.QUOTE
        quote_tags = self.browser.find_elements_by_css_selector(locator) # as we use elementS, plural, this will give all matching elements
        return [QuoteParser(e) for e in quote_tags]

