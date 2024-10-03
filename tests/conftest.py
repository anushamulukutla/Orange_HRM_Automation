import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def driver():
  #  _driver=webdriver.Firefox()
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    _driver.get("https://www.google.com")
    search_filed = _driver.find_element(By.NAME, "q")
    search_filed.send_keys("orangehrm login page")
    # search button
    wait = WebDriverWait(_driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "gNO89b")))
    # Now perform the click
    button.click()
    link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a/h3")))
    link.click()
    yield _driver
    _driver.quit()
@pytest.fixture(scope="session")
def username_password():

    user_name = "Admin"
    password = "admin123"
    return [user_name, password]

@pytest.fixture(scope="session")
def login(driver, username_password):
    """Fixture to log in once and reuse the session."""
    login_page = LoginPage(driver)
    login_page.login_with_valid(username_password[0], username_password[1])
    return driver  # Return the driver with an active session


@pytest.fixture(scope="module")
def invalid_username_password(username_password):
    user_name_invalid = "InvalidUser"
    password_invalid = "InvalidPass"
    if user_name_invalid == username_password[0]:
        user_name_invalid = None
    if password_invalid == username_password[1]:
        password_invalid = None
    return [user_name_invalid, password_invalid]