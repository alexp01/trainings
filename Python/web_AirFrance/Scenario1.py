# The website will block the click of Search button so i can not continue this test. Even in manual the Search does not work.
# The same for login.
''' Scope
Perform a search and verify that the first flight will match the seach criterias:
- 1 Adult and 1 Child
- Start Date : Today + X days
- Return Date : Today + X days + Y days
- Departure : Paris
- Arrival : Lyon
'''

from main import Driver
from Python.web_AirFrance.main_page import Main_page
import logging
import datetime

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s',
    datefmt = '%d-%m-%Y %H:%M:%S',
    level=logging.INFO,
    filename = datetime.datetime.today().strftime('%d-%m-%Y %H_%M_%S') + '_logs.txt',
    filemode = "w"
)
logger = logging.getLogger('test_logger')

chromeDriver = Driver(page = "https://wwws.airfrance.fr")
options = ["start-maximized"]
browser = chromeDriver.start(options, block_privacy=True)

do = Main_page(browser)

# Close the Cookie popup that will be visible at every page start
do.close_cookie_popup()
logging.info('Close the Cookie popup that will be visible at every page start')

# Expand the Search area
do.expand_search_area()
logging.info('Expand the Search area')

# Add Start date = (today + start_date) days and Return_date = (today + start_date + return_date) days
# If no return_date is given, default is +1.
# If return_date=None is given then we only add the Start date.
do.add_dates(start_days = 27, return_days = 100)
logging.info('Add Start date = (today + start_date) days and Return_date = (today + start_date + return_date) days')

# Set number of passengers
dict_passengers = {'infant_0_1' : 0,
                   'child_2_11' : 0,
                   'youth_12_17' : 0,
                   'youth_18_24' : 2,
                   'student_18_29': 0,
                   'adult': 3,
                   'senior>69': 0}
# this dict will define how many passengers will be selected, by type of passenger
do.set_passengers(dict_passengers)
logging.info('Set number of passengers')
logging.info(dict_passengers)

# Set Departure
do.set_departure('Paris')
do.set_landing('Lyon')

do.perform_search(family=True)

browser.save_screenshot('search_criteria.png')

print("Finish")