from pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class RecruitmentPage(BasePage):
	url_recruitment = "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates"
	url_recruitment_vacancies = "https://2131312opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy"
	url_recruitment_candidates = "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates"
	list_of_modules = (By.CSS_SELECTOR, ".oxd-main-menu")
	module_item = (By.CSS_SELECTOR, ".oxd-main-menu-item-wrapper")
	recruitment_item_text = (By.LINK_TEXT, "Recruitment")
	tab_recruitment_vacancies = (By.XPATH, "//a[normalize-space()='Vacancies']")
	button_new_vacancy = (By.XPATH, "//button[normalize-space()='Add']")
	

	def access_module(self):
		WebDriverWait(self.driver, 10).until(
			EC.visibility_of_element_located(self.list_of_modules)
		)

		modules = self.driver.find_elements(*self.module_item)
		for module in modules:
			if module.text == 'Recruitment':
				WebDriverWait(self.driver, 5).until(
					EC.element_to_be_clickable(module)
				).click()
				# module.click()
				break

	def access_vacancies(self):
		self.click_element(self.tab_recruitment_vacancies)
		self.click_element(self.button_new_vacancy)





