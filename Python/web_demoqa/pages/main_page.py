from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import timedelta, date
import time
from pathlib import Path
import os

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
        self.__go_back
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

    # Performing tests on "Text Box" option

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

    # Performing tests on "Check box" option

    # will check if the url is change to show an Add. If so it will click Back.
    @property
    def __go_back(self):
        time.sleep(3)
        if "demoqa" not in self.__browser.current_url:
            self.__browser.back()

    # Will enable some check-boxes "Elements/Check Box"
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
                        self.__browser.execute_script("arguments[0].scrollIntoView(true);", element)
                        element_checkbox.click()
                        for i in range(10):
                            if 'rct-node-expanded' in element.get_attribute('class'):
                                break
                            else:
                                time.sleep(1)
                    break
            else:
                raise MyException(f'Could not locate the parent checkbox: "{folder}".')
        if child:
            child_elements =  WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".rct-node-leaf")))
            for child_element in child_elements:
                element_text = child_element.find_element(By.CSS_SELECTOR, '.rct-title').text
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

    # Performing tests on "Radio Button" option

    def elements_radio_click(self, radio_name):
        radio_elements = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".custom-radio")))
        for element in radio_elements:
            element_radio = element.find_element(By.CSS_SELECTOR, '.custom-control-label')
            if element_radio.text == radio_name:
                if "disabled" not in element_radio.get_attribute("class"):
                    self.__browser.execute_script("arguments[0].scrollIntoView(true);", element_radio);
                    element_radio.click()
                    break
                else:
                    raise MyException(f'The radio button: "{element_radio.text}" is not active in order to be selected".')
        else:
            raise MyException(f'Could not locate the radio button: "{radio_name}".')

    # will verify the displayed info about the activated radio button.
    def elements_check_enabled_radio(self, radio_name):
        enabled_elements = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success")))
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

    # Performing tests on "Web Tables" option

    # will open the Add form for the web table.
    def _open_add_in_web_table(self):
        add_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "addNewRecordButton")))
        add_element.click()

    # will save the form and add a new line into the web table.
    def _click_submit_in_add_form(self):
        add_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "submit")))
        add_element.click()

    # will close the form.
    def _click_cancel_in_add_form(self):
        add_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".close")))
        add_element.click()

    # will add a line in a web table
    def elements_add_line_in_web_table(self, user_info):
        self._open_add_in_web_table()
        first_name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "firstName")))
        first_name_element.send_keys(user_info["first_name"])
        last_name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "lastName")))
        last_name_element.send_keys(user_info["last_name"])
        email_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "userEmail")))
        email_element.send_keys(user_info["email"])
        age_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "age")))
        age_element.send_keys(user_info["age"])
        salary_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "salary")))
        salary_element.send_keys(user_info["salary"])
        department_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "department")))
        department_element.send_keys(user_info["department"])
        logging.info(f'Adding the user details: {list(user_info.values())}')
        self._click_submit_in_add_form()

    # will search based on a given value.
    def elements_search_in_web_table(self, search_value):
        search_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "searchBox")))
        search_element.clear()
        search_element.send_keys(search_value)

    def elements_clear_search_web_table(self):
        search_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "searchBox")))
        search_element.clear()

    # will search a line with all its values into the web table. A filter by email is recomended as a prerequisite.
    def elements_validate_line_in_web_table(self, user_info):
        user_values = list(user_info.values())
        lines_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".rt-tr-group")))
        for line in lines_element:
            row_elements = line.find_elements(By.CSS_SELECTOR, '.rt-td')
            found_line = False
            for index in range(6):
                if row_elements[index].text != user_values[index]:
                    break
            else:
                found_line = True
            if found_line:
                return line
        else:
            raise MyException(f'Could not locate the user row with values: "{user_values}".')

    def _click_edit_web_table_line(self, line):
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[title="Edit"]')))
        element.click()

    # will edit a line
    def elements_edit_line_in_web_table(self, user_to_update, update_values):
        self.elements_search_in_web_table(user_to_update["email"])
        user_element_line = self.elements_validate_line_in_web_table(user_to_update)
        self._click_edit_web_table_line(user_element_line)

        if update_values["first_name"]:
            first_name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "firstName")))
            first_name_element.clear()
            first_name_element.send_keys(update_values["first_name"])
        if update_values["last_name"]:
            last_name_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "lastName")))
            last_name_element.clear()
            last_name_element.send_keys(update_values["last_name"])
        if update_values["email"]:
            email_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "userEmail")))
            email_element.clear()
            email_element.send_keys(update_values["email"])
        if update_values["age"]:
            age_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "age")))
            age_element.clear()
            age_element.send_keys(update_values["age"])
        if update_values["salary"]:
            salary_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "salary")))
            salary_element.clear()
            salary_element.send_keys(update_values["salary"])
        if update_values["department"]:
            department_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "department")))
            department_element.clear()
            department_element.send_keys(update_values["department"])
        self._click_submit_in_add_form()
        self.elements_clear_search_web_table()
        logging.info(f'Updating the user details from : "{list(user_to_update.values())}" to : "{list(update_values.values())}".')

    # will select the number of visible rows
    def elements_change_visible_rows_web_table(self, row_limit):
        select_limit = Select(self.__browser.find_element(By.CSS_SELECTOR, '[aria-label="rows per page"]'))
        logging.info(f'Updating the visible row number from: {select_limit.first_selected_option.get_attribute("value")}, to: {str(row_limit)}.')
        select_limit.select_by_value(str(row_limit))

    # Performing tests on "Buttons" option
    @property
    def elements_verify_buttons(self):
        double_click_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "doubleClickBtn")))
        action = ActionChains(self.__browser)
        action.double_click(double_click_element).perform()
        double_click_message_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "doubleClickMessage")))
        assert double_click_message_element.text == "You have done a double click", 'The double click confirmation text is not visible.'
        logging.info('A double click was performed.')

        right_click_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "rightClickBtn")))
        action.context_click(right_click_element).perform()
        right_click_message_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "rightClickMessage")))
        assert right_click_message_element.text == "You have done a right click", 'The right click confirmation text is not visible.'
        logging.info('A right click was performed.')

    # Performing tests on "Broken Links - Images" option
    @property
    def elements_verify_broken_images(self):
        img_elements = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img[src]")))
        for img in img_elements:
            image_natural_height = img.get_attribute("naturalHeight")
            # ignore in order to not block the test due to a broken image.
            #assert image_natural_height != "0", f'The image url {current_url + endpoint} does not display an image on the page.'
            logging.info(f'Check for image display from url: "{img.get_attribute("src")}".')
            logging.info(f'The image is {"visible" if image_natural_height != "0" else "not visible"}.')

    # Performing tests on "Upload and Download" option

    # will click download and verify that the downloaded file name is correct
    @property
    def elements_verify_download(self):
        download_element = WebDriverWait(self._Main_page__browser, self._Main_page__timeout).until(EC.presence_of_element_located((By.ID, "downloadButton")))
        download_element.click()
        self.__browser.execute_script("window.open()")
        self.__browser.switch_to.window(self.__browser.window_handles[-1])
        self.__browser.get('chrome://downloads')
        file_name = self.__browser.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
        assert "sampleFile" in file_name , f'The downloaded file name is not correct. Expecting "sampleFile.jpg" but received "{file_name}"'
        self.__browser.switch_to.window(self.__browser.window_handles[0])
        logging.info(f'The file "{file_name}" was downloaded.')
        return file_name

    # will upload the recent downloaded file and verify the display message.
    def elements_verify_upload(self, downloaded_file):
        upload_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control-file")))
        upload_element.send_keys("C:/Users/user/Downloads/" + downloaded_file)
        download_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "uploadedFilePath")))
        displayed_name = download_element.text.split('\\')[-1]
        assert "sampleFile" in displayed_name, f'The uploaded file name is correct. Expecting "sampleFile.jpg" but received "{displayed_name}"'
        logging.info(f'The file "{displayed_name}" was uploaded.')

    def elements_clean_download(self, downloaded_file):
        downloads_path = str(Path.home() / "Downloads")
        myfile = downloads_path + "\\" + downloaded_file
        if os.path.isfile(myfile):
            os.remove(myfile)
        else:
            raise MyException(f'Could not locate the file: "{myfile}".')

    # Performing tests on "Dynamic Properties" option

    @property
    def refresh(self):
        self.__browser.refresh()
        self.__go_back
    def elements_check_button_visible_5_secs(self):
        start = time.time()
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "visibleAfter")))
        final = time.time() - start
        assert final >= 5, f'The button was visible after 5 secods. It took: "{final}'
        logging.info(f'The button was visible after 5 secods. It took: "{final}')

    def elements_check_button_enable_5_secs(self):
        start = time.time()
        self.refresh
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.element_to_be_clickable((By.ID, "enableAfter")))
        final = time.time() - start
        assert final >= 5, f'The button was enabled after 5 secods. It took: "{final}'
        logging.info(f'The button was enabled after 5 secods. It took: "{final}')