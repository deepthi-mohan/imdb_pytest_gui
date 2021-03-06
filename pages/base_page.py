
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""This class is the parent of all the pages """
"""This class contains all the generic methods and utilities for all the pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Click on an element
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).click()

    # Input text
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # Get text of an element
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return element.text

    # Verify element is visible
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of(by_locator))
        return bool(element)

    # Get title of an element
    def get_title(self, title):
        WebDriverWait(self.driver, 30).until(EC.title_is(title))
        return self.driver.title

    # Find elements
    def get_value_from_grid(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(by_locator))
        return element

    # Get attribute value
    def get_attribute_value(self, by_locator, attribute):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        attribute_value = element.get_attribute(attribute)
        return attribute_value

    # Wait of page load
    def wait_for_page_load(self, by_locator):
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(by_locator))

