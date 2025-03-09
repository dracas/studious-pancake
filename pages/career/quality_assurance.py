from selenium.webdriver.common.by import By

from pages.career_page import CareerPage


class QualityAssurancePage(CareerPage):
    # Locators:
    see_all_qa_jobs_button = (By.CSS_SELECTOR, "#page-head .btn")


    def go_to_open_positions(self):
        self.close_cookie_banner()
        self.driver.find_element(*self.see_all_qa_jobs_button).click()