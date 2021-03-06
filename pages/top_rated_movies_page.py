from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import ConfigData
from utils.general import General
"""Class for TopRatedMovies Page"""


class TopRatedMoviesPage(BasePage):

    """Locator details"""
    grdMovieTitle = (By.XPATH, "//tbody[@Class='lister-list']//td[@Class='titleColumn']")
    cmbSortBy = (By.ID, "lister-sort-by-options")
    txtSearch = (By.ID, "suggestion-search")
    btnSearch = (By.XPATH, "//*[@id='suggestion-search-button']")
    grdMovieRating = (By.XPATH, "// tbody[ @ Class = 'lister-list'] // td[ @ Class = 'ratingColumn imdbRating'] // strong")
    btnDescendingOrder = (By.XPATH, "//span[contains(@Class, 'global-sprite lister-sort-reverse')]")
    rbnAddWishList = (By.XPATH, "//tbody[@Class='lister-list']//td[@Class='watchlistColumn']//div[@class='wlb_ribbon']")
    divUserProfile = (By.XPATH, "//*[@id='imdbHeader']//div[@class='ipc-button__text']//span")
    rbnAddWishListDetail = (By.XPATH, "//tbody[@Class='lister-list']//td[@Class='watchlistColumn']//div[@class='wlb_ribbon']//div")

    """constructor of the TopRatedMoviesPage class"""
    """launch IMDB top rated movies page """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ConfigData.BASE_URL)
        self.general = General()
        
    """Actions for TopRatedMoviesPage class"""

    # Get top rated movie list
    # params: None

    def get_movie_list(self):
        list_movie_details = []
        top_rated_movie_chart = self.get_value_from_grid(self.grdMovieTitle)
        for ele in top_rated_movie_chart:
            list_movie_details.append(ele.text)
        return list_movie_details

    # Verify top rated movie list count
    # params: movie list, expected count

    def verify_movie_count(self, movie_list, expected_movie_list_count):
        actual_movie_list_count = len(movie_list)
        assert int(actual_movie_list_count) == int(expected_movie_list_count)

    # Select value in drop down
    # params: drop down value

    def select_value_in_sort_by(self, dropdown_value):
        self.do_send_keys(self.cmbSortBy, dropdown_value)

    # Input value in Search text box
    # params: search text value

    def input_search_imbd_text(self, search_text):
        self.do_send_keys(self.txtSearch, str(search_text))

    # Input value in Search text box
    # params: None

    def click_search_button(self):
        self.do_click(self.btnSearch)

    # Get top rated movie rating list
    # params: None

    def get_movie_rating_list(self):
        list_rating_details = []
        top_rated_movie_ratings = self.get_value_from_grid(self.grdMovieRating)
        for ele in top_rated_movie_ratings:
            list_rating_details.append(ele.text)
        return list_rating_details

    # Verify top rated movie rating list
    # params: rating list
    def verify_movie_rating_list(self, rating_list, order_details):
        expected_list = self.general.sort_list(rating_list, order_details)
        if expected_list == rating_list:
            assert True
        else:
            assert False

    # Click on descending order icon
    # params: None
    def click_descending_order_icon(self):
        self.do_click(self.btnDescendingOrder)

    # Click on add to wish list icon
    # params: None
    def click_wish_list_icon(self):
        self.do_click(self.rbnAddWishList)

    # Verify user profile details
    # params: Profile name
    def verify_profile_name(self, profile_name):
        self.wait_for_page_load(self.divUserProfile)
        user_profile_detail = self.get_value_from_grid(self.divUserProfile)
        profile_detail = user_profile_detail[1].text
        self.general.verify_values(str(profile_detail), str(profile_name))

    # Verify user watch list details
    # params: Profile name
    def verify_watch_list(self, watch_list_count):
        user_profile_detail = self.get_value_from_grid(self.divUserProfile)
        watchlist_detail = user_profile_detail[0].text
        self.general.verify_values(int(watchlist_detail), int(watch_list_count))

    # Verify user watch list added in movie chart
    # params : Watch list details
    def verify_watch_list_added_to_movie(self, actual_wishlist_title):
        watchlist_title = self.get_attribute_value(self.rbnAddWishListDetail, "title")
        self.general.verify_values(str(watchlist_title), str(actual_wishlist_title))




