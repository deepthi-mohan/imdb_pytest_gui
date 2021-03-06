from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
import pytest

"""set up and tear down """
""" Initialize drivers"""""


@pytest.fixture(params=["chrome"], scope='function')
# @pytest.fixture(params=["chrome", "firefox"], scope='function')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    if request.param == "internet explorer":
        web_driver = webdriver.Ie(IEDriverManager().install())

    request.cls.driver =web_driver
    web_driver.maximize_window()
    # tear down
    yield
    web_driver.close()

