import time

import pytest

from pages.career.open_positions import OpenPositionsPage
from config.config import OPEN_POSITIONS_PAGE_URL
from pages.locators import OpenPositionsPageLocators


@pytest.mark.unstable_case # This test case is unstable due to problems with displaying positions after filtering
def test_filtering_by_location_and_department(driver):
    page = OpenPositionsPage(driver)
    page.open(OPEN_POSITIONS_PAGE_URL)
    page.close_cookie_banner()
    page.should_be_open_position_page()
    page.apply_filter_option(OpenPositionsPageLocators.FILTER_BY_LOCATION_BTN,
                             OpenPositionsPageLocators.FILTER_BY_LOC_ISTANBUL_TURKEY_OPTION)
    time.sleep(5)  # TODO: Necessary due to problems with displaying positions after filters are applied
    page.apply_filter_option(OpenPositionsPageLocators.FILTER_BY_DEPARTMENT_BTN,
                             OpenPositionsPageLocators.FILTER_BY_DEP_QA_OPTION, 1)
    time.sleep(5) #TODO: Necessary due to problems with displaying positions after filters are applied
    page.check_elements_have_attribute('data-location', 'istanbul-turkiye')
    page.check_elements_have_attribute('data-team', 'qualityassurance')
    page.check_view_role_button()