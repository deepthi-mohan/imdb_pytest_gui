from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.general import General
import time
"""Class for FindIMDB Page"""


class FindIMDB(BasePage):

    """Locators of the Find page"""
    lblSearchResult = (By.XPATH, "//span[@class= 'findSearchTerm']")
    lnkSearchResults = (By.XPATH, "//div[@class='findSection']//table[@class='findList']//td[@class='result_text']//a[contains(@href, 'title')]")

    """constructor of the FindIMDB class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.general = General()
        self.get_title("Find - IMDb")

    # Get Search result label value
    # params: None
    def get_search_result(self):
        search_result_label = self.get_element_text(self.lblSearchResult)
        return search_result_label

    # Get Search result label value
    # params: expected search result
    def verify_search_result_label(self, expected_search_result_label):
        actual_search_result_label = self.get_search_result()
        actual_search_result_label = self.general.strip_string_value(actual_search_result_label, '"')
        assert actual_search_result_label == expected_search_result_label, "Actual search label and expected label is not same as expected"

    # get Search result links
    # params: None
    def get_search_result_links(self):
        search_links = self.get_value_from_grid(self.lnkSearchResults)
        search_result_list = []
        for element in search_links:
            search_result_list.append(element.text)
        return search_result_list

    # verify text in Search result links
    # params: search text, list
    def verify_search_result_links_text(self, expected_text, search_result_list):
        self.general.verify_list_values(search_result_list, expected_text)

    # verify navigate back page
    # params: expected title of page
    def verify_navigate_back(self, expected_title):
        self.driver.back()
        time.sleep(10)
        actual_title = self.driver.title
        assert actual_title == expected_title, "Actual and expected title values does not match"


