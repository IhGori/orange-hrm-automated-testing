from pages.pimPage import PIMPage
from pages.loginPage import LoginPage

def test_add_new_employee(logged_in_page):
    # Acessar o módulo PIM e clicar em Add
    pim_p = PIMPage(logged_in_page)
    pim_p.access_module("PIM")
    pim_p.go_to_pim_module()
    pim_p.add_employee()
    pim_p.message_employee_saved()

def test_search_employee(logged_in_page):
    pim_p = PIMPage(logged_in_page)
    pim_p.access_module("PIM")
    pim_p.search_employee()
    
def test_delete_employee(logged_in_page):
    pim_p = PIMPage(logged_in_page)
    pim_p.access_module("PIM")
    pim_p.search_employee()
    pim_p.delete_employee()
