import logging
import pytest
from fixtures.constans import TestDataInput

logger = logging.getLogger("tests")


class TestsSearchPage:
    @pytest.mark.smoke
    def test_smoked_functional(self, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Fill data and return available suggested
        4.Search with text and number suggest to click
        5.Equal count suggests
        6.Equal page has changed
        """
        logger.info(f"Smoked tests: open search page, fill data, click 4 suggest. Data input: {TestDataInput.WEATHER}")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        count_available_suggested = app.search_page.fill_data_and_get_count_suggested(TestDataInput.WEATHER)
        app.search_page.search_with_suggested_and_click(TestDataInput.WEATHER, 3)
        assert count_available_suggested == TestDataInput.DEFAULT_COUNT_SUGGESTED, "Suggested not is 10"
        assert f'https://go.mail.ru/search?q=' in app.driver.current_url, "URL has not changed. Click doesnt work"

    @pytest.mark.critical_path
    def test_entry_one_symbol(self, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Search with text and number suggest to click
        4.Equal page has changed
        """
        logger.info(
            f"Entry to search one symbol and click first elements in suggested. Checked page not equal start page.Data:"
            f"{TestDataInput.ONE_SYMBOL}")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.search_with_suggested_and_click(TestDataInput.ONE_SYMBOL, 0)
        assert f'https://go.mail.ru/search?q=' in app.driver.current_url, "URL has not changed. Click doesnt work"

    @pytest.mark.critical_path
    def test_click_last_suggested(self, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Search with text and click last suggest
        4.Equal page has changed
        """
        logger.info(
            f"Entry to search {TestDataInput.WEATHER} and click last element in suggested. Checked page not equal start page.")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.search_with_suggested_and_click(TestDataInput.WEATHER, 9)
        assert f'https://go.mail.ru/search?q=' in app.driver.current_url, "URL has not changed. Click doesnt work"

    @pytest.mark.critical_path
    def test_equal_text_in_suggested(self, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Fill data to search field
        4.Getting text in suggested
        5.Equal word presence in suggested
        """
        logger.info(
            f"Entry to search {TestDataInput.MOTHER}. Checked suggested have word presence")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(TestDataInput.MOTHER)
        lst_suggested = app.search_page.get_text_suggested()
        result_checked_inner_word = app.search_page.word_presence_in_suggested(TestDataInput.MOTHER, lst_suggested)
        assert result_checked_inner_word == True, "Word presence and suggested are different"

    @pytest.mark.critical_path
    @pytest.mark.xfail(reason="There is no method in selenium to wait for the text in the locator to change. "
                              "We have to wait for the DOM to change.")
    def test_modification_field_from_delete_character(self, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Fill data and get text suggested
        4.Del symbols in search
        5.Get suggested and equal to before
        """
        logger.info(
            f"Entry to search {TestDataInput.HELL}. Checked suggested refactoring from delete one symbols")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(TestDataInput.HELL)
        lst_before_suggested = app.search_page.get_text_suggested()
        app.search_page.del_one_characters_in_search_field()
        lst_after_suggested = app.search_page.get_text_suggested()
        assert lst_after_suggested != lst_before_suggested, "Does not change suggested when deleting a character"

    @pytest.mark.critical_path
    def test_blocked_suggested_with_only_space(self, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Get count suggested
        4.Equal available and expected count suggested
        """
        logger.info(f"Entry to search only spaces and checked suggested not visibility")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        count_available_suggested = app.search_page.fill_data_and_get_count_suggested(TestDataInput.ONE_SPACES)
        assert count_available_suggested == TestDataInput.NULL_COUNT_SUGGESTED, "Tips are displayed when entering spaces"

    @pytest.mark.critical_path
    @pytest.mark.parametrize("word", TestDataInput.POSTFIX_AND_PREFIX_WORD)
    def test_fill_data_with_postfix_and_prefix_space_in_word(self, word, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Get count suggested
        4.Equal available and expected count suggested
        """
        logger.info(f"Entry {word} from prefix or postfix space and checked suggested visibility")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        count_available_suggested = app.search_page.fill_data_and_get_count_suggested(word)
        assert count_available_suggested == TestDataInput.DEFAULT_COUNT_SUGGESTED, \
            "Tips are displayed when entering post or prefix spaces"

    @pytest.mark.critical_path
    def test_available_suggested_from_two_words(self, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Get count suggested
        4.Equal available and expected count suggested
        """
        logger.info(f"Entry {TestDataInput.TWO_WORD} for two word in search. Check available suggested")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        count_available_suggested = app.search_page.fill_data_and_get_count_suggested(TestDataInput.TWO_WORD)
        assert count_available_suggested == TestDataInput.DEFAULT_COUNT_SUGGESTED, "Two words don't show tooltip"

    @pytest.mark.critical_path
    def test_dont_working_entry_uppercase(self, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal suggested dont have uppercase
        """
        logger.info(f"Entry {TestDataInput.UPPERCASE}. Check suggested dont have uppercase symbols")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(TestDataInput.UPPERCASE)
        lst_suggested = app.search_page.get_text_suggested()
        assert app.search_page.checked_upper_case(lst_suggested) is False, "Displays upper case instead of lower case"

    @pytest.mark.critical_path
    def test_word_is_highlighted(self, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal element have <b> attribute
        """
        logger.info(f"Entry any word and checked word in suggested have <b> attribute")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(TestDataInput.WEATHER)
        inner_html = app.search_page.checked_existence_attribute_in_element()
        assert f"<b>{TestDataInput.WEATHER}</b>" in inner_html, "Query word not highlighted"

    @pytest.mark.negative
    @pytest.mark.critical_path
    @pytest.mark.parametrize("word", TestDataInput.ADULT_WORDS)
    def test_entry_adult_word(self, app, word):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal suggested doesn't have available for search adult
        """
        logger.info(f"Entry {word} and checked suggested dont visibility")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        assert TestDataInput.NULL_COUNT_SUGGESTED == app.search_page.fill_data_and_get_count_suggested(
            word), "According to the adult hints appear"

    @pytest.mark.extended
    @pytest.mark.parametrize("sym", TestDataInput.SPEC_SYMBOLS_TO_RUS)
    def test_entry_spec_symbols(self, app, sym):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal suggested doesn't have available for search spec symbols == has changed to russian sym
        """
        logger.info(f"Entry {sym} and checked this spec-sym changed to RUS sym")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(sym)
        assert sym not in app.search_page.get_text_suggested()

    @pytest.mark.critical_path
    @pytest.mark.parametrize("item, key", TestDataInput.AUTOCORRECT_ONE_AND_TWO_WORDS.items())
    def test_entry_to_autocorrect(self, app, item, key):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal entry word auto-corrected
        """
        logger.info(f"Entry words and checked auto-corrected")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(item)
        assert key in app.search_page.get_text_suggested()

    @pytest.mark.critical_path
    def test_available_suggested_from_long_words(self, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Get count suggested
        4.Equal available and expected count suggested
        """
        logger.info(f"Entry {TestDataInput.LONG_WORD} and check have this word in suggested")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        count_available_suggested = app.search_page.fill_data_and_get_count_suggested(TestDataInput.LONG_WORD)
        assert count_available_suggested == TestDataInput.DEFAULT_COUNT_SUGGESTED, "Long word don't show tooltip"

    @pytest.mark.critical_path
    def test_fill_data_and_delete_checked_field_empty(self, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Fill data
        4.Click to delete field button
        4.Equal field has empty
        """
        logger.info(f"Entry word and click to delete field button and check field search has empty")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(TestDataInput.WEATHER)
        app.search_page.click_to_X_button()
        assert app.search_page.return_data_attribute_value_in_element() == '', "Search field is not empty"

    @pytest.mark.negative
    @pytest.mark.critical_path
    def test_blocked_suggested_with_hieroglyph(self, app):
        """
        1.Open Search Page
        2.Clicked on input field
        3.Get count suggested
        4.Equal available and expected count suggested
        """
        logger.info(f"Entry to search hieroglyph and checked suggested not visibility")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        count_available_suggested = app.search_page.fill_data_and_get_count_suggested(TestDataInput.HIEROGLYPH)
        assert count_available_suggested == TestDataInput.NULL_COUNT_SUGGESTED, "Tips are displayed when entering spaces"
