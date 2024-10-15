from pages.buzzPage import BuzzPage

def test_post(logged_in_page):
	buzz_p = BuzzPage(logged_in_page)
	buzz_p.access_module("Buzz")
	buzz_p.create_post()
	buzz_p.test_like_post()
	buzz_p.delete_post()