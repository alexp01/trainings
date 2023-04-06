from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import timedelta, date
from selenium.webdriver.common.keys import Keys
import time
from .common.log import *

class MyException(Exception):
    pass

class Telecharger_les_horaires():

    def __init__(self, browser):
        self.__browser = browser

    def select_by_city(self, city):
        logging.info(f'#Step : Select from "Par ville" option : "{city}".')
        element_dropdown = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="municipalitiesInput"]')))
        element_dropdown.click()
        time.sleep(1)
        list_of_dropdown_elements = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[id^= "react-autowhatever-autoSuggestmunicipalitiesInput--item-"]')))
        for index, option_in_list in enumerate(list_of_dropdown_elements):
            if city in option_in_list.text:
                index_to_select = index
                break
        element_to_select = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'[id="react-autowhatever-autoSuggestmunicipalitiesInput--item-{index_to_select}"]')))
        self.__browser.execute_script("arguments[0].scrollIntoView(true);", element_to_select);
        self.__browser.execute_script('arguments[0].click()', element_to_select)

    def select_by_ligne(self, ligne):
        logging.info(f'#Step : Select from "Par ligne" option : "{ligne}".')
        element_dropdown = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="linesInput"]')))
        element_dropdown.click()
        time.sleep(1)
        list_of_dropdown_elements = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[id^= "react-autowhatever-autoSuggestlinesInput--item-"]')))
        for index, option_in_list in enumerate(list_of_dropdown_elements):
            if ligne in option_in_list.text:
                index_to_select = index
                break
        element_to_select = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'[id="react-autowhatever-autoSuggestlinesInput--item-{index_to_select}"]')))
        self.__browser.execute_script("arguments[0].scrollIntoView(true);", element_to_select);
        self.__browser.execute_script('arguments[0].click()', element_to_select)

    def select_by_point(self, point):
        logging.info(f'#Step : Select from "Par point d intérêt" option : "{point}".')
        element_dropdown = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="pointsOfInterestInput"]')))
        element_dropdown.click()
        time.sleep(1)
        list_of_dropdown_elements = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[id^= "react-autowhatever-autoSuggestpointsOfInterestInput--item-"]')))
        for index, option_in_list in enumerate(list_of_dropdown_elements):
            if point in option_in_list.text:
                index_to_select = index
                break
        element_to_select = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'[id="react-autowhatever-autoSuggestpointsOfInterestInput--item-{index_to_select}"]')))
        self.__browser.execute_script("arguments[0].scrollIntoView(true);", element_to_select);
        self.__browser.execute_script('arguments[0].click()', element_to_select)

    def verify_lignes(self, lignes):
        logging.info('#Step : Verifying if all lignes are found in the "Par ligne" dropdown option.')
        element_dropdown = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="linesInput"]')))
        element_dropdown.click()
        time.sleep(1)
        list_of_dropdown_elements = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[id^= "react-autowhatever-autoSuggestlinesInput--item-"]')))
        for index, option_in_list in enumerate(list_of_dropdown_elements):
            option_in_list_text = option_in_list.text
            logging.info(f'Found ligne value : {option_in_list_text}')
            if lignes[index] != option_in_list_text:
                return index

    def verify_cities(self, cities):
        logging.info('#Step : Verifying if all lignes are found in the "Par ville" dropdown option.')
        element_dropdown = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="municipalitiesInput"]')))
        element_dropdown.click()
        time.sleep(1)
        list_of_dropdown_elements = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[id^= "react-autowhatever-autoSuggestmunicipalitiesInput--item-"]')))
        for index, option_in_list in enumerate(list_of_dropdown_elements):
            option_in_list_text = option_in_list.text
            logging.info(f'Found city value : {option_in_list_text}')
            if cities[index] != option_in_list_text:
                return index

    def verify_points(self, points):
        logging.info('#Step : Verifying if all stop points are found in the "Par point d intérêt" dropdown option.')
        element_dropdown = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="pointsOfInterestInput"]')))
        action = ActionChains(self.__browser)
        action.move_to_element(element_dropdown).perform()
        element_dropdown.click()
        time.sleep(1)
        list_of_dropdown_elements = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[id^= "react-autowhatever-autoSuggestpointsOfInterestInput--item-"]')))
        for index, option_in_list in enumerate(list_of_dropdown_elements):
            option_in_list_text = option_in_list.text
            logging.info(f'Found stop point value : {option_in_list_text}')
            if points[index] != option_in_list_text:
                return index

    @property
    def clean_ligne(self):
        logging.info('#Step : Removing the selected ligne".')
        element_dropdown = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="linesInput"]')))
        action = ActionChains(self.__browser)
        action.move_to_element(element_dropdown).perform()
        element_dropdown.send_keys(Keys.CONTROL + "a")
        element_dropdown.send_keys(Keys.BACKSPACE)

    @property
    def clean_city(self):
        logging.info('#Step : Removing the selected ligne".')
        element_dropdown = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="municipalitiesInput"]')))
        action = ActionChains(self.__browser)
        action.move_to_element(element_dropdown).perform()
        element_dropdown.send_keys(Keys.CONTROL + "a")
        element_dropdown.send_keys(Keys.BACKSPACE)

    @property
    def clean_point(self):
        logging.info('#Step : Removing the selected point".')
        element_dropdown = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="pointsOfInterestInput"]')))
        action = ActionChains(self.__browser)
        action.move_to_element(element_dropdown).perform()
        element_dropdown.send_keys(Keys.CONTROL + "a")
        element_dropdown.send_keys(Keys.BACKSPACE)

    @property
    def refuse_cockies(self):
        element_dropdown = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]')))
        element_dropdown.click()

