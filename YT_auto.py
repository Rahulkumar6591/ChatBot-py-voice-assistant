from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class Music:
    def __init__(self):
        # Disable GPU rendering
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Initialize the Chrome WebDriver with options
        self.driver = webdriver.Chrome(options=chrome_options)

    def play(self, query):
        # Open YouTube
        self.driver.get("https://www.youtube.com")

        # Allow time for the page to load
        time.sleep(0)

        # Find the search input box using By.NAME and perform a search
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(query)  # Type the query into the search box
        search_box.send_keys(Keys.RETURN)  # Simulates pressing Enter

        print(f"Searching for: {query}")

        # Allow time for search results to load
        time.sleep(0)

        # Click on the first video in the results
        first_video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        first_video.click()

        print("Playing the first video...")

        # Allow time for the video page to load
        time.sleep(2)

        # Use JavaScript to get the video duration
        video_duration = self.driver.execute_script(
            "return document.querySelector('video').duration;"
        )
        print(f"Video duration: {video_duration} seconds")

        # Wait for the video to finish playing
        time.sleep(video_duration)

        print("Video has finished playing.")

# Instantiate and use the class
# assist = Music()
# assist.play("")
# assist.driver.quit()  # Close the browser
