from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service  # firefox service
from webdriver_manager.firefox import GeckoDriver  # firefox browser
from selenium.webdriver.chrome.service import Service  # chrome service
from webdriver_manager.chrome import ChromeDriverManager  # chrome browser

import time


def web_search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # url
    driver.get('https://www.amazon.com')
    # search bar found by ID
    search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
    # search bar input text
    search_bar.send_keys('hard drive')
    # search bar submit button found by ID
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    # click search button
    search_button.click()

    #! there are 32 search results in an amazon web result before the button to next page.

    time.sleep(3)

    driver.quit()


web_search()
