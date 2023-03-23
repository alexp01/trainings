

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_options = Options()
prefs = {"profile.default_content_setting_values.automatic_downloads": 1,
         "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,
         "credentials_enable_service": False,
         "profile.password_manager_enabled": False}

chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-save-password-bubble')
chrome_options.add_argument('--disable-translate')
#chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')


driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\webdriver\chromedriver')
driver.get("https://google.com")

print("eee")