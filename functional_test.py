import os
from selenium import webdriver


def get_chromedriver_browser():
    return webdriver.Chrome(
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)),
            '../superlists/chromedriver')
    )

browser = get_chromedriver_browser()
browser.get('http://localhost:8000')

assert 'Django' in browser.title