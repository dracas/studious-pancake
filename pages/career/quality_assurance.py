from pages.career_page import CareerPage
from pages.locators import QualityAssurancePageLocators


class QualityAssurancePage(CareerPage):
    def go_to_open_positions(self):
        self.close_cookie_banner()
        self.driver.find_element(*QualityAssurancePageLocators.SEE_ALL_QA_JOBS_BUTTON).click()