
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from resources.constants import MAX_WAIT_INTERVAL
class My_info_locators(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.First_Name = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
        #self.First_Name = (By.NAME, "firstName")
       # self.Middle_Name = (By.XPATH, "//input[@placeholder='Middle Name']") //*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input
        self.Middle_Name = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input")
        #self.Last_Name = (By.XPATH, "//input[@placeholder='Last Name']")//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input
        self.Last_Name = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
        self.Employee_ID = (By.XPATH,"//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[1]/div[1]/div[1]/div[2]/input[1]")
        self.Driverse_License = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
        self.save_button= (By.CSS_SELECTOR,"#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div.oxd-form-actions > button")
        #self.add_button = (By.XPATH, "//button[normalize-space()='Add']")
        self.add_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button")
        self.file_input = (By.XPATH, "//div[@class='oxd-file-button']")
        self.save_button_file = (By.XPATH, "//div[@class='orangehrm-attachment']//button[@type='submit'][normalize-space()='Save']")

    def scroll_by_pixels(self, pixels=300):

        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def scroll_into_view(self, element):

        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)


    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    def clear_all_fields(self):
        first_name_input = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until( EC.presence_of_element_located(self.First_Name))
        first_name_input.clear()
        middle_name_input = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(EC.presence_of_element_located(self.Middle_Name) )
        middle_name_input.clear()
        last_name_input = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until( EC.presence_of_element_located(self.Last_Name) )
        last_name_input.clear()
        employee_id_input = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(EC.presence_of_element_located(self.Employee_ID) )
        employee_id_input.clear()
        drivers_license_input = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until( EC.presence_of_element_located(self.Driverse_License))
        drivers_license_input.clear()

    def enter_personal_fields_details(self, first_name, middle_name, last_name, emp_id, license_number):

            try:
                first_name_field = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(EC.presence_of_element_located(self.First_Name))
                first_name_field.send_keys(first_name)
                middle_name_field = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(EC.presence_of_element_located(self.Middle_Name))
                middle_name_field.send_keys(middle_name)
                last_name_field = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until( EC.presence_of_element_located(self.Last_Name) )
                last_name_field.send_keys(last_name)
                employee_id_field = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(EC.presence_of_element_located(self.Employee_ID))
                employee_id_field.send_keys(emp_id)
                driver_license_field = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(EC.presence_of_element_located(self.Driverse_License))
                driver_license_field.send_keys(license_number)
                # Wait for the save button to be clickable before clicking
                save_button_element = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until( EC.element_to_be_clickable(self.save_button))
                self.save_screenshot("my_info_page_ss_1.png")
                self.scroll_into_view(save_button_element)
                time.sleep(2)
                self.save_screenshot("Myinfo_page_SS_2.png")
                save_button_element.click()
            except Exception as e:
                print(f"Failed to interact with the save button: {e}")
                self.driver.save_screenshot('save_button_error.png')  # Take a screenshot for debugging
                raise

    def click_add_button_and_upload_file(self, file_path):
        try:
            self.scroll_to_bottom()  # Ensure that the element is visible
            add_button_element = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
                EC.element_to_be_clickable(self.add_button)
            )
            add_button_element.click()
            file_input_element = self.driver.find_element(By.XPATH, "//input[@type='file']")
            self.driver.execute_script("arguments[0].style.display = 'block';", file_input_element)
            # Send the file path to the input element
            file_input_element.send_keys(file_path)
            self.save_screenshot("file_upload_success.png")
            save_button = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
                EC.element_to_be_clickable(self.save_button_file)
            )
            save_button.click()
        except Exception as e:
            print(f"Failed to upload the file: {e}")
            self.driver.save_screenshot('file_upload_error.png')
            raise




