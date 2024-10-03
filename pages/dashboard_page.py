

"""
class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.info_locator_ele = (By.XPATH, "//span[normalize-space()='My Info']")
        self.success_info_ele = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        self.max_wait_interval = MAX_WAIT_INTERVAL

    def navigate_to_MyInfo(self):
        try:
            info_button = self.explicitly_wait_until_clickable(self.max_wait_interval, self.info_locator_ele)
            info_button.click()
        except Exception as e:
            print(f"Failed to navigate to 'My Info': {str(e)}")
            return False
        return True

    def verify_MyInfo(self):
        try:
            success_element = self.explicitly_wait_and_find_element(self.max_wait_interval, self.success_info_ele)
            assert success_element is not None, "Navigation to 'My Info' Tab failed. Success element not found."
        except AssertionError as e:
            print(str(e))
            return False
        return True

"""
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from resources.constants import MAX_WAIT_INTERVAL

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.info_locator_ele = (By.XPATH, "//span[normalize-space()='My Info']")
        self.success_info_ele = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        self.max_wait_interval = MAX_WAIT_INTERVAL

    def navigate_to_MyInfo(self):
        """Navigates to the 'My Info' section."""
        time.sleep(2)
        self.save_screenshot("dashboard_page.png")
        self.explicitly_wait_until_clickable(self.max_wait_interval, self.info_locator_ele).click()

    def verify_MyInfo(self):
        """Verifies that the user has successfully navigated to the 'My Info' section."""
        success_element = self.explicitly_wait_and_find_element(self.max_wait_interval, self.success_info_ele)
        assert success_element is not None, "Navigation to 'My Info' Tab failed. Success element not found."
