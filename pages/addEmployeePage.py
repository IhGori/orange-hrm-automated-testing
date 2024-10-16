from selenium.webdriver.common.by import By

class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.NAME, "firstName")
        self.middle_name_input = (By.NAME, "middleName")
        self.last_name_input = (By.NAME, "lastName")
        self.create_login_details_toggle = (By.XPATH, "//span[@class='oxd-switch-input']")
        self.username_input = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
        self.status_dropdown = (By.XPATH, "//label[text()='Status']/../following-sibling::div//div[text()='Enabled']")
        self.password_input = (By.XPATH, "//input[@type='password']")
        self.confirm_password_input = (By.XPATH, "//input[@name='confirmPassword']")
        self.save_button = (By.XPATH, "//button[@type='submit']")

    def add_employee(self, first_name, middle_name, last_name, username, password, confirm_password, status="Enabled"):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.middle_name_input).send_keys(middle_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.create_login_details_toggle).click()
        self.driver.find_element(*self.username_input).send_keys(username)
        if status == "Enabled":
            self.driver.find_element(*self.status_dropdown).click()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)
        self.driver.find_element(*self.save_button).click()
