from selenium.webdriver.common.by import By


class ConstantsLocators:
    SEARCH_FIELD = (By.XPATH, "//*[@id='MSearch']/input[1]")
    ALL_SUGGESTS = (By.CSS_SELECTOR, ".DesktopSuggests-row")
    SETTING_BUTTON = (By.CSS_SELECTOR, '//*[@id="js-main-page"]/div/div/div[1]/div[2]/div[2]/div/div')
    TOOGLE_DELETE_HISTORY = (
        By.CSS_SELECTOR, '//*[@id="js-main-page"]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/label/div[1]')
    BUTTON_CLEAR_SEARCH_FIELD = (By.CSS_SELECTOR, ".Button-value")
    INPUT_FIELD_TEXT = (By.CSS_SELECTOR, "#MSearch > input.DesktopInput-input.DesktopInput-preWrappedWhiteSpace")


class TestDataInput:
    DEFAULT_COUNT_SUGGESTED = 10
    NULL_COUNT_SUGGESTED = 0
    WEATHER = "погода"
    TWO_WORD = "погода москва"
    LONG_WORD = "Автопортрет"
    ONE_SYMBOL = "Y"
    MOTHER = "мама"
    HELL = "hell"
    ONE_SPACES = " "
    UPPERCASE = "МОЛОКО"
    ADULT_WORDS = ["секс", "porn"]
    SPEC_SYMBOLS_TO_RUS = ['.', ':', ';', '>', '<', ',', "'", "\"", '[', "{", "]", "}"]
    AUTOCORRECT_ONE_AND_TWO_WORDS = {"пивет": "привет",
                                     "пивет сосд": "привет сосед"}
    POSTFIX_AND_PREFIX_WORD = ["     программа", "программа     "]
    HIEROGLYPH = "描摹; 临摹; 复写; 复制"
