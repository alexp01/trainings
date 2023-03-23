from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver():
    def __init__(self, page):
        self.__page = page

    def start(self, options = None, block_privacy = False):

        # Block the notification check when page will start.
        if options:
            option = Options()
            for option_value in options:
                option.add_argument(option_value)

        # Pass the argument 1 to allow and 2 to block
        if block_privacy:
            option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        else:
            option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})

        chrome = webdriver.Chrome(chrome_options=option, executable_path="C:\webdriver\chromedriver")
        chrome.get(self.__page)
        return chrome
