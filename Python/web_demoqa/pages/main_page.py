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

    def __init__(self, browser, timeout = 10):
        self.__browser = browser
        self.__timeout = timeout

    # from main page open option.
    def open_menu_option(self, option):
        elements = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card-body")))
        for element in elements:
            if element.text == option:
                self.__browser.execute_script("arguments[0].scrollIntoView(true);", element);
                element.click()
                break
        else:
            raise MyException(f'Could not locate menu option: "{option}".')

    # will get the menu and option element.
    def __get_menu_element(self, option):
        elements = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".element-group")))
        for element in elements:
            element_title = element.find_element(By.CSS_SELECTOR, '.header-text')
            if element_title.text == option:
                menu_element = element.find_element(By.CSS_SELECTOR, '.group-header')
                element_list = element.find_element(By.CSS_SELECTOR, '.element-list')
                return menu_element, element_list
        else:
            raise MyException(f'Could not locate element for option: "{option}".')

    # will check if the menu list is expanded.
    def __is_expanded(self, element_list):
        element_list = element_list.get_attribute("class")
        if "show" in element_list:
            return True
        else:
            return False

    # hide the list of an option.
    def hide_option_list(self, option):
        logging.info(f'#Hiding the list for option : "{option}".')
        menu_element, element_list  = self.__get_menu_element(option)
        self.__browser.execute_script("arguments[0].scrollIntoView(true);", menu_element);
        if self.__is_expanded(element_list):
            menu_element.click()
        else:
            logging.info('#No need to hide as the option list is not visible.')

    # expand the list of an option.
    def expand_option_list(self, option):
        logging.info(f'#Expanding the list for option : "{option}".')
        menu_element, element_list  = self.__get_menu_element(option)
        self.__browser.execute_script("arguments[0].scrollIntoView(true);", menu_element);
        if not self.__is_expanded(element_list):
            menu_element.click()
        else:
            logging.info('#No need to expand as the option list is visible.')

    # will click an option from the expanded list.
    def click_option(self, option):
        list_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".element-list.show")))
        elements = list_element.find_elements(By.CSS_SELECTOR, '.btn.btn-light ')
        for element in elements:
            if option == element.text:
                self.__browser.execute_script("arguments[0].scrollIntoView(true);", element);
                element.click()
                element_class_value = element.get_attribute("class")
                if "active" not in element_class_value:
                    raise MyException(f'The option: "{option}" is not properlly opened. The element does not have the class value : "active".')
                url = self.__browser.current_url
                if element.text.split()[0].lower() not in url.split("/")[-1]:
                   raise MyException(f'The current url: "{url}" does not contain the option text : "{element.text.split()[0].lower()}".')

    # Will fill some text fields in "Elements/Text Box"
    def elements_text_box_fill_text(self, name, email, current_address, permanent_address):
        name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "userName")))
        name_element.send_keys(name)
        user_value = name_element.get_attribute('value')
        assert  user_value == name , f'For username text field we got: "{user_value}" but was expecting "{name}"'
        email_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "userEmail")))
        email_element.send_keys(email)
        email_value = name_element.get_attribute('value')
        assert  email_value == name , f'For username text field we got: "{email_value}" but was expecting "{email}"'
        current_adress_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "currentAddress")))
        current_adress_element.send_keys(current_address)
        current_address_value = name_element.get_attribute('value')
        assert  current_address_value == name , f'For username text field we got: "{current_address_value}" but was expecting "{current_address}"'
        permanent_address_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "permanentAddress")))
        permanent_address_element.send_keys(permanent_address)
        permanent_address_value = name_element.get_attribute('value')
        assert  permanent_address_value == name , f'For username text field we got: "{permanent_address_value}" but was expecting "{permanent_address}"'

    # Will eneble some check-boxes "Elements/Check Box"
    def elements_check_boxes(self, folder_path, child = None):
        last_folder_element = None
        last_folder_name = None
        for folder in folder_path:
            folders_elements = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".rct-node-parent")))
            for element in folders_elements:
                element_text = element.find_element(By.CSS_SELECTOR, '.rct-title').text
                if element_text == folder:
                    last_folder_element = element
                    last_folder_name = element_text
                    if 'rct-node-expanded' not in element.get_attribute('class'):
                        element_checkbox = element.find_element(By.CSS_SELECTOR, '[type="button"]')
                        element_checkbox.click()
                        break
                    else:
                        break
        if child:
            child_elements =  WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".rct-node-leaf")))
            print(f'There are {len(child_elements)} children for parent: {last_folder_name}')
            for child_element in child_elements:
                element_text = child_element.find_element(By.CSS_SELECTOR, '.rct-title').text
                print(element_text)
                if element_text == child:
                    element_checkbox = child_element.find_element(By.CSS_SELECTOR, '.rct-checkbox')
                    element_checkbox.click()
                    logging.info(f'The checkbox child option: "{element_text}" was enabled (or disabled if already enabled).')
                    break
            else:
                path = ('/'.join(folder_path)) + '/' + child
                raise MyException(f'Could not locate the checkbox: "{path}".')
        else:
            element_folder = last_folder_element.find_element(By.CSS_SELECTOR, '.rct-checkbox')
            element_folder.click()
            logging.info(f'The checkbox parent option: "{last_folder_name}" was enabled.')

    # Will verify the selected check boxes in the "You have selected" section
    # there could be another way to check this, with the values for classes of the selected elements.
    def elements_verify_check_boxes(self, values):
        enabled_elements = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".text-success")))
        list_of_values = [element.text.lower() for element in enabled_elements]
        assert set(list_of_values) == set(values), f' Expecting: "{values}" but found: "{list_of_values}"'
        logging.info(f'The fallowing checkboxes are enabled: {",".join(list_of_values)}')

    def elements_radio_click(self, radio_name):
        radio_elements = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".custom-radio")))
        for element in radio_elements:
            element_radio = element.find_element(By.CSS_SELECTOR, '.custom-control-label')
            if element_radio.text == radio_name:
                if "disabled" not in element_radio.get_attribute("class"):
                    element_radio.click()
                    break
                else:
                    raise MyException(f'The radio button: "{element_radio.text}" is not active in order to be selected".')
        else:
            raise MyException(f'Could not locate the radio button: "{radio_name}".')

    # will verify the displayed info about the activated radio button.
    def elements_check_enabled_radio(self, radio_name):
        enabled_elements = WebDriverWait(self._Main_page__browser, self._Main_page__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success")))
        assert enabled_elements.text == radio_name, f'The proper radio button is not enabled. Expecting: "{radio_name}" but found: "{enabled_elements.text}"'

    # will get the status of a radio button, to know if it's clickable or not.
    def elements_get_radio_availability(self, radio_name):
        radio_elements = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".custom-radio")))
        for element in radio_elements:
            element_radio = element.find_element(By.CSS_SELECTOR, '.custom-control-label')
            if element_radio.text == radio_name:
                if "disabled" in element_radio.get_attribute("class"):
                    return False
                else:
                    return True

    def _open_add_in_web_table(self):
        add_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "addNewRecordButton")))
        add_element.click()

    def _click_submit_in_add_form(self):
        add_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "submit")))
        add_element.click()

    def _click_cancel_in_add_form(self):
        add_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".close")))
        add_element.click()

    # will add a line in a web table
    def elements_add_line_in_web_table(self, user_info):
        self._open_add_in_web_table()
        first_name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "firstName")))
        first_name_element.send_keys(user_info["first_name"])
        first_name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "lastName")))
        first_name_element.send_keys(user_info["last_name"])
        first_name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "userEmail")))
        first_name_element.send_keys(user_info["email"])
        first_name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "age")))
        first_name_element.send_keys(user_info["age"])
        first_name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "salary")))
        first_name_element.send_keys(user_info["salary"])
        first_name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "department")))
        first_name_element.send_keys(user_info["department"])
        logging.info(f'Adding the user details: {list(user_info.values())}')
        self._click_submit_in_add_form()


