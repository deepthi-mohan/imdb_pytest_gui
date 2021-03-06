import pytest
from tests.test_base import BaseTest
from pages.top_rated_movies_page import TopRatedMoviesPage
from config.config import ConfigData
from pages.find_page import FindIMDB
from utils.excel import Excel
from pages.signin_page import SignInPage
from pages.imdb_signin_page import IMDBSignInPage

"""Test Class for TestTopRatedMovies Page"""


class TestTopRatedMoviesPage(BaseTest):

    # Test scenario: Verify the movie chart has 250 movies in it and Sort by functionality
    def test_top_rated_movies_imdb_page(self):
        self.excel = Excel()
        self.config_data = ConfigData()

        # get test data
        movie_list = self.excel.read_test_data(self.config_data.SHEET_NAME)
        search_sort_by = movie_list[0][4]
        movie_count = movie_list[0][6]

        # Get movie details in top rate movie page and verify count
        self.top_rated_movies_page = TopRatedMoviesPage(self.driver)
        list_movie_details = self.top_rated_movies_page.get_movie_list()
        self.top_rated_movies_page.verify_movie_count(list_movie_details, movie_count)

        # Select and verify Sort By using "IMDb Rating" and verify rating list and count
        self.top_rated_movies_page.select_value_in_sort_by(search_sort_by)
        list_movie_ratings = self.top_rated_movies_page.get_movie_rating_list()
        self.top_rated_movies_page.verify_movie_rating_list(list_movie_ratings, True)
        self.top_rated_movies_page.verify_movie_count(list_movie_ratings, movie_count)

        # Click Descending Order button and verify rating list and count
        self.top_rated_movies_page.click_descending_order_icon()
        list_movie_ratings = self.top_rated_movies_page.get_movie_rating_list()
        self.top_rated_movies_page.verify_movie_rating_list(list_movie_ratings, False)
        self.top_rated_movies_page.verify_movie_count(list_movie_ratings, movie_count)

    # Test Scenario: Verify Search in IMDB web page and navigate back to home page
    def test_search_in_imdb_page(self):
        self.excel = Excel()
        self.config_data = ConfigData()

        # get test data
        test_data = self.excel.read_test_data(self.config_data.SHEET_NAME)
        search_text = test_data[1][5]
        page_title = test_data[1][7]

        # Search value in TopRatedMoviesPage
        self.top_rated_movies_page = TopRatedMoviesPage(self.driver)
        self.top_rated_movies_page.input_search_imbd_text(search_text)
        self.top_rated_movies_page.click_search_button()

        # Verify search
        self.find_imdb = FindIMDB(self.driver)
        self.find_imdb.verify_search_result_label(search_text)
        search_result = self.find_imdb.get_search_result_links()
        self.find_imdb.verify_search_result_links_text(search_text, search_result)

        # Navigate back to TopRatedMoviesPage and verify
        self.find_imdb.verify_navigate_back(page_title)

    # Test Scenario: Verify Wish list before and after user signed in
    def test_add_to_watch_list_in_imdb_page(self):
        self.excel = Excel()
        self.config_data = ConfigData()

        # get data from excel
        data_list = self.excel.read_test_data(self.config_data.SHEET_NAME)
        user_name = data_list[2][1]
        password = data_list[2][2]

        profile_name_after_sign_in = data_list[2][8]
        watch_list_count = data_list[2][9]
        watch_list_title_before_adding = data_list[2][10]
        watch_list_title_after_adding = data_list[2][11]

        # Verify sign in and wish list when user is not authenticated or not signed in
        self.top_rated_movies_page = TopRatedMoviesPage(self.driver)
        self.top_rated_movies_page.verify_watch_list_added_to_movie(watch_list_title_before_adding)
        self.top_rated_movies_page.click_wish_list_icon()

        # Sign in with valid user
        # Sign in using IMDB sign in
        self.sign_in_page = SignInPage(self.driver)
        self.sign_in_page.click_sign_in_with_imdb()
        self.imdb_sign_in_page = IMDBSignInPage(self.driver)
        self.imdb_sign_in_page.enter_user_details_and_sign_in(user_name, password)

        # Verify Top rated Movies page after user sign in
        # Verify User name and Watch list details
        self.top_rated_movies_pages = TopRatedMoviesPage(self.driver)
        self.top_rated_movies_pages.verify_profile_name(profile_name_after_sign_in)
        self.top_rated_movies_pages.verify_watch_list(watch_list_count)
        self.top_rated_movies_pages.verify_watch_list_added_to_movie(watch_list_title_after_adding)











