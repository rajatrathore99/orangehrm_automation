from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Updated locators for the new UI
        self.pim_menu = (By.XPATH, "//a[contains(@href, '/pim/viewPimModule')]")
        self.add_employee_button = (By.XPATH, "//a[contains(@href, '/pim/addEmployee')]")

    def navigate_to_pim(self):
        self.wait.until(EC.element_to_be_clickable(self.pim_menu)).click()

    def click_add_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.add_employee_button)).click()
