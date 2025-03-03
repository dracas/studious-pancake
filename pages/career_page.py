from .base_page import BasePage
from .locators import CareerPageLocators


class CareerPage(BasePage):
    def should_be_career_page(self):
        self.should_be_career_url()

        missing_blocks = [
            name for locator, name in [
                (CareerPageLocators.OUR_LOCATIONS_BLOCK, "Our Locations"),
                (CareerPageLocators.FIND_YOUR_CALLING_BLOCK, "Find Your Calling"),
                (CareerPageLocators.LIFE_AT_INSIDER_BLOCK, "Life at Insider")
            ] if not self.is_element_visible(locator)
        ]

        assert not missing_blocks, f"The following blocks are missing or not visible: {', '.join(missing_blocks)}"


    def should_be_career_url(self):
        current_page_url = self.driver.current_url
        assert 'careers' in current_page_url, "Substring 'careers' is missing in the current URL"
