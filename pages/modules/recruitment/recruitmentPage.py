from pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import string
import time

class RecruitmentPage(BasePage):
	url_recruitment = "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates"
	url_add_job = "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addJobVacancy"
	url_recruitment_vacancies = "https://2131312opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy"
	url_recruitment_candidates = "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates"
	list_of_modules = (By.CSS_SELECTOR, ".oxd-main-menu")
	module_item = (By.CSS_SELECTOR, ".oxd-main-menu-item-wrapper")
	recruitment_item_text = (By.LINK_TEXT, "Recruitment")
	tab_recruitment_vacancies = (By.XPATH, "//a[normalize-space()='Vacancies']")
	button_new_vacancy = (By.XPATH, "//button[normalize-space()='Add']")
	button_new_candidate = (By.XPATH, "//button[normalize-space()='Add']")
	input_vacancy_name = (By.XPATH, '//label[text()="Vacancy Name"]/../following-sibling::div//input')
	input_number_of_positions = (By.XPATH, '//label[text()="Number of Positions"]/../following-sibling::div//input') 
	input_job_title = (By.XPATH, '//label[text()="Job Title"]/../following-sibling::div//div[@class="oxd-select-text-input"]')
	toast_response = (By.CSS_SELECTOR, "div.oxd-toast--success")
	input_first_name = (By.CSS_SELECTOR, "input[name='firstName']")
	text_first_name = "Wardell"
	input_middle_name = (By.CSS_SELECTOR, "input[name='middleName']")
	text_middle_name = "Stephen"
	input_last_name = (By.CSS_SELECTOR, "input[name='lastName']")
	text_latest_name = "Curry"
	input_email = (By.XPATH, '//label[text()="Email"]/../following-sibling::div//input')
	text_email = "stephen.curry@example.com"
	input_keywords = (By.XPATH, '//label[text()="Keywords"]/../following-sibling::div//input')
	text_keywords = "Estudo, Cesar"
	input_notes = (By.XPATH, '//label[text()="Notes"]/../following-sibling::div//textarea')
	text_notes = "Preciso dessa vaga."
	vacancy_dropdown = (By.XPATH, '//label[text()="Vacancy"]/../following-sibling::div//div[@class="oxd-select-text-input"]')
	button_save = (By.XPATH, '//button[text()=" Save "]')
	input_filter_vacancy = (By.XPATH, '//label[text()="Vacancy"]/../following-sibling::div//div[@class="oxd-select-text-input"]')
	button_search = (By.XPATH, '//button[text()=" Search "]')
	input_text_area = (By.XPATH, '//label[text()="Description"]/../following-sibling::div//textarea')
	text_area = "Descrição da vaga para desenvolvedor"
	input_hiring_manager = (By.XPATH, '//label[text()="Hiring Manager"]/../following-sibling::div//input')
	url_add_vacancy = "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate"
	text_result_filter = (By.XPATH, '//div[@class="orangehrm-horizontal-padding orangehrm-vertical-padding"]//span')

	def generate_random_string(self):
		letters = string.ascii_letters
		return ''.join(random.choice(letters) for i in range(10))

	def test_create_vacancy(self):
		self.click_element(self.tab_recruitment_vacancies)
		self.click_element(self.button_new_vacancy)
		
		self.check_url(self.url_add_job)

		time.sleep(1)

		random_name = self.generate_random_string()
		self.send_keys_to_element(self.input_vacancy_name, random_name)
	
		job_title_select = self.driver.find_element(*self.input_job_title)
		job_title_select.click()

		options = WebDriverWait(self.driver, 10).until(
			EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="listbox"]//span'))
		)

		random_option = random.choice(options)
		random_option.click()

		hiring_manager_input = self.driver.find_element(*self.input_hiring_manager)
		hiring_manager_input.send_keys("a")
		time.sleep(2)
		hiring_manager_input.send_keys(Keys.ARROW_DOWN)
		hiring_manager_input.send_keys(Keys.ENTER)

		random_value = random.randint(1, 99)
		self.send_keys_to_element(self.input_number_of_positions, random_value)

		save_button = self.driver.find_element(*self.button_save)

		save_button.click()
		#Necessário colocar esse time, pois a plataforma está com algum problema e se não der o delay acaba não criando a vaga
		time.sleep(2)

		assert self.driver.current_url != self.url_add_vacancy

		self.access_module("Recruitment")

		return random_name

	def test_apply_for_the_vacancy(self, vacancy_name):
		self.click_element(self.button_new_candidate)

		WebDriverWait(self.driver, 10).until(
			EC.visibility_of_element_located(self.input_first_name)
		)

		self.send_keys_to_element(self.input_first_name, self.text_first_name)
		self.send_keys_to_element(self.input_middle_name, self.text_middle_name)
		self.send_keys_to_element(self.input_last_name, self.text_latest_name)

		self.click_element(self.vacancy_dropdown)

		vacancy_option_xpath = f'//div[@role="listbox"]//span[text()="{vacancy_name}"]'

		vacancy_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, vacancy_option_xpath)))
		vacancy_option.click()

		self.send_keys_to_element(self.input_email, self.text_email)
		self.send_keys_to_element(self.input_keywords, self.text_keywords)
		self.send_keys_to_element(self.input_notes, self.text_notes)

		self.click_element(self.button_save)

		self.access_module("Recruitment")


	def test_filter_vacancy(self, vacancy_name):
		self.click_element(self.input_filter_vacancy)
		
		vacancy_option_xpath = f'//div[@role="listbox"]//span[text()="{vacancy_name}"]'
		vacancy_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, vacancy_option_xpath)))
		vacancy_option.click()

		self.click_element(self.button_search)

		result_text = WebDriverWait(self.driver, 10).until(
			EC.visibility_of_element_located(self.text_result_filter)
		).text

		assert "No Records Found" not in result_text, "Nenhum registro encontrado para a vaga especificada"







