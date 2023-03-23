from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from datetime import timedelta, date
import time
class MyException(Exception):
    pass

class Main_page():

    def __init__(self, browser):
        self.__browser = browser

    # Close the Cookie popup that will be visible at every page start
    def close_cookie_popup(self):
        element = WebDriverWait(self.__browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bw-cookie-banner__first-button")))
        #time.sleep(1)
        element.click()

    # Expand the Search area
    def expand_search_area(self):
        time.sleep(1)
        # Could not make the explicit wait work here as i had un element and i was searching again inside that element.

        #WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bw-search-widget__open-search-button")))
        #element = self.__browser.find_element(By.CSS_SELECTOR, '.bw-search-widget__open-search-button')
        #child_element = WebDriverWait(self.__browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mat-button-wrapper")))
        #element.find_element(By.CSS_SELECTOR, '.mat-button-wrapper').click()
        #child_element.click()

        #The solution was tu find a better CSS path by using the addons in Chrome
        # Its using the class name of our element, its parent atribute "color" and then another parent, several levels up with the tag "bw-search-widget"
        self.__browser.find_element(By.CSS_SELECTOR, 'bw-search-widget [color] .mat-button-wrapper').click()

    # If return_days is sent with None it will not be selected, if its not send at all, the default value is 1.
    def add_dates(self, start_days, return_days = 1):
        Months_list = ["janvier", "février.", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
        #time.sleep(1)
        start_date_value = date.today() + timedelta(days=start_days)

        element = WebDriverWait(self.__browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mat-end-date")))
        element.click()
        element = WebDriverWait(self.__browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mat-calendar-period-button")))
        element.click()
        self.__browser.find_element(By.CSS_SELECTOR, '[aria-label="' + str(start_date_value.year) + '"]').click() #'[aria-label="2023"]'
        self.__browser.find_element(By.CSS_SELECTOR, '[aria-label="' + str(Months_list[start_date_value.month-1]) + " " + str(start_date_value.year) + '"]').click() #'[aria-label="April 2023"]'
        self.__browser.find_element(By.CSS_SELECTOR, '[aria-label="' + str(start_date_value.day) + " " + str(Months_list[start_date_value.month-1]) + '"]').click() #'[aria-label="4 April"]'

        if return_days:
            end_date_value = date.today() + timedelta(days= start_days + return_days)
            gap_in_months = end_date_value.month - start_date_value.month
            # in case the Return Months is not the Starting Months, we go to the correct Months by clicking next month.
            for i in range(0,gap_in_months):
                self.__browser.find_element(By.CSS_SELECTOR, '.mat-calendar-next-button').click()

            self.__browser.find_element(By.CSS_SELECTOR, '[aria-label="' + str(end_date_value.day) + " " + str(Months_list[end_date_value.month-1]) + '"]').click() #'[aria-label="7 April"]'

    # Will add passengers based on the input dict
    def set_passengers(self, dict_passengers):
        self.__browser.find_element(By.CSS_SELECTOR, '.bw-search-widget__passenger-manager-input').click()
        passengers_added = 0
        for category, number in dict_passengers.items():
            if number > 0:
                for passenger in range(0, number):
                    if passengers_added != 0:
                        # add a new passenger
                        self.__browser.find_element(By.CSS_SELECTOR,'[data-test="bwsfe-passenger-manager__add-passenger"]').click()
                    select = Select(self.__browser.find_elements(By.CSS_SELECTOR, '[data-test="bwsfe-passenger-manager__passenger-type-select"]')[passengers_added])
                    select.select_by_index(list(dict_passengers.keys()).index(category))
                    passengers_added += 1

        total_passengers_selected = int(self.__browser.find_element(By.CSS_SELECTOR, '.bwsfe-passenger-manager__title').text.split("(")[1].split(")")[0])
        assert passengers_added == total_passengers_selected, f'We expect having : {passengers_added} selected but we have : {total_passengers_selected}. The selected number of passengers is not correct.'
        self.__browser.find_element(By.CSS_SELECTOR, '[data-test="bwsfe-passenger-manager__continue"]').click()

    def set_departure(self, departure):
        self._Main_page__browser.find_element(By.CSS_SELECTOR, '[requirederrorlabelkey="search.widget.error.departing_from"] [data-test="bwsfe-widget__station-input"]').send_keys(departure)
        elements = self.__browser.find_elements(By.CSS_SELECTOR, '.bw-search-station-item__station-heading')
        for element in elements:
            if element.text == departure:
                element.click()
                break


    def set_landing(self, landing):
        self.__browser.find_element(By.CSS_SELECTOR,'[requirederrorlabelkey="search.widget.error.arriving_at"] [data-test="bwsfe-widget__station-input"]').send_keys(landing)
        elements = self.__browser.find_elements(By.CSS_SELECTOR, '.bw-search-station-item__station-heading')
        for element in elements:
            if element.text == landing:
                element.click()
                break

    def perform_search(self, family = False):
        #print('eee')
        time.sleep(1)
        self._Main_page__browser.find_element(By.CSS_SELECTOR, '[data-test="bwsfe-widget__search-button"]').click()
        if family:
            self._Main_page__browser.find_element(By.CSS_SELECTOR, '[data-test="bwsfe-family-fare-popup__continue--yes"]').click()
        else:
            self._Main_page__browser.find_element(By.CSS_SELECTOR,'[data-test="bwsfe-family-fare-popup__continue--no"]').click()

