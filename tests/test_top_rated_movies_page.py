import pytest
from tests.test_base import BaseTest
from pages.top_rated_movies_page import TopRatedMoviesPage
from pages.movie_detail_page import MovieDetailPage
from config.config import ConfigData
from pages.find_page import FindIMDB
"""Test Class for MovieDetail Page"""


class TestTopRatedMoviesPage(BaseTest):

    # Test scenario: Verify the movie chart has 250 movies in it and Sort by functionality
    def test_top_rated_movies_imdb_page(self):
        # self.excel = Excel()
        # movie_list = self.excel.read_row_data("signIn")
        # print(movie_list[2])
        # print(movie_list[3])
        movie_list = ['tc0001', 'itsmedeepthy@gmail.com', 'p@ssw0rd', 'IMDB', 'IMDb Rating', 'The Godfather', 250, 'IMDb Top 250 - IMDb']

        # Get movie details in top rate movie page and verify count
        self.top_rated_movies_page = TopRatedMoviesPage(self.driver)
        list_movie_details = self.top_rated_movies_page.get_movie_list()
        self.top_rated_movies_page.verify_movie_count(list_movie_details, movie_list[6])

        # Select and verify Sort By using "IMDb Rating" and verify rating list and count
        self.top_rated_movies_page.select_value_in_sort_by(movie_list[4])
        list_movie_ratings = self.top_rated_movies_page.get_movie_rating_list()
        self.top_rated_movies_page.verify_movie_rating_list(list_movie_ratings, True)
        self.top_rated_movies_page.verify_movie_count(list_movie_ratings, movie_list[6])
        # Click Descending Order button and verify rating list and count
        self.top_rated_movies_page.click_descending_order_icon()
        list_movie_ratings = self.top_rated_movies_page.get_movie_rating_list()
        self.top_rated_movies_page.verify_movie_rating_list(list_movie_ratings, False)
        self.top_rated_movies_page.verify_movie_count(list_movie_ratings, movie_list[6])

    # Test Scenario: Verify Search in IMDB web page.
    def test_search_in_imdb_page(self):
        test_data = ['tc0001', 'itsmedeepthy@gmail.com', 'p@ssw0rd', 'IMDB', 'Release Date', 'The Dark Knight', 250.0, 'IMDb Top 250 - IMDb']
        search_text = test_data[5]
        page_title = test_data[7]
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





