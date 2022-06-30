from PageObjects.SearchPage.SearchPage import SearchPage


class Application:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.search_page = SearchPage(self)

    def quit(self):
        self.driver.quit()
