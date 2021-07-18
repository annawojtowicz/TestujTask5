from selenium.webdriver.chrome.webdriver import WebDriver


import random
import string

from Xpaths.XpathsExerciseFive import XpathsExerciseFive
from driver import Driver


class TestExerciseFive:
    def test_if_page_loads(self, driver: WebDriver):
        """
        This test loads webpage of ParaBank and verifies if browser title is correct
        :param driver:WebDriver instance of Selenium WebDriver
        """
        driver.get(XpathsExerciseFive.url)
        driver.implicitly_wait(3)
        assert driver.title == 'ParaBank | Register for Free Online Account Access'

    def test_registration(self, driver: WebDriver):
        """
        This test fills register form and registers user. After that test is checking is user is logged in.
        Test uses random strig as a user's login in order to enable multiple test runs
        :param driver:WebDriver instance of Selenium WebDriver
        """
        Driver.go_to_url(XpathsExerciseFive.url)
        result_str = ''.join(random.sample(string.ascii_lowercase, 8))
        username = 'QA'
        lastname = 'Test'
        address_input = 'Far Far Away'
        city_input = 'Over the 7 hills'
        state_input = 'the mountain garden'
        zipcode_input = '12-345'
        phone_input = '123456789'
        ssn_input = '000-00-0000'
        userlogin = result_str
        password_input = 'fiona'
        first_name = driver.find_element_by_xpath(XpathsExerciseFive.first_name)
        first_name.send_keys(username)
        last_name = driver.find_element_by_xpath(XpathsExerciseFive.last_name)
        last_name.send_keys(lastname)
        address = driver.find_element_by_xpath(XpathsExerciseFive.address)
        address.send_keys(address_input)
        city = driver.find_element_by_xpath(XpathsExerciseFive.city)
        city.send_keys(city_input)
        state = driver.find_element_by_xpath(XpathsExerciseFive.state)
        state.send_keys(state_input)
        zipcode = driver.find_element_by_xpath(XpathsExerciseFive.zipcode)
        zipcode.send_keys(zipcode_input)
        phone = driver.find_element_by_xpath(XpathsExerciseFive.phone)
        phone.send_keys(phone_input)
        ssn = driver.find_element_by_xpath(XpathsExerciseFive.ssn)
        ssn.send_keys(ssn_input)
        username = driver.find_element_by_xpath(XpathsExerciseFive.username)
        username.send_keys(userlogin)
        password = driver.find_element_by_xpath(XpathsExerciseFive.password)
        password.send_keys(password_input)
        confirm = driver.find_element_by_xpath(XpathsExerciseFive.confirm_password)
        confirm.send_keys(password_input)
        register = driver.find_element_by_xpath(XpathsExerciseFive.submit_button)
        register.click()
        driver.implicitly_wait(3)
        success = driver.find_element_by_xpath(XpathsExerciseFive.success)
        assert success.is_displayed()

