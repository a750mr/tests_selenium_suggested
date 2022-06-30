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
        3.Return available suggested
        4.Search with text and number suggest to click
        5.Equal count suggests
        6.Equal other link
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
        4.Equal other link
        """
        logger.info(
            f"Entry one symbol and click first elements in suggested. Checked page not equal start pages. Data: "
            f"{TestDataInput.ONE_SYMBOL}")
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.search_with_suggested_and_click(TestDataInput.ONE_SYMBOL, 0)
        assert app.driver.current_url != "https://go.mail.ru/", "URL has not changed"

    def test_click_last_suggested(self, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Search with text and number suggest to click
        4.Equal other link
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.search_with_suggested_and_click(TestDataInput.WEATHER, 9)
        assert app.driver.current_url != "https://go.mail.ru/", "URL has not changed"

    def test_equal_text_in_suggested(self, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Search with text and number suggest to click
        4.Equal other link
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(TestDataInput.MOTHER)
        lst_suggested = app.search_page.get_text_suggested()
        result_checked_inner_word = app.search_page.word_presence_in_suggested(TestDataInput.MOTHER, lst_suggested)
        assert result_checked_inner_word == True, "Request and suggested are different"

    @pytest.mark.xfail
    def test_modification_field_from_delete_character(self, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Fill data and get text suggested
        4.Del symbols in search
        5.Get suggested and equal to before
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(TestDataInput.HELL)
        lst_before_suggested = app.search_page.get_text_suggested()
        app.search_page.del_one_characters_in_search_field()
        lst_after_suggested = app.search_page.get_text_suggested()
        assert lst_after_suggested != lst_before_suggested, "Does not change suggested when deleting a character"
        # noqa There is no method in selenium to wait for the text in the locator to change. We have to wait for the DOM to change. That's why the test is marked with xfail

    def test_blocked_suggested_with_only_space(self, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Get count suggested
        4.Equal available and expected
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        count_available_suggested = app.search_page.fill_data_and_get_count_suggested(TestDataInput.ONE_SPACES)
        assert count_available_suggested == TestDataInput.NULL_COUNT_SUGGESTED, "Tips are displayed when entering spaces"

    @pytest.mark.parametrize("word", TestDataInput.POSTFIX_AND_PREFIX_WORD)
    def test_fill_data_with_postfix_and_prefix_space_in_word(self, word, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal available suggested
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        count_available_suggested = app.search_page.fill_data_and_get_count_suggested(word)
        assert count_available_suggested == TestDataInput.DEFAULT_COUNT_SUGGESTED, \
            "Tips are displayed when entering post or prefix spaces"

    def test_available_suggested_from_two_words(self, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Get count suggested
        4.Equal available and expected
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        count_available_suggested = app.search_page.fill_data_and_get_count_suggested(TestDataInput.TWO_WORD)
        assert count_available_suggested == TestDataInput.DEFAULT_COUNT_SUGGESTED, "Two words don't show tooltip"

    def test_dont_working_entry_uppercase(self, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal avialible suggested for uppercase checked
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(TestDataInput.UPPERCASE)
        lst_suggested = app.search_page.get_text_suggested()
        assert app.search_page.checked_upper_case(lst_suggested) == False, "Displays upper case instead of lower case"

    def test_word_is_highlighted(self, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal element have <b> attribute
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(TestDataInput.WEATHER)
        inner_html = app.search_page.checked_existence_attribute_in_element()
        assert f"<b>{TestDataInput.WEATHER}</b>" in inner_html, "Query word not highlighted"

    @pytest.mark.parametrize("word", TestDataInput.ADULT_WORDS)
    def test_entry_adult_word(self, app, word):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal miss suggested for search adult
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        assert TestDataInput.NULL_COUNT_SUGGESTED == app.search_page.fill_data_and_get_count_suggested(
            word), "According to the adult hints appear"

    @pytest.mark.parametrize("sym", TestDataInput.SPEC_SYMBOLS_TO_RUS)
    def test_entry_spec_symbols(self, app, sym):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal miss suggested for search spec symbols
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(sym)
        assert sym not in app.search_page.get_text_suggested()

    @pytest.mark.parametrize("item, key", TestDataInput.AUTOCORRECT_ONE_AND_TWO_WORDS.items())
    def test_entry_to_autocorrect(self, app, item, key):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Fill data
        4.Equal miss suggested for search spec symbols
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        app.search_page.fill_data_to_search(item)
        assert key in app.search_page.get_text_suggested()

    def test_available_suggested_from_long_words(self, app):
        """
        1.Go to Search Page
        2.Clicked on input field
        3.Get count suggested
        4.Equal available and expected
        """
        app.search_page.open_search_page()
        app.search_page.click_field_search()
        count_available_suggested = app.search_page.fill_data_and_get_count_suggested(TestDataInput.LONG_WORD)
        assert count_available_suggested == TestDataInput.DEFAULT_COUNT_SUGGESTED, "Long word don't show tooltip"

    # def test_working_toogle_delete_history(self, app):
    #     """
    #     1.Go to Search Page
    #     2.Clicked on input field
    #     3.Fill data
    #     4.Get before suggested
    #     5.Switch toogle setting history
    #     6.Get after suggested and assert to before
    #     """
    #     app.search_page.open_search_page()
    #     app.search_page.click_field_search()
    #     app.search_page.fill_data_to_search(TestData.DATA_WEATHER)
    #     lst_before_suggested = app.search_page.get_text_suggested()
    #     app.search_page.open_setting_search_and_switch_toogle()
    #     lst_after_suggested = app.search_page.get_text_suggested()
    #     assert lst_after_suggested != lst_before_suggested, "The two lists correspond to each other"
