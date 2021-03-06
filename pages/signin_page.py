from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.general import General
"""Class for SignInPage Page"""


class SignInPage(BasePage):

    """locator details"""
    spnSignInWithIMDB1 = (By.XPATH, "//span[@class='auth-sprite imdb-logo retina']")
    spnSignInWithIMDB = (By.XPATH, "//div[@class='list-group']//span[2]")

    """constructor of the Sign In page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.general = General()
        self.get_title("Sign in with IMDb - IMDb")

    """Actions in the Sign In Page"""

    # Click sign in with IMDB
    # params: None
    def click_sign_in_with_imdb(self):
        self.do_click(self.spnSignInWithIMDB)

