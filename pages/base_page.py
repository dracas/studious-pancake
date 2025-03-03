from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config.config import UI_BASE_URL
from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url=UI_BASE_URL):
        self.driver.get(url)

    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def navigate_to_under_header_page(self, menu_locator, submenu_locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)

        menu_element = wait.until(EC.element_to_be_clickable(menu_locator))
        menu_element.click()

        submenu_element = wait.until(EC.element_to_be_clickable(submenu_locator))
        submenu_element.click()

    def close_cookie_banner(self):
        try:
            cookie_close_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(BasePageLocators.ONLY_NECESSARY_BUTTON)
            )
            cookie_close_button.click()
        except TimeoutException:
            pass
