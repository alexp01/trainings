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

class E_boutique():
    def __init__(self, browser):
        self.__browser = browser

    @property
    def click_login(self):
        element_login = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gtm-header-login-link")))
        element_login.click()

    def add_user(self, user):
        element_login = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name = "login"]')))
        element_login.send_keys(user)

    def add_psw(self, psw):
        element_login = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name = "password"]')))
        element_login.send_keys(psw)

    @property
    def click_connect(self):
        element_connect = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gtm-auth-login-button')))
        if not element_connect.is_enabled():
            raise MyException(f'The Login can not be done as the "Connexion" button is not enabled. ')
        else:
            element_connect.click()

    def login(self, user, psw):
        logging.info(f'#Step : Perform a login for user "{user}".')
        self.click_login
        self.add_user(user)
        self.add_psw(psw)
        self.click_connect
        logging.info('#End of login STEP.')

    @property
    def open_account(self):
        element_account = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gtm-header-account-link')))
        if not element_account.is_enabled():
            raise MyException(f'The Login can not be done as the "Connexion" button is not enabled. ')
        else:
            element_account.click()

    @property
    def open_account_menu(self):
        element_account = WebDriverWait(self._E_boutique__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[href="\/account\/"]')))
        if not element_account.is_enabled():
            raise MyException(f'The Account menu button is not enabled. ')
        else:
            element_account.click()

    @property
    def open_bills_menu(self):
        element_account = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[href="\/account\/invoices"]')))
        '[name = "login"]'
        if not element_account.is_enabled():
            raise MyException(f'The Bill menu button is not enabled. ')
        else:
            element_account.click()

    @property
    def open_payment_menu(self):
        self.__browser.refresh()
        element_account = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[href="\/account\/payment-cards"]')))
        if not element_account.is_enabled():
            raise MyException(f'The Payment menu button is not enabled. ')
        else:
            element_account.click()

    @property
    def logout(self):
        element_account = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gtm-account-logout-button')))
        if not element_account.is_enabled():
            raise MyException(f'The Logout can not be done as the button is not enabled. ')
        else:
            element_account.click()

    @property
    def expand_filters(self):
        element_filter = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.mt-6')))
        if element_filter.get_attribute("open"):
            logging.info(f'The Tickets filters are already expanded. No need to click expand.')
        else:
            child_element = element_filter.find_element(By.CSS_SELECTOR, '.mt-6 .cursor-pointer')
            child_element.click()

    @property
    def hide_filters(self):
        element_filter = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.mt-6')))
        if element_filter.get_attribute("open"):
            child_element = element_filter.find_element(By.CSS_SELECTOR, '.mt-6 .cursor-pointer')
            child_element.click()
        else:
            logging.info(f'The Tickets filters are already hidden. No need to click hide.')

    def verify_filters_presence(self, tickets_categories):
        elements_parent = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.ml-2.cursor-pointer')))
        if len(elements_parent) != len(tickets_categories):
            raise MyException(f'The filter checkbox number : "{len(elements_parent)}", is not the expected one: "{len(tickets_categories)}". ')
        for index, element in enumerate(elements_parent):
            if element.text.lower() != tickets_categories[index].lower():
                raise MyException(f'Expecting checkbox text : "{tickets_categories[index].lower()}", but we found "{element.text.lower()}". ')

    def apply_filter(self, filter_value):
        elements_parent = WebDriverWait(self.__browser, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[type="checkbox"]')))
        for element in elements_parent:
            previous_sibling = self.__browser.execute_script("""return arguments[0].nextElementSibling""",element)
            if previous_sibling.text.lower() == filter_value.lower():
                element.click()
                logging.info(f'The filter "{filter_value}", was enabled.')
                break

    def remove_filter(self, filter_value):
        elements_parent = WebDriverWait(self.__browser, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[type="checkbox"]')))
        for element in elements_parent:
            previous_sibling = self.__browser.execute_script("""return arguments[0].nextElementSibling""",element)
            if previous_sibling.text.lower() == filter_value.lower():
                element.click()
                logging.info(f'The filter "{filter_value}", was enabled.')
                break

    # Verify if all category names are available.
    def verify_categories(self, tickets_categories):
        elements_parent = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details .sticky')))
        if len(elements_parent) != len(tickets_categories)-1:
            raise MyException(f'The visible ticket categories number : "{len(elements_parent)}", is not the expected one: "{len(tickets_categories)}". ')
        for index, element in enumerate(elements_parent):
            if element.text.lower() != tickets_categories[index+1].lower():
                raise MyException(f'Expecting ticket category type : "{tickets_categories[index+1].lower()}", but we found "{element.text.lower()}". ')

    # Show the content of a category.
    def expand_category(self, ticket_category):
        elements_category = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details')))
        for element in elements_category:
            child_element = element.find_element(By.CSS_SELECTOR, '.sticky ')
            if child_element.text.lower() == ticket_category.lower():
                if element.get_attribute("open"):
                    logging.info(f'The Category: "{ticket_category}" is already expanded. No need to click expand.')
                else:
                    self.__browser.execute_script("arguments[0].scrollIntoView(true);", element);
                    time.sleep(1)
                    element.click()
                    break

    # Hide the content of a category.
    def hide_category(self, ticket_category):
        elements_category = WebDriverWait(self.__browser, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details')))
        for element in elements_category:
            child_element = element.find_element(By.CSS_SELECTOR, '.sticky ')
            if child_element.text.lower() == ticket_category.lower():
                if not element.get_attribute("open"):
                    logging.info(f'The Category: "{ticket_category}" is already hidden. No need to click hide.')
                else:
                    self.__browser.execute_script("arguments[0].scrollIntoView(true);", element);
                    time.sleep(1)
                    child_element.click()
                    break

    # Checks if the category tickets details is expanded.
    def is_category_expanded(self, ticket_category_value):
        elements_category = WebDriverWait(self.__browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details')))
        for element in elements_category:
            child_element = element.find_element(By.CSS_SELECTOR, '.sticky ')
            if child_element.text.lower() == ticket_category_value.lower():
                if element.get_attribute("open"):
                    return True
                else:
                    return False

    # Checks if the category tickets details is hidden.
    def is_category_hidden(self, ticket_category_value):
        elements_category = WebDriverWait(self.__browser, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details')))
        for element in elements_category:
            child_element = element.find_element(By.CSS_SELECTOR, '.sticky ')
            if child_element.text.lower() == ticket_category_value.lower():
                if not element.get_attribute("open"):
                    return True
                else:
                    return False

    def get_category_element(self, category):
        elements_category = WebDriverWait(self.__browser, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details')))
        for element in elements_category:
            child_element = element.find_element(By.CSS_SELECTOR, '.sticky ')
            if child_element.text.lower() == category.lower():
                return element

    # Checks the ticket name and price for a specific category.
    def verify_category_tickets(self, ticket_category, category_name):
        logging.info(f'#Step : Check the tickets name and price for category : "{category_name}".')
        if self.is_category_expanded(category_name):
            pass
        else:
            self.expand_category(category_name)
        category_parent_element = self.get_category_element(category_name)
        for index, category in enumerate(ticket_category[category_name]):
            category_element = category_parent_element.find_element(By.CSS_SELECTOR, f'[item-index="{index}"]')
            title_element = category_element.find_elements(By.CSS_SELECTOR, '.text-xl')
            name = ticket_category[category_name][index]['name']
            price = ticket_category[category_name][index]['price']
            if name != title_element[0].text:
                raise MyException(f"For category: '{category_name}', we were expecting the ticket type : '{name}', but we found '{title_element[0].text}'. ")
            if price != title_element[1].text:
                raise MyException(f'For category: "{category_name}", we were expecting the price : "{price}", but we found "{title_element[1].text}". ')

    # Checks if all categories can be extended and hidden. With check.
    def verify_category_content_accessibility(self, ticket_category):
        for category in ticket_category:
            self.expand_category(category)
            if self.is_category_hidden(category):
                raise MyException(f'Category: "{category}" should be visible but its hidden". ')
            logging.info(f'The category "{category}" is now extended.')
            self.hide_category(category)
            if self.is_category_expanded(category):
                raise MyException(f'Category: "{category}" should be hidden but its visible". ')
            logging.info(f'The category "{category}" is now hidden.')

    def check_email(self, email):
        elements_category = WebDriverWait(self.__browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="staleemail"]')))
        email_text = elements_category.get_attribute('value')
        if not email_text:
            raise MyException(f'Could not locate the email text. ')
        elif email_text != email:
            raise MyException(f'The displayed email : "{email_text}" is not the expected one : "{email}". ')

    def add_card(self, card):
        months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
        add_new_card_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gtm-new-payment-card-button')))
        add_new_card_element.click()
        popup_visible = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.w-full')))
        if popup_visible:
            self.__browser.switch_to.frame(1)
            card_number_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cardNumber')))
            card_number_element.send_keys(card["name"])

            select_month = Select(self.__browser.find_element(By.CSS_SELECTOR,'.vads-expiry-date-input'))
            select_month.select_by_index(months.index(card["month"])+1)

            select_year = Select(self.__browser.find_element(By.CSS_SELECTOR, '[name="vads_expiry_year"]'))
            select_year.select_by_value(card["year"])

            cvv_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cvvHide')))
            cvv_element.send_keys(card["ccv"])

            validate_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.validationButton')))
            validate_element.click()
            self.__browser.switch_to.default_content()
            my_account_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gtm-header-account-link')))
            self.__browser.execute_script('arguments[0].click()', my_account_element)
        else:
            raise MyException(f'Payment popup took longer than 5 seconds to open". ')

    def check_card_warnings(self, card, card_errors):
        months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre",
                  "Novembre", "Décembre"]
        self.open_payment_menu
        add_new_card_element = WebDriverWait(self.__browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gtm-new-payment-card-button')))
        add_new_card_element.click()
        popup_visible = WebDriverWait(self.__browser, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.w-full')))
        if popup_visible:
            self.__browser.switch_to.frame(1)
            validate_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.validationButton')))

            # Check when no fields are filled.
            validate_element.click()
            error_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.mess_error')))
            error_lignes = error_element.text.splitlines()
            if len(error_lignes) != 3:
                raise MyException(f'We were expecting 3 error lignes and only have : {len(error_lignes)}". ')
            elif (card_errors["no_card"] !=  error_lignes[0]):
                raise MyException(f' We were expecting the error: {card_errors["no_card"]}, but received : {error_lignes[0]}". ')
            elif (card_errors["expiration_fail"] !=  error_lignes[1]):
                raise MyException(f' We were expecting the error: {card_errors["expiration_fail"]}, but received : {error_lignes[1]}". ')
            elif (card_errors["crypto_fail"] !=  error_lignes[2]):
                raise MyException(f' We were expecting the error: {card_errors["crypto_fail"]}, but received : {error_lignes[2]}". ')

            # Check when no expiration and crypto is given
            card_number_element = WebDriverWait(self._E_boutique__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cardNumber')))
            card_number_element.send_keys(card["name"])
            validate_element = WebDriverWait(self._E_boutique__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.validationButton')))
            validate_element.click()
            error_element = WebDriverWait(self._E_boutique__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.mess_error')))
            error_lignes = error_element.text.splitlines()
            if len(error_lignes) != 2:
                raise MyException(f'We were expecting 2 error lignes and only have : {len(error_lignes)}". ')
            elif (card_errors["expiration_fail"] !=  error_lignes[0]):
                raise MyException(f' We were expecting the error: {card_errors["expiration_fail"]}, but received : {error_lignes[0]}". ')
            elif (card_errors["crypto_fail"] !=  error_lignes[1]):
                raise MyException(f' We were expecting the error: {card_errors["crypto_fail"]}, but received : {error_lignes[1]}". ')

            # Check when no card number is given
            card_number_element = WebDriverWait(self._E_boutique__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cardNumber')))
            card_number_element.clear()
            select_month = Select(self.__browser.find_element(By.CSS_SELECTOR,'.vads-expiry-date-input'))
            select_month.select_by_index(months.index(card["month"])+1)
            select_year = Select(self.__browser.find_element(By.CSS_SELECTOR, '[name="vads_expiry_year"]'))
            select_year.select_by_value(card["year"])
            cvv_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cvvHide')))
            cvv_element.send_keys(card["ccv"])
            validate_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.validationButton')))
            validate_element.click()
            error_element = WebDriverWait(self.__browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.mess_error')))
            error_lignes = error_element.text.splitlines()
            if len(error_lignes) != 1:
                raise MyException(f'We were expecting 1 error ligne and have : {len(error_lignes)}". ')
            elif (card_errors["no_card"] !=  error_lignes[0]):
                raise MyException(f' We were expecting the error: {card_errors["no_card"]}, but received : {error_lignes[0]}". ')
            self.__browser.switch_to.default_content()
            my_account_element = WebDriverWait(self.__browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gtm-header-account-link')))
            self.__browser.execute_script('arguments[0].click()', my_account_element)
        else:
            raise MyException(f'Payment popup took longer than 5 seconds to open". ')






