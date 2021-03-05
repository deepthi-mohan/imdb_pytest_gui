import pytest

"""This class is the parent of all the tests """
"""This uses fixture init_driver"""


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
