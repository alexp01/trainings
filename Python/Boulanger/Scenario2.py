from main import Driver
from common_content import Main_content
from selenium.webdriver.common.by import By

chromeDriver = Driver(page = "https://wwws.airfrance.fr/en")
options = ["start-maximized"]
browser = chromeDriver.start(options, block_privacy=True)

#browser.save_screenshot('foo.png')

do = Main_content(browser)

# Close the Cookie popup that will be visible at every page start
do.close_cookie_popup()

# Expand the Search area
do.expand_search_area()

# Add Start date = (today + start_date) days and Return_date = (today + start_date + return_date) days
# If no return_date is given, default is +1.
# If return_date=None is given then we only add the Start date.
do.add_dates(start_days = 27, return_days = 100)

# Set number of passengers
dict_passengers = {'infant_0_1' : 0,
                   'child_2_11' : 0,
                   'youth_12_17' : 0,
                   'youth_18_24' : 1,
                   'student_18_29': 0,
                   'adult': 2,
                   'senior>69': 0}
# this dict will define how many passengers will be selected, by type of passenger

do.set_passengers(dict_passengers)

print("Finish")