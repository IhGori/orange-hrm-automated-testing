from pages.modules.recruitment.recruitmentPage import RecruitmentPage

def test_vacancy(logged_in_page):
	vacancies_p = RecruitmentPage(logged_in_page)
	vacancies_p.access_module()
	vacancy_name = vacancies_p.test_create_vacancy()
	vacancies_p.test_apply_for_the_vacancy(vacancy_name)
	vacancies_p.test_filter_vacancy(vacancy_name)