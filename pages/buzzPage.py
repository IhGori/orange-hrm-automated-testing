from pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BuzzPage(BasePage):
	url_recruitment = "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates"
	list_of_modules = (By.CSS_SELECTOR, ".oxd-main-menu")
	module_item = (By.CSS_SELECTOR, ".oxd-main-menu-item-wrapper")
	input_new_post = (By.CLASS_NAME, "oxd-buzz-post-input")
	button_new_post = (By.CSS_SELECTOR, "button[type='submit']")
	post_card = (By.CLASS_NAME, "oxd-grid-1 orangehrm-buzz-newsfeed-posts")
	heart_icon = (By.ID, "heart-svg")
	three_dots_icon = (By.CLASS_NAME, "oxd-icon.bi-three-dots")
	three_dots_dropdown_menu = (By.CLASS_NAME, "oxd-dropdown-menu")
	delete_post_option = (By.XPATH, "//p[text()='Delete Post']")
	confirmation_modal = (By.CLASS_NAME, "oxd-dialog-container-default--inner")
	confirm_delete_button = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
	toast_response = (By.CSS_SELECTOR, "div.oxd-toast--success")
	toast_text = (By.CSS_SELECTOR, "oxd-toast-content-text")

	def access_module(self):
		WebDriverWait(self.driver, 10).until(
			EC.visibility_of_element_located(self.list_of_modules)
		)

		modules = self.driver.find_elements(*self.module_item)
		for module in modules:
			if module.text == 'Buzz':
				WebDriverWait(self.driver, 5).until(
					EC.element_to_be_clickable(module)
				).click()
				break
	
	def create_post(self):
		self.await_element(*self.input_new_post).send_keys("Olá pessoal!")
		self.click_element(self.button_new_post)
		success_toast = self.await_element(*self.toast_response)
		toast_message = success_toast.find_element(By.CLASS_NAME, "oxd-text--toast-message").text

		assert toast_message == "Successfully Saved", "Post não foi criado"

	def test_like_post(self):
		self.click_element(self.heart_icon)


	def delete_post(self):
		# Adicionado um delay para dar tempo do elemento aparecer toast da criacão do post sumir
		time.sleep(2)

		self.click_element(self.three_dots_icon)
		self.click_element(self.delete_post_option)
		self.click_element(self.confirm_delete_button)
		success_toast = self.await_element(*self.toast_response)
		toast_message = success_toast.find_element(By.CLASS_NAME, "oxd-text--toast-message").text

		assert toast_message == "Successfully Deleted", "Post não foi criado"
