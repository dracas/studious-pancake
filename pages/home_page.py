from selenium.webdriver.common.by import By

from .base_page import BasePage


class HomePage(BasePage):
    # Locators:
    desktop_hero_block = (By.CSS_SELECTOR, "#desktop_hero_24 .container")
    case_studies_block = (By.CSS_SELECTOR, "#case-studies-home .container-fullwidth")


    def main_blocks_should_be_presented(self):
        assert all([
            self.is_element_visible(self.desktop_hero_block),
            self.is_element_visible(self.case_studies_block)
        ]), "Not all main blocks are visible on the Home page"