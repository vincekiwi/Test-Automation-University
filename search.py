from selenium.webdriver.common.by import By

class DuckDuckGoSearchPage:

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser):
        self.browser = browser
    
    def load(self):
        pass
    def search(self, phrase):
        pass