from locators.quotes_locator import QuotesLocators

class QuoteParser:
    """
    will receive a tag for a quote and return tags for elements (content,author and tags) of each quote
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Quote: {self.content} by {self.author}'

    @property
    def content(self):
        locator = QuotesLocators.CONTENT
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def author(self):
        locator = QuotesLocators.AUTHOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tags(self):
        locator = QuotesLocators.TAG
        return self.parent.find_element_by_css_selector(locator)