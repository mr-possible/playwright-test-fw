from playwright.sync_api import expect
from src.pages.login_page import LoginPage


def test_login(page):
    page.goto("https://practice.expandtesting.com/login")
    lp = LoginPage(page)

    username = "practice"
    password = "SuperSecretPassword!"

    lp.login(username, password)

    expect(page).to_have_url("https://practice.expandtesting.com/dashboard")
