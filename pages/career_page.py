from selenium.webdriver.common.by import By

from .base_page import BasePage


class CareerPage(BasePage):
    # Locators:
    our_locations_block = (By.CSS_SELECTOR, "#career-our-location")
    find_your_calling_block = (By.CSS_SELECTOR, "#career-find-our-calling")
    life_at_insider_block = (By.XPATH, "//section[4]")


    def should_be_career_page(self):
        self.should_be_career_url()

        missing_blocks = [
            name for locator, name in [
                (self.our_locations_block, "Our Locations"),
                (self.find_your_calling_block, "Find Your Calling"),
                (self.life_at_insider_block, "Life at Insider")
            ] if not self.is_element_visible(locator)
        ]

        assert not missing_blocks, f"The following blocks are missing or not visible: {', '.join(missing_blocks)}"


    def should_be_career_url(self):
        current_page_url = self.driver.current_url
        assert 'careers' in current_page_url, "Substring 'careers' is missing in the current URL"
