from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get('https://wwws.airfrance.fr/')

select = Select(driver.find_element(By.CSS_SELECTOR,'[data-test="bwsfe-passenger-manager__add-passenger"]'))

# select by visible text
select.select_by_visible_text('Banana')

# select by value
select.select_by_value('1')