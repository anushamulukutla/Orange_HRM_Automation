'''def clear_and_enter_text(self, locator_type_and_locator_tuple, text):
    """
    Clears the text field and enters new text.
    :param locator_type_and_locator_tuple: Tuple (By, locator string)
    :param text: String text to enter into the field
    """
    element = self.explicitly_wait_and_find_element(10, locator_type_and_locator_tuple)  # Wait up to 10 seconds
    element.clear()  # Clear the text field
    element.send_keys(text)  # Enter the new text


def clear_all_fields(self):
    input_fields = self.driver.find_elements(By.CSS_SELECTOR,
                                             "input:not([type='checkbox']):not([type='radio']):not([type='button']):not([type='submit'])")
    for field in input_fields:
        field.clear()
    text_areas = self.driver.find_elements(By.TAG_NAME, "textarea")
    for area in text_areas:
        area.clear()
    select_elements = self.driver.find_elements(By.TAG_NAME, 'select')
    for select_element in select_elements:
        Select(select_element).select_by_visible_text('--Select--')




        #method with no error
        def clear_field_js(self, locator):
            """ Clears the text field using JavaScript """
            element = self.explicitly_wait_and_find_element(10, locator)  # Assuming 10 seconds wait time
            self.driver.execute_script("arguments[0].value = '';", element)

        def clear_and_enter_text(self, locator, text, timeout=10):
            """ Clears the field using JavaScript and enters new text. """
            self.clear_field_js(locator)  # Clear using JavaScript
            element = self.explicitly_wait_and_find_element(timeout, locator)
            element.send_keys(text)  # Enter the new text








from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def enter_personal_fields_details(self, first_name, middle_name, last_name, emp_id, license_number):
    """Enter personal details and save."""
    try:
        # Wait for the First Name input field to be present
        first_name_field = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
            EC.presence_of_element_located(self.First_Name)
        )
        first_name_field.send_keys(first_name)

        middle_name_field = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
            EC.presence_of_element_located(self.Middle_Name)
        )
        middle_name_field.send_keys(middle_name)

        last_name_field = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
            EC.presence_of_element_located(self.Last_Name)
        )
        last_name_field.send_keys(last_name)

        employee_id_field = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
            EC.presence_of_element_located(self.Employee_ID)
        )
        employee_id_field.send_keys(emp_id)

        driver_license_field = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
            EC.presence_of_element_located(self.Driverse_License)
        )
        driver_license_field.send_keys(license_number)

        # Wait for the save button to be clickable before clicking
        save_button_element = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
            EC.element_to_be_clickable(self.save_button)
        )
        self.save_screenshot("my_info_page_ss_1.png")
        self.scroll_into_view(save_button_element)
        time.sleep(2)
        self.save_screenshot("Myinfo_page_SS_2.png")
        save_button_element.click()
    except Exception as e:
        print(f"Failed to interact with the save button: {e}")
        self.driver.save_screenshot('save_button_error.png')  # Take a screenshot for debugging
        raise
#cut from infopage
 """Enter personal details and save."""
        # Fill in personal details (assuming the methods to enter these fields are present in BasePage)
        try:
            self.driver.find_element(*self.First_Name).send_keys(first_name)
            self.driver.find_element(*self.Middle_Name).send_keys(middle_name)
            self.driver.find_element(*self.Last_Name).send_keys(last_name)
            self.driver.find_element(*self.Employee_ID).send_keys(emp_id)
            self.driver.find_element(*self.Driverse_License).send_keys(license_number)
            save_button_element = self.driver.find_element(*self.save_button)
            self.save_screenshot("my_info_page_ss_1.png")
            self.scroll_into_view(save_button_element)
            time.sleep(2)
            self.save_screenshot("Myinfo_page_SS_2.png")
            save_button_element.click()
        except Exception as e:
            print(f"Failed to interact with the save button: {e}")
            self.driver.save_screenshot('save_button_error.png')  # Take a screenshot for debugging
            raise
'''