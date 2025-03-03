from pages.home_page import HomePage
from pages.career_page import CareerPage
from pages.locators import BasePageLocators


def test_career_page_has_basic_elements(driver):
    page = HomePage(driver)
    page.open()
    page.close_cookie_banner()
    page.main_blocks_should_be_presented()
    page.navigate_to_under_header_page(BasePageLocators.COMPANY_MENU, BasePageLocators.COMPANY_CAREER_SUBMENU)
    career_page = CareerPage(driver)
    career_page.should_be_career_page()