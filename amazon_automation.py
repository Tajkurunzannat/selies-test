import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
dropdownItems = Select(driver.find_element("id","searchDropdownBox"))
dropdownItems.select_by_visible_text("Baby")
time.sleep(2)
driver.find_element("id","twotabsearchtextbox").send_keys("bag")
time.sleep(2)
driver.find_element("id","nav-search-submit-button").submit()
time.sleep(3)

driver.close()
