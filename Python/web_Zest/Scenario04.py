''' Scope
1. Open from menu "E-boutique"/"Accès E-boutique".
2. Verify that all category are accessible. (dropdown content can be visible or hidden)
'''

from pages.common.main import Driver
from pages.main_page import Main_page
from pages.e_boutique import E_boutique
from conf.conf_file import *
from pages.common.log import *

class MyException(Exception):
    pass

chromeDriver = Driver(page = "https://www.zestbus.fr/")
options = ["start-maximized"]
browser = chromeDriver.start(options, block_privacy=True)

do_mp = Main_page(browser)

logging.info('### Scenario04 ####################################.')

do_mp.open_from_menu(menu, "E-boutique", "Accès E-boutique")

do_eb = E_boutique(browser)
do_mp.verify_url(url["Accès E-boutique"][0])

do_eb.verify_categories(tickets_categories)

do_eb.verify_category_content_accessibility(tickets_categories)

browser.close()

logging.info('### End of Scenario04.')

