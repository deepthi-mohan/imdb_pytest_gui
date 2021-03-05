from selenium import webdriver
from config.config import ConfigData
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

"""set up and tear down """


#@pytest.fixture(params=["chrome"], scope= 'class')
@pytest.fixture(params=["chrome", "firefox"], scope= 'class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver =web_driver

    # tear down
    yield
    web_driver.close()

