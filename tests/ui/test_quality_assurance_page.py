from pages.career.quality_assurance import QualityAssurancePage
from pages.career.open_positions import OpenPositionsPage
from config.config import QUALITY_ASSURANCE_PAGE_URL


def test_navigation_to_open_positions_from_qa_page(driver):
    page = QualityAssurancePage(driver)
    page.open(QUALITY_ASSURANCE_PAGE_URL)
    page.go_to_open_positions()
    open_positions_page = OpenPositionsPage(driver)
    open_positions_page.should_be_open_position_page()