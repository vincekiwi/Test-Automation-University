from typing import KeysView
from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + KeysView.RETURN)

    def result_link_titles(self):
        return []
    
    def search_input_value(self):
        return ""
    
    def title(self):
        return ""