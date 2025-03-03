import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException

from pages.career_page import CareerPage
from pages.locators import OpenPositionsPageLocators


class OpenPositionsPage(CareerPage):
    def should_be_open_position_page(self):
        self.should_be_career_url()

        missing_blocks = [
            name for locator, name in [
                (OpenPositionsPageLocators.FILTER_BLOCK, "Filters"),
                (OpenPositionsPageLocators.POSITION_LIST_BLOCK, "Position list")
            ] if not self.is_element_visible(locator)
        ]

        assert not missing_blocks, f"The following blocks are missing or not visible: {', '.join(missing_blocks)}"

    def should_be_open_position_url(self):
        current_page_url = self.driver.current_url
        assert 'open-positions' in current_page_url, "Substring 'open-positions' is missing in the current URL"

    def apply_filter_option(self, filter_by, selected_option, sleep_period=5):
        time.sleep(sleep_period) #TODO: Change to more effective approach
        self.driver.find_element(*filter_by).click()
        self.driver.find_element(*selected_option).click()

    def check_elements_have_attribute(self, attribute, attribute_value):
        number_of_positions = len(self.driver.find_elements(*OpenPositionsPageLocators.LIST_OF_AVAILABLE_POSITIONS))

        list_of_elements_without_attribute = list()
        for i in range(1, number_of_positions + 1):
            # TODO: Find a way to use the variable instead of the direct selector
            element = self.driver.find_element(By.CSS_SELECTOR, f"#jobs-list > :nth-child({i})")

            if element.get_attribute(attribute) != attribute_value:
                list_of_elements_without_attribute.append(f"#jobs-list > :nth-child({i})")

        if len(list_of_elements_without_attribute) > 0:
            raise ValueError(
                f"Some elements are missing the '{attribute_value}' value in the {attribute} attribute, "
                f"the elements's selectors: {list_of_elements_without_attribute}"
            )

    def check_view_role_button(self):
        if len(self.driver.window_handles) == 1:
            # Hovers the first available position
            actions = ActionChains(self.driver)
            element = self.driver.find_element(*OpenPositionsPageLocators.FIRST_AVAILABLE_POSITION)
            actions.move_to_element(element).perform()

            # Clicks the View role button
            wait = WebDriverWait(self.driver, timeout=2)
            view_role_button = wait.until(EC.element_to_be_clickable(OpenPositionsPageLocators.VIEW_ROLE_BUTTON_OF_FIRST_POSITION))
            view_role_button.click()

            # Switches to the newly opened tab
            try:
                self.driver.switch_to.window(self.driver.window_handles[-1])
                current_page_url = self.driver.current_url
                assert '/useinsider/' in current_page_url, "Substring '/useinsider/' is missing in the current URL"
            except NoSuchWindowException:
                raise NoSuchWindowException("The new tab could not be found or switched to.")
        else:
            raise AssertionError("The number of open tabs is not equal to 1.")