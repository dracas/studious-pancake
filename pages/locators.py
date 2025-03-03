from selenium.webdriver.common.by import By


class BasePageLocators:
    COMPANY_MENU = (By.XPATH, "//a[contains(text(), 'Company')]")
    COMPANY_CAREER_SUBMENU = (By.XPATH, "//a[contains(text(), 'Careers')]")
    # The Cookies banner buttons:
    ONLY_NECESSARY_BUTTON = (By.CSS_SELECTOR, "#wt-cli-accept-btn.cookie_action_close_header")


class HomePageLocators:
    DESKTOP_HERO_BLOCK = (By.CSS_SELECTOR, "#desktop_hero_24 .container")
    CASE_STUDIES_BLOCK = (By.CSS_SELECTOR, "#case-studies-home .container-fullwidth")


class CareerPageLocators:
    OUR_LOCATIONS_BLOCK = (By.CSS_SELECTOR, "#career-our-location")
    FIND_YOUR_CALLING_BLOCK = (By.CSS_SELECTOR, "#career-find-our-calling")
    LIFE_AT_INSIDER_BLOCK = (By.XPATH, "//section[4]")


class QualityAssurancePageLocators:
    SEE_ALL_QA_JOBS_BUTTON = (By.CSS_SELECTOR, "#page-head .btn")

class OpenPositionsPageLocators:
    # The filter block:
    FILTER_BLOCK = (By.CSS_SELECTOR, "#career-position-filter")

    # Filtering by location:
    FILTER_BY_LOCATION_BTN = (By.CSS_SELECTOR, "#select2-filter-by-location-container")
    FILTER_BY_LOC_ISTANBUL_TURKEY_OPTION = (By.CSS_SELECTOR, "[id~=Turkiye]")

    # Filtering by department:
    FILTER_BY_DEPARTMENT_BTN = (By.CSS_SELECTOR, "#select2-filter-by-department-container")
    FILTER_BY_DEP_QA_OPTION = (By.CSS_SELECTOR, "[id~=Assurance]")

    # The position list block
    POSITION_LIST_BLOCK = (By.CSS_SELECTOR, "#career-position-list")
    LIST_OF_AVAILABLE_POSITIONS = (By.CSS_SELECTOR, "#jobs-list")
    FIRST_AVAILABLE_POSITION = (By.CSS_SELECTOR, "#jobs-list > :nth-child(1)")
    VIEW_ROLE_BUTTON_OF_FIRST_POSITION = (By.CSS_SELECTOR, "#jobs-list > :nth-child(1) .btn")