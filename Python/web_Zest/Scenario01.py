''' Scope
1. Open from menu : "Se déplacer"/"Télécharger les horaires"
2. Verify the content of 3 dropdowns
3. Select a value in each DropDown and then clean it.
'''

from pages.common.main import Driver
from pages.main_page import Main_page
from pages.telecharger_les_horaires import Telecharger_les_horaires
from conf.conf_file import *
from pages.common.log import *

class MyException(Exception):
    pass

chromeDriver = Driver(page = "https://www.zestbus.fr/")
options = ["start-maximized"]
browser = chromeDriver.start(options, block_privacy=True)

logging.info('### Scenario01 ####################################.')

do_mp = Main_page(browser)

do_mp.open_from_menu(menu, "Se déplacer", "Télécharger les horaires")

do_tlh = Telecharger_les_horaires(browser)

do_mp.verify_url(url["Télécharger les horaires"])

#do_tlh.refuse_cockies

# Check that all options are in Lignes dropdown
ligne_index_not_found = do_tlh.verify_lignes(lignes)
if ligne_index_not_found:
    raise MyException(f'Could not locate ligne : "{lignes[ligne_index_not_found]}".')

# Check that all options are in Cities dropdown
city_index_not_found = do_tlh.verify_cities(cities)
if city_index_not_found:
    raise MyException(f'Could not locate city : "{cities[city_index_not_found]}".')

# Check that all options are in Cities dropdown
point_index_not_found = do_tlh.verify_points(points)
if point_index_not_found:
    raise MyException(f'Could not locate point : "{points[point_index_not_found]}".')

# Select a ligne
do_tlh.select_by_ligne("LA NAVETTE")

# Clean the ligne
do_tlh.clean_ligne

# Select a city
do_tlh.select_by_city("Tende")

# Clean the ligne
do_tlh.clean_city

# Select a stopping point
do_tlh.select_by_point("Marché de Carnolès")

# Clean the stopping point
do_tlh.clean_point

browser.close()

logging.info('### End of Scenario01.')