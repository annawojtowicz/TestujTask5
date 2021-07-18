from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    driver = None

    @staticmethod
    def get_driver() -> WebDriver:
        if Driver.driver is None:
            Driver.driver = webdriver.Chrome(ChromeDriverManager().install())
        return Driver.driver

    @staticmethod
    def go_to_url(url: str):
        if Driver.driver.current_url == url:
            return
        Driver.driver.get(url)

