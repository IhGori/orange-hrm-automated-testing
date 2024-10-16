# tests/test_delete_employee.py
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

def test_delete_employee(logged_in_page):
    # Acessar o site  
    # Login no sistema
    login_p = LoginPage(logged_in_page)
    login_p.login()  # Agora o método aceita os parâmetros
    login_p.assert_url()

    # Navegar até o módulo PIM
    pim_page = PIMPage(driver)
    
    # Acessar a lista de funcionários (você pode precisar implementar isso se necessário)
    # Supondo que você já está na lista de funcionários após o login

    # Clicar no ícone de exclusão do primeiro registro da lista
    pim_page.delete_employee()

    # Verificar se o modal de confirmação é exibido
    assert pim_page.is_confirmation_modal_displayed(), "Modal de confirmação não foi exibido."

    # Confirmar a exclusão
    pim_page.confirm_delete()

    # Verificar se a exclusão foi bem-sucedida
    # (Isso pode ser feito verificando se o registro não está mais na lista)

