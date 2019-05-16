from selenium import webdriver
import pytest


@pytest.fixture()
def br():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('http://wikipedia.org')
    yield browser
    browser.close()