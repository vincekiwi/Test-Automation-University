from selenium import webdriver
import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

def test_basic_duckduckgo_search(browser):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "cat"

    search_page.load()

    search_page.search(PHRASE)

    assert PHRASE in result_page.title()

    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()