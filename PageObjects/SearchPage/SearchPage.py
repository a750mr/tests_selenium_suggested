from selenium.webdriver import Keys
from PageObjects.BasePage import BasePage
from fixtures.constans import ConstantsLocators
import logging

logger = logging.getLogger("moodle")


class SearchPage(BasePage):

    def open_search_page(self) -> None:
        self.open_page(self.app.url)

    def click_field_search(self) -> None:
        self.search_element_and_click(ConstantsLocators.SEARCH_FIELD)

    def fill_data_to_search(self, text) -> None:
        self.fill(ConstantsLocators.SEARCH_FIELD, text)

    def delete_data_in_search_field(self) -> None:
        self.clear(ConstantsLocators.SEARCH_FIELD)

    def fill_data_and_get_count_suggested(self, text: str) -> int:
        self.fill(ConstantsLocators.SEARCH_FIELD, text)
        all_suggests = self.find_all_elements(ConstantsLocators.ALL_SUGGESTS)
        return len(all_suggests)

    def search_with_suggested_and_click(self, text: str, select_suggest: int = 0) -> None:
        self.fill(ConstantsLocators.SEARCH_FIELD, text)
        all_suggests = self.find_all_elements(ConstantsLocators.ALL_SUGGESTS)
        self.click(all_suggests[select_suggest])

    def get_text_suggested(self) -> list:
        all_suggests = self.find_all_elements(ConstantsLocators.ALL_SUGGESTS)
        return [element.text for element in all_suggests]

    @staticmethod
    def word_presence_in_suggested(word, lst: list) -> bool:
        result = all(word in w for w in lst)
        return result

    def checked_existence_attribute_in_element(self) -> str:
        value_attribute = self.get_attribute_element(ConstantsLocators.ALL_SUGGESTS)
        return value_attribute

    def return_data_attribute_value_in_element(self) -> str:
        value_attribute = self.get_attribute_element(ConstantsLocators.INPUT_FIELD_TEXT, "value")
        return value_attribute

    def del_one_characters_in_search_field(self) -> None:
        self.fill(ConstantsLocators.SEARCH_FIELD, Keys.BACKSPACE)

    @staticmethod
    def checked_upper_case(lst: list) -> bool:
        result = all(w.isupper() for w in lst)
        return result

    def click_to_X_button(self) -> None:
        self.search_element_and_click(ConstantsLocators.BUTTON_CLEAR_SEARCH_FIELD)
