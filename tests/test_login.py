import pytest
from pages.loginPage import LoginPage
import time

def test_login(driver):
	login_p = LoginPage(driver)
	login_p.to_url()
	login_p.login()
	login_p.assert_url()