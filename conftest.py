import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    lang = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()
