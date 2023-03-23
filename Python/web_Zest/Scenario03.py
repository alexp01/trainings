''' Scope
1. Open from menu "E-boutique"/"Accès E-boutique".
2. Verify that all types of cards from every category are visible with the correct name and price.
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

logging.info('### Scenario03 ####################################.')

do_mp.open_from_menu(menu, "E-boutique", "Accès E-boutique")

do_eb = E_boutique(browser)
do_mp.verify_url(url["Accès E-boutique"][0])

do_eb.verify_category_tickets(ticket_categories, "Création support")
do_eb.verify_category_tickets(ticket_categories, "Duplicata support")
do_eb.verify_category_tickets(ticket_categories, "Tout public")
do_eb.verify_category_tickets(ticket_categories, "Jeune")
do_eb.verify_category_tickets(ticket_categories, "Tarif réduit")
do_eb.verify_category_tickets(ticket_categories, "Ramassage scolaire")

browser.close()

logging.info('### End of Scenario03.')