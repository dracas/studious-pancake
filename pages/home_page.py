from .base_page import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):
    def main_blocks_should_be_presented(self):
        assert all([
            self.is_element_visible(HomePageLocators.DESKTOP_HERO_BLOCK),
            self.is_element_visible(HomePageLocators.CASE_STUDIES_BLOCK)
        ]), "Not all main blocks are visible on the Home page"