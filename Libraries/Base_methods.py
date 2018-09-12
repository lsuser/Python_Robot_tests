from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import Driver


class Base_methods():
    ROBOT_LIBRARY_SCOPE = 'TEST_SUITE'
    __version__ = '0.1'

    def get_driver(self):
        driver = BuiltIn().get_variable_value('${BROWSER}')
        return driver

    def Go_To_Url(self, url):
        Driver.Instance.get(url)
        BuiltIn().log('Url: {0} is opened'.format(url), console=True)

    def Fill_In_Field(self, locator, text):
        driver = BuiltIn().get_variable_value('${BROWSER}')
        try:
            element = driver.find_element_by_css_selector(locator)
        except InvalidSelectorException:
            element = driver.find_element_by_xpath(locator)
        finally:
            element.clear()
            element.send_keys(text)
            BuiltIn().log("{0} inputed in a field".format(text), console=True)

    def Click_Button(self, locator):
        driver = BuiltIn().get_variable_value('${BROWSER}')
        try:
            element = driver.find_element_by_css_selector(locator)
        except InvalidSelectorException:
            element = driver.find_element_by_xpath(locator)
        finally:
            element.click()
            BuiltIn().log("{0} element was clicked".format(locator), console=True)

    def Verify_Data(self, locator, text):
        ltext = None
        driver = BuiltIn().get_variable_value('${BROWSER}')
        try:
            element = driver.find_element_by_css_selector(locator)
            ltext = element.get_attribute('value')
        except InvalidSelectorException:
            element = driver.find_element_by_xpath(locator)
            ltext = element.get_attribute('value')
        finally:
            if ltext == text:
                BuiltIn().log('Correct data - {0}'.format(ltext))
            else:
                BuiltIn().fail('ERROR : Incorrect data -  {0}'.format(ltext))

    def get_url(self):
        driver = BuiltIn().get_variable_value('${BROWSER}')
        url = driver.current_url
        BuiltIn().log('User was redirected to {0}'.format(url))
        return url

    # need to work on it
    def switch_to_popup(self, locator, text):
        driver = BuiltIn().get_variable_value('${BROWSER}')
        try:
            wait = WebDriverWait(driver, 100)
            wait.until(EC.text_to_be_present_in_element(locator, text))
            # wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, locator)))
            BuiltIn().log('switch to {0}'.format(locator), console=True)
            element = driver.find_element_by_css_selector(locator)
            text = element.get_text()
            BuiltIn().log('text on the pop-up {0}'.format(text), console=True)
        except InvalidSelectorException:
            BuiltIn().fail("Can't find the element")
        except TimeoutException, e:
            BuiltIn().fail('No pop-up on the page {0}'.format(e))
        finally:
            BuiltIn().log('Take a screenshot', console=True)
            driver.save_screenshot("screenshot_popup.png")

    # need to work on it
    def get_text_in_message(self, locator):
        driver = BuiltIn().get_variable_value('${BROWSER}')
        element = driver.find_element_by_css_selector(locator)
        text = element.text
        BuiltIn().log('The message after registration - {0}'.format(text), console=True)
        return text
