from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class Infow:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        # Open Wikipedia
        self.driver.get("https://www.wikipedia.org")

        # Find the search input box using By.ID and perform a search
        search_box = self.driver.find_element(By.ID, "searchInput")
        search_box.send_keys(query)  # Type the query into the search box
        search_box.send_keys(Keys.RETURN)  # Simulates pressing Enter

        print(f"Searching for: {query}")

# Instantiate and use the class
# assist = Infow()
# assist.get_info("Lovely professional university")
# time.sleep(10)