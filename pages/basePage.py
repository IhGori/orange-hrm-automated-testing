from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage:    
	module_item = (By.CSS_SELECTOR, ".oxd-main-menu-item-wrapper")
	toast_response = (By.CSS_SELECTOR, "div.oxd-toast--success")
	list_of_modules = (By.CSS_SELECTOR, ".oxd-main-menu")
	def __init__(self, driver):
		self.driver = driver

	def open_url(self, url):
		self.driver.get(url)
		
	def check_url(self, url):
		return self.driver.current_url == url

	def await_element(self, *locator, timeout=5):
		return WebDriverWait(self.driver, timeout).until(
			EC.visibility_of_element_located(locator)
		)

	def click_element(self, locator):
		self.await_element(*locator).click()

	def input_text(self, locator, text):
		self.await_element(*locator).send_keys(text)

	def to_module(self, module):
		self.click_element((By.LINK_TEXT, module))
		
	def send_keys_to_element(self, locator, text):
		#limpar texto 
		self.driver.find_element(*locator).send_keys(Keys.CONTROL, 'a')
		self.driver.find_element(*locator).send_keys(Keys.BACKSPACE)
		#escrever
		self.driver.find_element(*locator).send_keys(text)

	def access_module(self, moduleName):
		WebDriverWait(self.driver, 10).until(
			EC.visibility_of_element_located(self.list_of_modules)
		)

		modules = self.driver.find_elements(*self.module_item)
		for module in modules:
			if module.text == moduleName:
				WebDriverWait(self.driver, 5).until(
					EC.element_to_be_clickable(module)
				).click()
				break

	def verify_toast_message(self, msg):
		success_toast = self.await_element(*self.toast_response)
		toast_message = success_toast.find_element(By.CLASS_NAME, "oxd-text--toast-message").text

		assert toast_message == msg, "mensagem inválida"