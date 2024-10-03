'''
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from resources.constants import TEST_SITE_URL, MAX_WAIT_INTERVAL, EXPECTED_SUCCESS_URL


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_username = (By.XPATH, "//input[@name='username']")
        self.login_password = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        self.login_error = (By.XPATH, "//div[@role='alert']")
        self.success_ele=(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    def login_with_valid(self, username, password):
        self.navigate_to(TEST_SITE_URL)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.login_username).send_keys(username)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.login_password).send_keys(password)
        #self.explicitly_wait_until_clickable(self.login_button).click()
        # Use explicitly_wait_until_clickable before clicking the login button
        self.explicitly_wait_until_clickable(MAX_WAIT_INTERVAL, self.login_button).click()

    def verify_login(self):
        """Verifies the login by checking a specific element or URL."""
        success_element = self.explicitly_wait_and_find_element(self.MAX_WAIT_INTERVAL, self.success_element)
        assert success_element is not None, "Login failed. Success element not found."

        current_url = self.driver.current_url
        assert EXPECTED_SUCCESS_URL == current_url, "URL after login does not match expected." '''
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from resources.constants import TEST_SITE_URL, MAX_WAIT_INTERVAL, EXPECTED_SUCCESS_URL

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_username = (By.XPATH, "//input[@name='username']")
        self.login_password = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        self.login_error = (By.XPATH, "//div[@role='alert']")
        self.success_ele = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    def login_with_valid(self, username, password):
        #self.navigate_to(TEST_SITE_URL)
        time.sleep(3)
        self.save_screenshot("Login_navigate_screen_shot.png")
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.login_username).send_keys(username)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.login_password).send_keys(password)
        self.explicitly_wait_until_clickable(MAX_WAIT_INTERVAL, self.login_button).click()
    def verify_login(self):
        """Verifies the login by checking a specific element or URL."""
        success_element = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.success_ele)
        assert success_element is not None, "Login failed. Success element not found."
        current_url = self.get_current_url()
        time.sleep(3)
        self.save_screenshot("Verify_login_screenShot.png")
        assert EXPECTED_SUCCESS_URL == current_url, f"URL after login does not match expected. Got {current_url}"
