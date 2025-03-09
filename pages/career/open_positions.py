import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException

from pages.career_page import CareerPage


class OpenPositionsPage(CareerPage):
    # Locators:
    # The filter block:
    filter_block = (By.CSS_SELECTOR, "#career-position-filter")
    # Filtering by location:
    filter_by_location_btn = (By.CSS_SELECTOR, "#select2-filter-by-location-container")
    filter_by_loc_istanbul_turkey_option = (By.CSS_SELECTOR, "[id~=Turkiye]")
    filter_by_loc_london_united_kingdom_option = (By.CSS_SELECTOR, "[id~=Kingdom]")
    filter_by_loc_paris_france_option = (By.CSS_SELECTOR, "[id~=France]")
    # Filtering by department:
    filter_by_department_btn = (By.CSS_SELECTOR, "#select2-filter-by-department-container")
    filter_by_depart_qa_option = (By.CSS_SELECTOR, "[id~=Assurance]")
    filter_by_depart_design_option = (By.CSS_SELECTOR, "[id~ = Design]")
    # The position list block
    position_list_block = (By.CSS_SELECTOR, "#career-position-list")
    list_of_available_positions = (By.CSS_SELECTOR, "#jobs-list")
    first_available_position = (By.CSS_SELECTOR, "#jobs-list > :nth-child(1)")
    view_role_button_of_first_position = (By.CSS_SELECTOR, "#jobs-list > :nth-child(1) .btn")


    def should_be_open_position_page(self):
        self.should_be_career_url()

        missing_blocks = [
            name for locator, name in [
                (self.filter_block, "Filters"),
                (self.position_list_block, "Position list")
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

    def apply_location_filter(self, location):
        available_locations = ['istanbul_turkey', 'london_united_kingdom', 'paris_france']

        if location.lower() not in available_locations:
            raise ValueError(
                f"Location '{location}' is not valid. Available locations are: {', '.join(available_locations)}")
        else:
            location_locator = f'filter_by_loc_{location.lower()}_option'
            locator = getattr(self, location_locator)
            self.apply_filter_option(self.filter_by_location_btn, locator)

    def apply_department_filter(self, department):
        available_departments = ['qa', 'design']

        if department.lower() not in available_departments:
            raise ValueError(
                f"Department '{department}' is not valid. Available departments are: {', '.join(available_departments)}")
        else:
            department_locator = f'filter_by_depart_{department.lower()}_option'
            locator = getattr(self, department_locator)
            self.apply_filter_option(self.filter_by_department_btn, locator)

    def check_elements_have_attribute(self, attribute, attribute_value):
        number_of_positions = len(self.driver.find_elements(*self.list_of_available_positions))

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
            element = self.driver.find_element(*self.first_available_position)
            actions.move_to_element(element).perform()

            # Clicks the View role button
            wait = WebDriverWait(self.driver, timeout=2)
            view_role_button = wait.until(EC.element_to_be_clickable(self.view_role_button_of_first_position))
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