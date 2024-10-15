from pages.adminPage import AdminPage

def test_JobTitle(logged_in_page):
    admin_p = AdminPage(logged_in_page)
    admin_p.access_module("Admin")
    admin_p.load_add_job_title()
    admin_p.fill_job_fields()
    admin_p.verify_job_saved()