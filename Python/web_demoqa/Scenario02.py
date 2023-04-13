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

logging.info('### Scenario02 ####################################.')

do_mp = Main_page(browser, timeout = 10)

do_mp.open_menu_option(Main_options_mapping[Main_options.Elements.name])