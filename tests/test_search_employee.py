# tests/test_search_employee.py
import pytest
from selenium import webdriver
from pages.loginPage import LoginPage
from pages.pimPage import PIMPage

@pytest.fixture
def driver():
    # Configuração do driver (pode ser Chrome, Firefox, etc.)
    driver = webdriver.Chrome()  # Ou outro driver de sua escolha
    driver.implicitly_wait(10)  # Espera implícita para elementos
    yield driver
    driver.quit()

def test_search_employee(logged_in_page):
    # Acessar o site
    # Login no sistema
    login_p = LoginPage(logged_in_page)
    login_p.login()  # Agora o método aceita os parâmetros
    login_p.assert_url()

    # Navegar até o módulo PIM
    pim_page = PIMPage(driver)
    pim_page.go_to_pim_module()  # Você precisará implementar isso se necessário

    # Pesquisar funcionário
    employee_name = "John Doe"  # Substitua pelo nome que deseja pesquisar
    pim_page.search_employee(employee_name)

    # Verificar se o registro do funcionário é exibido
    assert pim_page.is_employee_record_displayed(), "Registro do funcionário não foi encontrado."
