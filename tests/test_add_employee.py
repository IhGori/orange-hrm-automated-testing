from pages.pimPage import PIMPage
from pages.loginPage import LoginPage
from pages.addEmployeePage import AddEmployeePage

def test_add_new_employee(logged_in_page):
    # Acessar o site    
    # Login no sistema
    login_p = LoginPage(logged_in_page)
    login_p.login()  # Agora o método aceita os parâmetros
    login_p.assert_url()

    # Acessar o módulo PIM e clicar em Add
    pim_page = PIMPage(logged_in_page)
    pim_page.go_to_pim_module()
    pim_page.click_add_button()

    # Adicionar novo funcionário
    add_employee_page = AddEmployeePage(logged_in_page)
    add_employee_page.add_employee(
        first_name="João",
        middle_name="Silva",
        last_name="Sousa",
        username="joaosousa",
        password="joao123",
        confirm_password="joao123",
        status="Enabled"
    )
