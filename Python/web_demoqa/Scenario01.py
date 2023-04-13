''' Scope
1. Will open "Element" from main menu.
2. Will perform some tests on each option found in "Elements".
Each option has a specific UI component.
'''

from pages.common.main import Driver
from pages.main_page import Main_page
from conf.conf_file import *
from pages.common.log import *
import time

chromeDriver = Driver(page = "https://demoqa.com/")
options = ["start-maximized", "--incognito"]
browser = chromeDriver.start(options)

logging.info('### Scenario01 ####################################.')

do_mp = Main_page(browser, timeout = 10)

do_mp.open_menu_option(Main_options_mapping[Main_options.Elements.name])

# Performing tests on "Text Box" option
logging.info('Performing tests on "Text Box" option')
do_mp.click_option(Elements_options_mapping[Elements.Text_box.name])
do_mp.elements_text_box_fill_text(name="Tom Johnes", email = "tom1@gmail.com", current_address = "1 Street NYC", permanent_address = "2 Street NYC")

# Performing tests on "Check box" option
logging.info('Performing tests on "Check box" option')
do_mp.click_option(Elements_options_mapping[Elements.Check_box.name])
do_mp.elements_check_boxes(folder_path = ["Home", "Documents", "Office"], child= "Private" )
do_mp.elements_verify_check_boxes(values = ["private"])
do_mp.elements_check_boxes(folder_path = ["Home", "Documents", "Office"], child= "Private" )
do_mp.elements_check_boxes(folder_path = ["Home", "Documents", "WorkSpace"] )
do_mp.elements_verify_check_boxes(values = ["workspace","react","angular","veu"])
do_mp.elements_check_boxes(folder_path = ["Home", "Documents", "WorkSpace"] )

do_mp.elements_check_boxes(folder_path = ["Home", "Documents", "Office"], child= "Public" )
do_mp.elements_check_boxes(folder_path = ["Home", "Documents", "Office"], child= "General" )
do_mp.elements_check_boxes(folder_path = ["Home", "Documents", "WorkSpace"], child= "Veu" )
do_mp.elements_check_boxes(folder_path = ["Home", "Documents", "Office"], child= "Private" )
do_mp.elements_verify_check_boxes(values = ["veu","public","private","general"])

# Performing tests on "Radio Button" option
logging.info('Performing tests on "Radio Button" option')
do_mp.click_option(Elements_options_mapping[Elements.Radio_button.name])
time.sleep(1)
do_mp.elements_radio_click(radio_name = "Yes")
do_mp.elements_check_enabled_radio(radio_name = "Yes")
do_mp.elements_radio_click(radio_name = "Impressive")
do_mp.elements_check_enabled_radio(radio_name = "Impressive")
do_mp.elements_radio_click(radio_name = "Yes")
do_mp.elements_check_enabled_radio(radio_name = "Yes")
#do_mp.elements_radio_click(radio_name = "No")

assert do_mp.elements_get_radio_availability(radio_name = "Yes") , "The radio button 'Yes' is not activated and it should"
assert not do_mp.elements_get_radio_availability(radio_name = "No") , "The radio button 'No' is activated and it shouldn't"

# Performing tests on "Web Tables" option
logging.info('Performing tests on "Web Tables" option')
do_mp.click_option(Elements_options_mapping[Elements.Web_tables.name])
do_mp.elements_add_line_in_web_table(web_table_values[0])
do_mp.elements_add_line_in_web_table(web_table_values[1])
do_mp.elements_search_in_web_table(web_table_values[0]["email"])
do_mp.elements_validate_line_in_web_table(web_table_values[0])
do_mp.elements_edit_line_in_web_table(user_to_update = web_table_values[1], update_values = web_table_updates[0])

updated_user = web_table_values[1]
for key, value in web_table_updates[0].items():
    if value:
        updated_user[key] = value
do_mp.elements_search_in_web_table(updated_user["email"])
do_mp.elements_validate_line_in_web_table(updated_user)

do_mp.elements_change_visible_rows_web_table(20)

# Performing tests on "Buttons" option
logging.info('Performing tests on "Buttons" option')
do_mp.click_option(Elements_options_mapping[Elements.Buttons.name])
do_mp.elements_verify_buttons

# Performing tests on "Broken Links - Images" option
logging.info('Performing tests on "Broken Links - Images" option')
do_mp.click_option(Elements_options_mapping[Elements.Broken_Links_Images.name])
do_mp.elements_verify_broken_images

# Performing tests on "Upload and Download" option
logging.info('Performing tests on "Upload and Download" option')
do_mp.click_option(Elements_options_mapping[Elements.Upload_and_Download.name])
downloaded_file = do_mp.elements_verify_download
do_mp.elements_verify_upload(downloaded_file)
do_mp.elements_clean_download(downloaded_file)

# Performing tests on "Dynamic Properties" option
logging.info('Performing tests on "Dynamic Properties" option')
do_mp.click_option(Elements_options_mapping[Elements.Dynamic_Properties.name])
do_mp.elements_check_button_visible_5_secs()
do_mp.elements_check_button_enable_5_secs()

logging.info('### End of Scenario01.')


