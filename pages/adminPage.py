import time
from pages.basePage import BasePage
from selenium.webdriver.common.by import By
from datetime import datetime



class AdminPage(BasePage):
    dt = datetime.now()
    url_admin = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
    button_job = (By.XPATH, "//span[.='Job ']")
    button_job_titles = (By.XPATH, "//a[.='Job Titles']")
    button_add_job_title = (By.XPATH, "//button[.=' Add ']")
    button_delete_job_title = (By.XPATH, f"//div[.='Job Title - {str(dt.microsecond)}']/following::button/i[contains(@class,'trash')]")
    button_edit_job_title = (By.XPATH, f"//div[.='Job Title - {str(dt.microsecond)}']/following::button/i[contains(@class,'pencil')]")
    button_confirm_delete_job_title = (By.XPATH ,"//button[.=' Yes, Delete ']")
    url_add_job_title = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveJobTitle"
    label_job_title = (By.XPATH,"//label[.='Job Title']/parent::div/following-sibling::div/input")
    label_job_description = (By.XPATH,"//textarea[@placeholder='Type description here']")
    button_save = (By.XPATH, "//button[.=' Save ']")
    
    
    def load_add_job_title(self):
        self.click_element(self.button_job)
        self.click_element(self.button_job_titles)
        self.click_element(self.button_add_job_title)
        self.check_url(self.url_add_job_title)
    
    def fill_job_fields(self):
        self.click_element(self.label_job_title)
        self.send_keys_to_element(self.label_job_title, "Job Title - " + str(self.dt.microsecond))
        self.send_keys_to_element(self.label_job_description, "Job Description - " + str(self.dt.microsecond))
        
        self.click_element(self.button_save)
    
    def verify_job_saved(self):
        self.verify_toast_message("Successfully Saved")
        # TODO: Verificar valores de Job Title e Job Description em tela
    
    def delete_job_title(self):
        self.click_element(self.button_delete_job_title)
        self.click_element(self.button_confirm_delete_job_title)
        self.verify_toast_message("Successfully Deleted")
        # TODO: Verificar valores de Job Title e Job Description não estão em tela
    
    def edit_job_title(self):
        self.click_element(self.button_edit_job_title)
        self.fill_job_fields()
        self.verify_toast_message("Successfully Updated")