from playwright.sync_api import expect
from src.pages.login_page import LoginPage


def test_login_title(page, login_page_url):
    page.goto(login_page_url)
    expect(page).to_have_title("Test Login form page for Automation Testing Practice")


def test_successful_login(page, login_page_url):
    page.goto(login_page_url)
    lp = LoginPage(page)

    username = "practice"
    password = "SuperSecretPassword!"

    lp.login(username, password)

    expect(page).not_to_have_url(login_page_url)


def test_unsuccessful_login(page, login_page_url):
    page.goto(login_page_url)
    lp = LoginPage(page)

    username = "sam"
    password = "legend"

    lp.login(username, password)

    assert lp.is_incorrect_credential_flash_displayed() is True
