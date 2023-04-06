''' Scope
1. Open from menu "E-boutique"/"Accès E-boutique".
2. Check if filters will be change the available ticket categories.
'''

from pages.common.main import Driver
from pages.main_page import Main_page
from pages.e_boutique import E_boutique
from conf.conf_file import *
from pages.common.log import *
import time

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

do_eb.apply_filter(tickets_categories[4])
do_eb.apply_filter(tickets_categories[2])
time.sleep(1)
visible_categories = do_eb.get_available_categories()
expected_categories = set([tickets_categories[4].lower(),tickets_categories[2].lower()])
assert set(visible_categories) == expected_categories, \
    f'We were expecting {len(expected_categories)} catogories but we can see  : {len(set(visible_categories))}'

do_eb.apply_filter(tickets_categories[5])
time.sleep(1)
visible_categories = do_eb.get_available_categories()
expected_categories = set([tickets_categories[4].lower(), tickets_categories[2].lower(), tickets_categories[5].lower()])
assert set(visible_categories) == expected_categories, \
    f'We were expecting {len(expected_categories)} catogories but we can see  : {len(set(visible_categories))}'

do_eb.remove_filter(tickets_categories[2])
do_eb.apply_filter(tickets_categories[3])
time.sleep(1)
visible_categories = do_eb.get_available_categories()
expected_categories = set([tickets_categories[4].lower(), tickets_categories[3].lower(), tickets_categories[5].lower()])
assert set(visible_categories) == expected_categories, \
    f'We were expecting {len(expected_categories)} catogories but we can see  : {len(set(visible_categories))}'

do_eb.remove_filter(tickets_categories[3])
do_eb.remove_filter(tickets_categories[4])
do_eb.remove_filter(tickets_categories[5])
do_eb.apply_filter(tickets_categories[0])
time.sleep(1)
visible_categories = do_eb.get_available_categories()
expected_categories = set([x.lower() for x in tickets_categories[1:]])
assert set(visible_categories) == expected_categories, \
    f'We were expecting {len(expected_categories)} catogories but we can see  : {len(set(visible_categories))}'


browser.close()

logging.info('### End of Scenario04.')

