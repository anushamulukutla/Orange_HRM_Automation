
import time
import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.my_info_page import My_info_locators
from resources.constants import EXPECTED_SUCCESS_URL_MYINFO


class TestOrange:
    @pytest.mark.usefixtures("driver", "username_password")
    def test_login_with_valid_cred(self, driver, username_password):
        login_page = LoginPage(driver)
        login_page.login_with_valid(username_password[0], username_password[1])

    @pytest.mark.usefixtures("driver")
    def test_navigate_dashboard_myinfo(self, driver):
        #navigating to myinfo tab
        dashboard_page = DashboardPage(driver)
        dashboard_page.navigate_to_MyInfo()
        time.sleep(2)

    @pytest.mark.usefixtures("driver")
    def test_verify_myinfo_loaded(self,driver ):
        #verifying myinof page  is succesfully loaded
        dashboard_page = DashboardPage(driver)
        dashboard_page.verify_MyInfo()
        expected_url = EXPECTED_SUCCESS_URL_MYINFO
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Expected URL to be {expected_url}, but got {actual_url}"

    @pytest.mark.usefixtures("driver")
    #fn,mn,ln,emp_id,driverse_license,driverse_license_expiry
    def test_enter_personal_details(self,driver):
        my_info_page=My_info_locators(driver)
        time.sleep(2)
        my_info_page.clear_all_fields()
        time.sleep(5)
        driver.refresh()
        personal_details=('demo',"user","sample","emp123","456987")
        my_info_page.enter_personal_fields_details(*personal_details)

    def test_verify_save_personal_details(self):

        pass

    @pytest.mark.usefixtures("driver")
    def test_add_file_attachment(self,driver):
        #path--/Users/ramchandupindiproli/PycharmProjects/Orangehrm_final_Project/resources
        file_path = "/Users/ramchandupindiproli/PycharmProjects/Orangehrm_final_Project/resources/test_selenium-automation.pdf"
        my_info_page = My_info_locators(driver)
        my_info_page.click_add_button_and_upload_file(file_path)


