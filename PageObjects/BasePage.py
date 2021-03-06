from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


class BasePage:
    def __init__(self, app):
        self.app = app

    def open_page(self, url: str):
        self.app.driver.get(url)

    def _find_element(self, locator, wait_time=10):
        """
        Find element. Explicit wait using
        :param locator: locator like (BY.ID, 'name')
        :param wait_time: waiting time
        :return:
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def clear(self, locator, wait_time=10) -> None:
        """
        Clear to field
        :param locator : locator(*locator, name)
        :param wait_time: waiting time
        """
        element = self._find_element(locator, wait_time)
        element.clear()

    def find_all_elements(self, locator) -> list:
        """
        Find element. Explicit wait using
        :param locator: locator like (BY.ID, 'name')
        :return list all elements have this locator
        """
        return self.app.driver.find_elements(*locator)

    def fill(self, locator, value, wait_time=10) -> None:
        """
        Fill element == send_keys
        :param locator: locator(*locator,name)
        :param value: sting to fill
        :param wait_time: waiting time
        """
        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def search_element_and_click(self, locator, wait_time=10) -> None:
        """
        Click on Element
        :param locator : locator(*locator, name)
        :param wait_time: waiting time
        """
        element = self._find_element(locator, wait_time)
        element.click()

    @staticmethod
    def click(locator):
        locator.click()

    def send_keys(self, value):
        self.send_keys(value)

    def text(self, locator, wait_time=10) -> str:
        """
        Get text in element
        :param locator : locator(*locator, name)
        :param wait_time: waiting time
        """
        element = self._find_element(locator, wait_time)
        return element.text

    def get_attribute_element(self, locator, attribute: str = "innerHTML"):
        """
        Find attribute in locator. Default fiend "innerHTML"
        :param locator: locator(*locator, name)
        :param attribute: attribute locator in html
        """
        element = self._find_element(locator)
        if element:
            return element.get_attribute(attribute)
        else:
            return False
