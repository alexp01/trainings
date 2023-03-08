# The scope of this test is to do a search of a product, add it in the shoping cart, delete it from the shoping cart
from main import Driver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import logging

initial_start_time = datetime.now()
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s',
    datefmt = '%d-%m-%Y %H:%M:%S',
    level=logging.INFO,
    filename = 'logs.txt',
    filemode = "w"
)
logger = logging.getLogger('test_logger')
options = ["--disable-infobars", "start-maximized", "--disable-extensions"]
chromeDriver = Driver(page = "https://www.boulanger.com/")
browser = chromeDriver.start(options, block_privacy=True)

time.sleep(3)

#Closing the privacy popup by chanching frame in order to have access to the close button.
browser.switch_to.frame(browser.find_element(By.CSS_SELECTOR,'iframe[id="privacy-iframe"]'))
privicy_popup = browser.find_element(By.CSS_SELECTOR,'.modal-content')
if privicy_popup:
    close_button = browser.find_element(By.CSS_SELECTOR,'.close')
    close_button.click()
    browser.switch_to.default_content()

# STEP : Search for a product with "LG" and "TV" search inputs
# As the element is inside a Shadow-Root we need to go inside it to have access.
logging.info(' ### STEP ### : Search for a product with "LG" and "TV" search inputs')
search_type = "TV"
search_brand = "LG"
browser.execute_script('''return document.querySelector('bl-search#search__component').shadowRoot.querySelector('.search-input')''').send_keys(search_brand + " " + search_type)
browser.execute_script('''return document.querySelector('bl-search#search__component').shadowRoot.querySelector('.search-button')''').click()

# STEP : Verify that URL contains the search inputs
logging.info(' ### STEP ### : Search for a product with "LG" and "TV" search inputs')
current_url = browser.current_url
search_inputs = current_url.split('#tr=')[1]
assert search_brand + "+" + search_type == search_inputs, f' The current URL {current_url} does not have the search inputs : search_type:"{search_type}" and search_brand:"{search_brand}"'
logging.info(f' The current URL {current_url} has search inputs : search_type:"{search_type}" and search_brand:"{search_brand}"')

# STEP : Verify that the search results are TV products made by LG
logging.info(' ### STEP ### : Verify that the search results are TV products made by LG')
logging.info(' Comparing search result to the initial search criteria')
search_result_list = browser.find_elements(By.CSS_SELECTOR,'.product-item')
for product_element in search_result_list:
    product_text = product_element.find_element(By.CSS_SELECTOR,'.product-item__label').text
    assert (search_type.lower() in product_text.lower()) and (search_brand.lower() in product_text.lower()), f'The search results do not contain the proper search_type value : "{search_type}" or the search-brand value : "{search_brand}"'
    logger.info(f' In the search result text {product_text} we have found the search inputs : search_type:"{search_type}" and search_brand:"{search_brand}"')

# Add the step execution time in seconds
final_time = datetime.now() - initial_start_time
logger.info(f' The test execution took {final_time} seconds')