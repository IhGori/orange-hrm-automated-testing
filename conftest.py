import pytest
from selenium import webdriver
from pages.loginPage import LoginPage

@pytest.fixture(scope="function")
def driver():
	driver = webdriver.Chrome()
	driver.maximize_window()
	yield driver
	driver.quit()

@pytest.fixture(scope="function")
def logged_in_page(driver):
	login_p = LoginPage(driver)
	login_p.to_url()
	login_p.login()
	return driver
