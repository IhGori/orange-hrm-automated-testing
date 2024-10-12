from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
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
		self.driver.find_element(*locator).send_keys(text)
