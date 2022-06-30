from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging

from fixtures.app import Application

logger = logging.getLogger("search suggest page")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://go.mail.ru/",
        help="search page mail.ru",
    )
    parser.addoption("--headless", action="store_true", help="Headless mode"),


@pytest.fixture(scope="class")
def app(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    if headless:
        chrome_options.headless = True
    else:
        chrome_options.headless = False
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(7)
    app = Application(driver, url)
    logger.info(f"open search page: {url}")
    yield app
    app.quit()
