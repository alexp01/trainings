from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import timedelta, date
import time
from .common.log import *

class MyException(Exception):
    pass

class Main_page():

    def __init__(self, browser):
        self.__browser = browser

    def open_e_boutique(self, option):
        self.__browser.find_element(By.CSS_SELECTOR, '[id="dropdownButton-1"]').click()

    def open_from_menu(self, menu, option1, option2):
        logging.info(' #Step : Opening the menu option : "Se déplacer" / "Télécharger les horaires".')
        if not (option1 in menu.keys()):
            raise MyException(f'The key "{option1}" does not exist in menu variable.')
        elif not (option2 in menu[option1]):
            raise MyException(f'The submenu key "{option2}" does not exist in menu key "{option1}".')
        parent_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dropdown-menu-bar-module--dropdownMenu--0cef9")))
        found_option1 = 0
        for index, parent in enumerate(parent_element):
            inside_parent = self.__browser.find_element(By.CSS_SELECTOR, f'[id="dropdownButton-{str(index)}"]')
            if inside_parent.text == option1:
                found_option1 = 1
                # Expand menu when proper name is found.
                action = ActionChains(self.__browser)
                action.move_to_element(parent).perform()
                child = self.__browser.find_elements(By.CSS_SELECTOR, f'[id="menu{str(index)}"] .jsMenuFocusable')
                for index_child, sub_child in enumerate(child):
                    if sub_child.text == option2:
                        action.move_to_element(sub_child).perform()
                        sub_child.click()
                        break
                else:
                    raise MyException(f'Could not locate sub menu : "{option2}", from menu : "{option1}".')
                break
        logging.info(' #End of STEP.')
        if not found_option1:
            raise MyException(f'Could not locate menu : "{option1}".')

    def verify_url(self, url):
        logging.info(f' #Step : Verify that the url is "{url}"')
        if not WebDriverWait(self.__browser, 5).until(EC.url_to_be(url)):
            raise MyException(f'The current url :"{self.__browser.current_url}" is not the correct one: "{url}". ')
        logging.info(' #End of STEP.')

    def set_cookies(self, value=False):
        locator = ".tarteaucitronAllow" if value else ".tarteaucitronDeny"
        element = WebDriverWait(self._Main_page__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        self._Main_page__browser.execute_script('arguments[0].click()', element)

