from selenium.webdriver.chrome.webdriver import WebDriver

from Xpaths.XpathsExerciseFour import XpathsExcerciseFour
from driver import Driver


class TestExerciseFour:
    def test_if_home_page_loads(self, driver: WebDriver):
        """
                This test loads webpage of WebDriverUniversity and verifies if browser title is correct
                :param driver:WebDriver instance of Selenium WebDriver
                """
        driver.get(XpathsExcerciseFour.url)
        driver.implicitly_wait(3)
        assert driver.title == 'WebDriverUniversity.com'

    def test_contact_us(self, driver: WebDriver):
        """
        This test loads contact form and sends comment; after that test verifies if comment have been successfully sent
        :param driver:WebDriver instance of Selenium WebDriver
        """
        Driver.go_to_url(XpathsExcerciseFour.url)
        contact_us = driver.find_element_by_xpath(XpathsExcerciseFour.contact_us)
        contact_us.click()
        driver.implicitly_wait(3)

        form_window = driver.window_handles[-1]
        driver.switch_to.window(form_window)

        first_name = driver.find_element_by_xpath(XpathsExcerciseFour.first_name)
        first_name.send_keys(XpathsExcerciseFour.first_name_input)
        last_name = driver.find_element_by_xpath(XpathsExcerciseFour.last_name)
        last_name.send_keys(XpathsExcerciseFour.last_name_input)
        email = driver.find_element_by_xpath(XpathsExcerciseFour.email)
        email.send_keys(XpathsExcerciseFour.email_input)
        comment = driver.find_element_by_xpath(XpathsExcerciseFour.textarea)
        comment.send_keys(XpathsExcerciseFour.textarea_input)
        submit = driver.find_element_by_xpath(XpathsExcerciseFour.submit)
        submit.click()
        driver.implicitly_wait(3)
        success = driver.find_element_by_xpath(XpathsExcerciseFour.success)
        assert success.is_displayed()
