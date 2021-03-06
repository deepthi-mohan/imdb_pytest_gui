from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.general import General
"""Class for SignInPage Page"""


class IMDBSignInPage(BasePage):

    """Locators of IMDBSignInPage """

    txtUserEmail = (By.ID, "ap_email")
    txtPassword = (By.ID, "ap_password")
    btnSignIn = (By.ID, "signInSubmit")
    lnkForgotSignIn = (By.ID, "auth-fpp-link-bottom")

    """constructor of the TopRatedMoviesPage class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.general = General()
        self.get_title("IMDb Sign-In")

    # Enter user name
    # params: user name
    def enter_user_email(self, user_name):
        self.do_send_keys(self.txtUserEmail, user_name)

    # Enter password
    # params: password
    def enter_user_password(self, password):
        self.do_send_keys(self.txtPassword, password)

    # Click Sign In button
    # params:None
    def click_sign_in_button(self):
        self.do_click(self.btnSignIn)

    # Input Sign In details and click button
    # params: user name, password
    def enter_user_details_and_sign_in(self, user_name, password):
        self.enter_user_email(user_name)
        self.enter_user_password(password)
        self.click_sign_in_button()
