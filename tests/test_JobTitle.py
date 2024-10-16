from pages.adminPage import AdminPage

def test_AddJobTitle(logged_in_page):
    admin_p = AdminPage(logged_in_page)
    createAndVerifyJobTitle(admin_p)
    #limpando massa pra rodar os outros cenários com sucesso
    admin_p.delete_job_title()
    
def test_DeleteJobTitle(logged_in_page):
    admin_p = AdminPage(logged_in_page)
    createAndVerifyJobTitle(admin_p)
    admin_p.delete_job_title()

def test_EditJobTitle(logged_in_page):
    admin_p = AdminPage(logged_in_page)
    createAndVerifyJobTitle(admin_p)
    admin_p.edit_job_title()

def createAndVerifyJobTitle(admin_p):
    admin_p.access_module("Admin")
    admin_p.load_add_job_title()
    admin_p.fill_job_fields()
    admin_p.verify_job_saved()