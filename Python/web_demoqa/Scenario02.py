''' Scope
1. Will open "Widgets" from main menu.
2. Will perform some tests on each option found in "Widgets".
Each option has a specific UI component.
'''

from pages.common.main import Driver
from pages.main_page import Main_page
from conf.conf_file import *
from pages.common.log import *
import time

chromeDriver = Driver(page = "https://demoqa.com/")
options = ["start-maximized"]
browser = chromeDriver.start(options)

logging.info('### Scenario02 ####################################.')

do_mp = Main_page(browser, timeout = 10)

do_mp.open_menu_option(Main_options_mapping[Main_options.Widgets.name])

# Performing tests on "Auto Complete" option
logging.info('Performing tests on "Auto Complete" optiton')
do_mp.click_option(Widgets_options_mapping[Widgets.Auto_complete.name])
do_mp.widgets_verify_auto_complete(values = ["Black", "Magenta", "Aqua"])

# Performing tests on "Date Picker" option
logging.info('Performing tests on "Date Picker" optiton')
do_mp.click_option(Widgets_options_mapping[Widgets.Date_picker.name])
do_mp.widgets_insert_text_date('01/01/2024')
do_mp.widgets_verify_date('01/01/2024')
do_mp.widgets_select_date('05/29/2025')
do_mp.widgets_verify_date('05/29/2025')

do_mp.widgets_insert_text_date_and_time('April 14, 2024 14:51 PM')
do_mp.widgets_select_date_and_time('09/09/2040/15:45')
do_mp.widgets_verify_date_and_time('September 9, 2040 3:45 PM')

# Performing tests on "Slider" option
logging.info('Performing tests on "Slider" optiton')
do_mp.click_option(Widgets_options_mapping[Widgets.Slider.name])
do_mp.widgets_set_slide_value_option1(10)
do_mp.widgets_set_slide_value_option2(20)

# Performing tests on "Progress Bar" option
logging.info('Performing tests on "Progress Bar" optiton')
do_mp.click_option(Widgets_options_mapping[Widgets.Progress_Bar.name])
do_mp.widgets_verify_progress_bar_finish
do_mp.widgets_stop_progress_bar(57)

logging.info('### End of Scenario02.')