import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from driver import Driver


@pytest.fixture(scope="session", autouse=True)
def driver() -> WebDriver:
    driver = Driver.get_driver()

    try:
        yield driver
    finally:
        driver.close()
