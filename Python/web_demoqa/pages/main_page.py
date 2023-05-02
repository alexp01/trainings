from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import timedelta, date
import time
from pathlib import Path
import os
from selenium.webdriver.common.keys import Keys

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

    # Scenario 1

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

    # will check that button is visible after at least 5 seconds
    def elements_check_button_visible_5_secs(self):
        start = time.time()
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "visibleAfter")))
        final = time.time() - start
        assert final >= 5, f'The button was visible after 5 secods. It took: "{final}'
        logging.info(f'The button was visible after 5 secods. It took: "{final}')

    # will check that button is enabled after at least 5 seconds
    def elements_check_button_enable_5_secs(self):
        start = time.time()
        self.refresh
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.element_to_be_clickable((By.ID, "enableAfter")))
        final = time.time() - start
        assert final >= 5, f'The button was enabled after 5 secods. It took: "{final}'
        logging.info(f'The button was enabled after 5 secods. It took: "{final}')

    # Scenario 2

    # Performing tests on "Auto Complete" option

    # will check the autosugest values based on harcoded argument
    def widgets_verify_auto_complete (self, values):
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "autoCompleteMultipleInput")))
        element.send_keys("a")
        suggestions = WebDriverWait(self._Main_page__browser, self._Main_page__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".auto-complete__option")))
        for index, suggestion in enumerate(suggestions):
            assert suggestion.text == values[index], f'The found suggestion is not the expected one. Expecting: "{values[index]}", Found : "{suggestion.text}"'

    # Performing tests on "Date Picker" option

    # will select a date by adding it as a text
    def widgets_insert_text_date (self, text_date):
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "datePickerMonthYearInput")))
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text_date)

    # will pick a date from popup
    def widgets_select_date (self, text_date):
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "datePickerMonthYearInput")))
        element.click()

        month, day, year = text_date.split('/')
        year_element = WebDriverWait(self.__browser, self.__timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".react-datepicker__year-select")))
        select_year = Select(year_element)
        select_year.select_by_visible_text(year)

        month_element = WebDriverWait(self._Main_page__browser, self._Main_page__timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".react-datepicker__month-select")))
        select_month = Select(month_element)
        select_month.select_by_value(str(int(month) - 1))

        days_element = WebDriverWait(self._Main_page__browser, self._Main_page__timeout).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".react-datepicker__day")))
        for index, day_element in enumerate(days_element):
            if (day_element.text == (str(int(day)))) and (index > 8):
                day_element.click()
                break
        else:
            raise MyException(f'Could not locate the day: "{day}".')

    # will verify the selected date.
    def widgets_verify_date(self, text_date):
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "datePickerMonthYearInput")))
        selected_date = element.get_attribute("value")
        assert element.get_attribute("value") == selected_date, f'The selected date is not the expected one. Expecting: "{text_date}", Found : "{selected_date}"'
        logging.info(f'The selected date is: "{selected_date}')

    # will select a date+time by adding it as a text
    def widgets_insert_text_date_and_time (self, text_date):
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "dateAndTimePickerInput")))
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text_date)

    # will select a date+ time
    def widgets_select_date_and_time(self, text_date_and_time):
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "dateAndTimePickerInput")))
        element.click()
        date_and_time = text_date_and_time.split('/')
        time = date_and_time[-1]

        month, day, year = date_and_time[0:3]
        if int(day) < 1 or int(day) > 31:
            raise MyException('The day must have a value between 1 and 31".')
        if int(month) < 1 or int(month) > 12:
            raise MyException('The month must have a value between 1 and 12".')
        if int(year) < 1950 or int(year) > 2050:
            raise MyException('The year must have a value between 1950 and 2050".')

        #select year
        year_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".react-datepicker__year-read-view--selected-year")))
        year_element.click()
        years_value_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".react-datepicker__year-option")))
        visible_years = []
        for year_element in years_value_element:
            year_value = year_element.text
            if len(year_value) > 4:
                child_element_text = year_element.find_element(By.CSS_SELECTOR, "*").text
                year_value = year_value.replace(child_element_text+'\n', '')
            # the bellow solution is more hardcoded, as the child text character might change.
            '''
            if year_element.text != '':
                if "✓\n" in year_element.text:
                    year_value = year_element.text[-4:]
                else:
                    year_value = year_element.text
            '''
            if year_value:
                visible_years.append(year_value)
        # the below code will scroll the searched year in order for it to be selectable.
        if year in visible_years:
            index = visible_years.index(year)+1
            years_value_element[index].click()
        elif int(year) > int(visible_years[0]):
            diff_years = int(year) - int(visible_years[0])
            for index in range(diff_years):
                years_value_element[0].click()
            year_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".react-datepicker__year-option")))
            if year_element[1].text == year:
                year_element[1].click()
            else:
                raise MyException(f'We did not sufficiently scroll up in order to have in the first line in the year: "{year}".')
        elif int(year) < int(visible_years[-2]):
            diff_years = int(visible_years[-2]) - int(year) - 1
            for index in range(diff_years):
                years_value_element[-1].click()
            year_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".react-datepicker__year-option")))
            if year_element[-2].text == year:
                year_element[-2].click()
        else:
            raise MyException(f'Could not locate the year: "{year}".')

        # select month
        months_list = ["January", "February", "March", "April", "May", "June", "Jully", "August", "September", "October", "November", "December"]
        month_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".react-datepicker__month-read-view--selected-month")))
        month_element.click()
        month_values_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".react-datepicker__month-option")))
        if month_values_element[int(month)-1].text == months_list[int(month)-1]:
            month_values_element[int(month)-1].click()
        else:
            raise MyException(f'Could not locate the month: "{month}".')

        # select day

        # this solution seems simpler, compared to how I selected the day in the previous datepicker element.
        # here we look over 2 times, and not in all 42 elements.
        # but this solution is dependent on a particular string in the class atribute.
        day_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".react-datepicker__day--" + day.zfill(3))))
        for element in day_element:
            if "react-datepicker__day--outside-month" not in element.get_attribute("class"):
                element.click()
                break
        else:
            raise MyException(f'Could not locate the day: "{day}".')

        # select time
        time_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".react-datepicker__time-list-item")))
        for element in time_element:
            if element.text == time:
                element.click()
                break
        else:
            raise MyException(f'Could not locate the time: "{time}".')

    # will verify the selected date and time.
    def widgets_verify_date_and_time(self, text_date_and_time):
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "dateAndTimePickerInput")))
        selected_date = element.get_attribute("value")
        assert element.get_attribute("value") == selected_date, f'The selected date is not the expected one. Expecting: "{text_date_and_time}", Found : "{selected_date}"'
        logging.info(f'The selected date and time is: "{selected_date}"')

    # Performing tests on "Slider" option

    # will click left or right key, until it will reach the correct value
    def widgets_set_slide_value_option1(self, slide_value):
        element = WebDriverWait(self._Main_page__browser, self._Main_page__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".range-slider")))
        current_value = int(element.get_attribute("value"))
        if current_value < slide_value:
            final_index = slide_value - current_value
            for index in range(final_index):
                element.send_keys(Keys.RIGHT)
        else:
            final_index =  current_value - slide_value
            for index in range(final_index):
                element.send_keys(Keys.LEFT)
        changed_value = int(element.get_attribute("value"))
        assert changed_value == slide_value, f'The slide changed value is not correct. Expecting: "{slide_value}", Found : "{changed_value}"'
        logging.info(f'The slider value was set to: "{changed_value}"')

    # will move the slide using ActionChain.
    # this solution is not that precise, especially more near the edges, as probably ActionChain is not that precise.
    # the offset value should probably take into account the pixels also.
    def widgets_set_slide_value_option2(self, slide_value):
        element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".range-slider")))
        #current_value = int(element.get_attribute("value"))
        action = ActionChains(self.__browser)
        scroll_with = int(element.get_attribute("scrollWidth"))
        if slide_value == 50:
            offset = 0
        elif slide_value < 50:
            offset = -(scroll_with / 100) * slide_value
        else:
            offset = (scroll_with / 100) * slide_value

        action.click_and_hold(element).move_by_offset(offset, 0).release().perform()

    # Performing tests on "Progress Bar" option

    # will check that the progress file has finish loading
    @property
    def widgets_verify_progress_bar_finish(self):
        start_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "startStopButton")))
        start_time= time.time()
        progress_bar_element = WebDriverWait(self._Main_page__browser, self._Main_page__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".progress-bar")))
        initial_value = int(progress_bar_element.get_attribute("aria-valuenow"))
        self.__browser.execute_script("arguments[0].scrollIntoView(true);", progress_bar_element)
        assert initial_value == 0, f'The slide initial value is not 0%. Expecting: 0%, Found : "{initial_value}"'
        start_element.click()

        for index in range(20):
            current_value = int(progress_bar_element.get_attribute("aria-valuenow"))
            if current_value == 100:
                break
            time.sleep(1)
        else:
            raise MyException('The progress bar did not finish in the limit timframe of 10  secs.')

        finish_time = time.time() - start_time
        reset_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "resetButton")))
        reset_element.click()
        logging.info(f'The progress bar was loaded to 100% in : "{finish_time}" seconds')

    # will stop the progres bar at a specific value.
    def widgets_stop_progress_bar(self, stop_value):
        start_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "startStopButton")))
        start_element.click()
        progress_bar_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".progress-bar")))
        self.__browser.execute_script("arguments[0].scrollIntoView(true);", progress_bar_element)
        not_reached = True
        while not_reached:
            if stop_value == int(progress_bar_element.get_attribute("aria-valuenow")):
                start_element.click()
                break
        else:
            raise MyException(f'The progress bar value: "{stop_value}" was not found/reached.')
        bar_value = int(progress_bar_element.get_attribute("aria-valuenow"))
        logging.info(f'The progress bar was stopped at : "{bar_value}" %')

    # Performing tests on "Tool tips" option

    # will check that a text will appear when button is hoovered.
    @property
    def check_hover_button(self):
        start_element = WebDriverWait(self.__browser, self.__timeout).until(EC.presence_of_element_located((By.ID, "toolTipButton")))
        action = ActionChains(self.__browser)
        action.move_to_element(start_element).perform()
        tooltip_element = WebDriverWait(self._Main_page__browser, self._Main_page__timeout).until(EC.presence_of_element_located((By.ID, "buttonToolTip")))
        assert tooltip_element.text == 'You hovered over the Button', f'The button tooltip message is correct: "{tooltip_element.text}"'


