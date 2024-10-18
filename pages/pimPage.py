import time
from selenium.webdriver.common.by import By

from pages.basePage import BasePage

class PIMPage(BasePage): 
    url_pim = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    list_of_modules = (By.CSS_SELECTOR, ".oxd-main-menu")
    module_item = (By.CSS_SELECTOR, ".oxd-main-menu-item-wrapper")
    label_employee_list = (By.XPATH, ".orangehrm-paper-container")
    button_add_employee_list = (By.XPATH, "//button[.=' Add ']")
    url_add_employee_list = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"
    first_name_input = (By.NAME, "firstName")
    middle_name_input = (By.NAME, "middleName")
    last_name_input = (By.NAME, "lastName")
    create_login_details_toggle = (By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    username_input = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
    status_dropdown = (By.XPATH, ".oxd-radio-input")
    password_input = (By.XPATH, "//label[text()='Password']/../following-sibling::div/input")
    confirm_password_input = (By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div/input")
    save_button = (By.XPATH, "//button[.=' Save ']")
    employee_name_input = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    search_button = (By.XPATH, "//button[.=' Search ']")
    select_employee = (By.XPATH, "(//span[contains(@class, 'oxd-checkbox-input')])[1]")
    delete_button = (By.XPATH, "//button[.=' Delete Selected ']")
    confirm_delete_button = (By.XPATH, "//button[.=' Yes, Delete ']")

    def go_to_pim_module(self):
        self.click_element(self.button_add_employee_list)
        time.sleep(2)
        self.check_url(self.url_add_employee_list)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def add_employee(self):
        self.find_element(self.first_name_input).send_keys("João")
        self.find_element(self.middle_name_input).send_keys("Silva")
        self.find_element(self.last_name_input).send_keys("Sousa")
        self.find_element(self.create_login_details_toggle).click()
        self.find_element(self.username_input).send_keys("joaosousa")
        self.find_element(self.password_input).send_keys("joao123")
        self.find_element(self.confirm_password_input).send_keys("joao123")      
        self.find_element(self.save_button).click()

    def message_employee_saved(self):
        time.sleep(2)
        self.verify_toast_message("Successfully Saved")

    def search_employee(self):    
        time.sleep(2)
        self.find_element(self.employee_name_input).send_keys("João Silva")
        self.find_element(self.search_button).click()
        time.sleep(2)

    def delete_employee(self):    
        self.click_element(self.select_employee)
        self.click_element(self.delete_button)
        self.click_element(self.confirm_delete_button)
        time.sleep(2)
        self.verify_toast_message("Successfully Deleted")


        


