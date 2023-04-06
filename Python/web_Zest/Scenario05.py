''' Scope
1. Open from menu "E-boutique"/"Accès E-boutique".
2. Login.
3. Verify that we cand add a new card to an account.
4. Verify the errors for card form.
'''

from pages.common.main import Driver
from pages.main_page import Main_page
from pages.e_boutique import E_boutique
from conf.conf_file import *
from pages.common.log import *

class MyException(Exception):
    pass

chromeDriver = Driver(page = "https://www.zestbus.fr/" )
options = ["--incognito", "start-maximized"]
browser = chromeDriver.start(options, block_privacy=False)

do_mp = Main_page(browser)

logging.info('### Scenario05 ####################################.')

do_mp.open_from_menu(menu, "E-boutique", "Accès E-boutique")

do_eb = E_boutique(browser)
do_mp.set_cookies(value=False)

do_eb.login(user1,user1_psw)
do_mp.verify_url(url["Accès E-boutique"][1])

do_eb.open_account

do_eb.open_bills_menu

do_eb.open_account_menu

do_eb.check_email(user1)

do_eb.open_payment_menu

do_eb.add_card(cards[0]) # As a fake card is used I can only fill in the info and close the popup

do_eb.check_card_warnings(cards[0], card_errors)

do_eb.logout

browser.close()

logging.info('### End of Scenario05.')

