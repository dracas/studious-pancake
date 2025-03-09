from pages.home_page import HomePage
from pages.career_page import CareerPage


def test_career_page_has_basic_elements(driver):
    page = HomePage(driver)
    page.open()
    page.close_cookie_banner()
    page.main_blocks_should_be_presented()
    page.go_to_career_page()
    career_page = CareerPage(driver)
    career_page.should_be_career_page()