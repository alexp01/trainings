''' Scope
Will Go into a menu and login.
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

logging.info(' ### Scenario02 ####################################.')

do_mp.open_from_menu(menu, "E-boutique", "Accès E-boutique")

do_eb = E_boutique(browser)
do_mp.verify_url(url["Accès E-boutique"][0])

#do_eb.login(user1,user1_psw)
#do_mp.verify_url(url["Accès E-boutique"][1])

#do_eb.open_account

#do_eb.expand_filters
#do_eb.expand_filters

do_eb.verify_filters_presence(tickets_categories)

#do_eb.apply_filter(tickets_categories[4])
#do_eb.apply_filter(tickets_categories[2])
#do_eb.remove_filter(tickets_categories[2])
#do_eb.remove_filter(tickets_categories[4])

do_eb.verify_categories(tickets_categories)

#do_eb.expand_category(tickets_categories[4])
#do_eb.expand_category(tickets_categories[2])
#do_eb.expand_category(tickets_categories[5])

#do_eb.hide_category(tickets_categories[4])
#do_eb.expand_category(tickets_categories[4])

logging.info(' ### End of Scenario02.')