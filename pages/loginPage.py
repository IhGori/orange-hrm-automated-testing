from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class LoginPage(BasePage):
	url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
	input_username = (By.CSS_SELECTOR, "input[name='username']")
	text_username = "Admin"
	input_password = (By.CSS_SELECTOR, "input[name='password']")
	text_password = "admin123"
	button_login = (By.XPATH, "//button[@type='submit']")
	dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
	
	def to_url(self):
		self.open_url(self.url)

	def assert_url(self):
		self.check_url(self.dashboard_url)

	def login(self):
		self.input_text(self.input_username, self.text_username)
		self.input_text(self.input_password, self.text_password)
		self.click_element(self.button_login)
	

