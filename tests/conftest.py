from selenium import webdriver
from config.config import ConfigData
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
import pytest

"""set up and tear down """


@pytest.fixture(params=["chrome"], scope='function')
# @pytest.fixture(params=["firefox"], scope='function')
# @pytest.fixture(params=["internet explorer"], scope='function')
# @pytest.fixture(params=["edge"], scope='function')
# @pytest.fixture(params=["chrome", "firefox"], scope= 'class')
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

