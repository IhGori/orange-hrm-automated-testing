from pages.modules.recruitment.recruitmentPage import RecruitmentPage

def test_create_vacancy(logged_in_page):
	vacancies_p = RecruitmentPage(logged_in_page)
	vacancies_p.access_module()
	vacancies_p.access_vacancies()