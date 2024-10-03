'''from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import expected_conditions as EC

# base page
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)
    def go_back(self):
        self.driver.back()
    def get_current_url(self):
        self.driver.current_url

    def explicitly_wait_and_find_element(self, interval, locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.presence_of_element_located(locator_type_and_locator_tuple))

    def explicitly_wait_until_clickable(self, interval, locator_type_and_locator_tuple):
        """
        Wait for the specified interval until the element specified is clickable and return it.
        """
        return WebDriverWait(self.driver, interval).until(EC.element_to_be_clickable(locator_type_and_locator_tuple))

    def find_element(self, locator_type_and_locator_tuple):
        return self.driver.find_element(*locator_type_and_locator_tuple)'''
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from resources.constants import MAX_WAIT_INTERVAL


# base page
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def go_back(self):
        self.driver.back()

    def get_current_url(self):
        return self.driver.current_url

    def explicitly_wait_and_find_element(self, interval, locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.presence_of_element_located(locator_type_and_locator_tuple))

    def explicitly_wait_until_clickable(self, interval, locator_type_and_locator_tuple):
        """
        Wait for the specified interval until the element specified is clickable and return it.
        """
        return WebDriverWait(self.driver, interval).until(ec.element_to_be_clickable(locator_type_and_locator_tuple))

    def find_element(self, locator_type_and_locator_tuple):
        return self.driver.find_element(*locator_type_and_locator_tuple)

    def save_screenshot(self, file_name):
        """Save screenshot to a specific folder."""
        folder_path = "screenshots"  # Specify your folder name
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # Full path for the screenshot
        screenshot_path = os.path.join(folder_path, file_name)
        # Save the screenshot
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")


