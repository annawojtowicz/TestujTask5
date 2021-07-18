from selenium.webdriver.chrome.webdriver import WebDriver

from Xpaths.xpathssaucedemo import XpathsSauceDemo
from driver import Driver


class TestAddProductAndOrder:
    """
    This test loads webpage of SauceLabs and verifies if browser title is correct
    :param driver:WebDriver instance of Selenium WebDriver
    """
    def test_if_home_page_loads(self, driver: WebDriver):
        driver.get(XpathsSauceDemo.url)
        driver.implicitly_wait(3)
        assert driver.title == 'Swag Labs'

    def test_login_into_swaglabs_and_ordering_product(self, driver: WebDriver):
        """
        This test sorts products from A to Z amd adds 1st product from list to the shopping cart. Then test is making order and checking if correct text is displayed after ordering product
        :param driver:WebDriver instance of Selenium WebDriver
        """
        Driver.go_to_url(XpathsSauceDemo.url)
        username = driver.find_element_by_xpath(XpathsSauceDemo.username)
        username.send_keys(XpathsSauceDemo.standard_user)
        password = driver.find_element_by_xpath(XpathsSauceDemo.password)
        password.send_keys(XpathsSauceDemo.password_input)
        login_button = driver.find_element_by_xpath(XpathsSauceDemo.login_button)
        login_button.click()
        driver.implicitly_wait(3)
        filters = driver.find_element_by_xpath(XpathsSauceDemo.filters)
        filters.click()
        filters_A_to_Z = driver.find_element_by_xpath(XpathsSauceDemo.filters_A_to_Z)
        filters_A_to_Z.click()
        add_to_cart = driver.find_element_by_xpath(XpathsSauceDemo.first_product_on_list)
        add_to_cart.click()
        remove = driver.find_element_by_xpath(XpathsSauceDemo.remove)
        remove.is_displayed()
        cart = driver.find_element_by_xpath(XpathsSauceDemo.cart)
        cart.click()
        product_in_shopping_cart = driver.find_element_by_xpath(XpathsSauceDemo.product_in_shopping_cart)
        product_in_shopping_cart.is_displayed()
        checkout = driver.find_element_by_xpath(XpathsSauceDemo.checkout)
        checkout.click()
        driver.implicitly_wait(1)
        first_name = driver.find_element_by_xpath(XpathsSauceDemo.first_name)
        first_name.send_keys('Qajowy')
        last_name = driver.find_element_by_xpath(XpathsSauceDemo.last_name)
        last_name.send_keys('Tester')
        postal_code = driver.find_element_by_xpath(XpathsSauceDemo.postal_code)
        postal_code.send_keys('12-345')
        continue_button = driver.find_element_by_xpath(XpathsSauceDemo.continue_button)
        continue_button.click()
        driver.implicitly_wait(3)
        finish_button = driver.find_element_by_xpath(XpathsSauceDemo.finish_button)
        finish_button.click()
        driver.implicitly_wait(1)
        successful_order = driver.find_element_by_xpath(XpathsSauceDemo.successfull_order)
        assert successful_order.is_displayed()
