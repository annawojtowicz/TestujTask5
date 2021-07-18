from selenium.webdriver.chrome.webdriver import WebDriver

from Xpaths.xpathssaucedemo import XpathsSauceDemo
from driver import Driver


class TestLockedUser:
    def test_if_home_page_loads(self, driver: WebDriver):
        """
        This test loads webpage of SauceLabs and verifies if browser title is correct
        :param driver:WebDriver instance of Selenium WebDriver
        """
        driver.get(XpathsSauceDemo.url)
        driver.implicitly_wait(3)
        assert driver.title == 'Swag Labs'

    def test_login_into_swaglabs(self, driver: WebDriver):
        """
        This test checks if error appears for locked user
        :param driver:WebDriver instance of Selenium WebDriver
        """
        Driver.go_to_url(XpathsSauceDemo.url)
        username = driver.find_element_by_xpath(XpathsSauceDemo.username)
        username.send_keys(XpathsSauceDemo.locked_out_user)
        password = driver.find_element_by_xpath(XpathsSauceDemo.password)
        password.send_keys(XpathsSauceDemo.password_input)
        login_button = driver.find_element_by_xpath(XpathsSauceDemo.login_button)
        login_button.click()
        assert driver.current_url == XpathsSauceDemo.url
        error = driver.find_element_by_xpath(XpathsSauceDemo.error)
        assert error.is_displayed()
