import os, pytest
from dotenv import load_dotenv

from playwright.sync_api import sync_playwright

load_dotenv()


@pytest.fixture(scope="session")
def config():
    return config


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def login_page_url(config):
    return os.environ.get('login_url')


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
