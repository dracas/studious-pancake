import time

import pytest

from pages.career.open_positions import OpenPositionsPage
from config.config import OPEN_POSITIONS_PAGE_URL


@pytest.mark.unstable_case # This test case is unstable due to problems with displaying positions after filtering
def test_filtering_by_location_and_department(driver):
    page = OpenPositionsPage(driver)
    page.open(OPEN_POSITIONS_PAGE_URL)
    page.close_cookie_banner()
    page.should_be_open_position_page()
    page.apply_location_filter('istanbul_turkey')
    time.sleep(5)  # TODO: Necessary due to problems with displaying positions after filters are applied
    page.apply_department_filter('qa')
    time.sleep(5) #TODO: Necessary due to problems with displaying positions after filters are applied
    page.check_elements_have_attribute('data-location', 'istanbul-turkiye')
    page.check_elements_have_attribute('data-team', 'qualityassurance')
    page.check_view_role_button()