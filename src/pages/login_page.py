from playwright.sync_api import Page, expect

from ..components import login_modal


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def login(self, username: str, password: str):
        lm = login_modal.LoginModal(self.page)
        lm.enter_username(username)
        lm.enter_password(password)
        # loginModal.click_login_btn()
