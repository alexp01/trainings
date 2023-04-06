from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver():
    def __init__(self, page):
        self.__page = page

    def start(self, options = None):
        option = webdriver.ChromeOptions()
        if options:
            for option_value in options:
                option.add_argument(option_value)

        chrome = webdriver.Chrome(chrome_options=option, executable_path="C:\webdriver\chromedriver")
        chrome.get(self.__page)
        return chrome
