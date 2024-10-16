from selenium.webdriver.common.by import By

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.ID, "menu_pim_viewPimModule")
        self.add_button = (By.XPATH, "//button[normalize-space()='+ Add']")

    def go_to_pim_module(self):
        self.driver.find_element(*self.pim_menu).click()

    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def search_employee(self, employee_name):
        self.input_text(self.input_employee_name, employee_name)
        self.click_element(self.button_search)

    def is_employee_record_displayed(self):
        return self.check_element_visible(self.employee_table)

    def delete_employee(self):
        self.click_element(self.delete_icon)

    def confirm_delete(self):
        self.click_element(self.confirm_delete_button)

    def is_confirmation_modal_displayed(self):
        return self.check_element_visible(self.confirmation_modal)