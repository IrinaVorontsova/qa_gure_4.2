from selene.support.shared import browser
from selene import be, have
import pytest
import os


@pytest.fixture()
def driver_browser():
    browser.config.window_width = 1600
    browser.config.window_height = 1024
    browser.open('https://google.com')
    yield driver_browser
    browser.close()


def test_positive(driver_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative(driver_browser):
    browser.element('[name="q"]').should(be.blank).type(os.getcwd()).press_enter()
    browser.element('[class="card-section"]').should(have.text('Страницы, содержащие все слова запроса, не найдены.'))
