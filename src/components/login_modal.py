from playwright.sync_api import Page


class LoginModal:
    def __init__(self, page: Page):
        self.page = page
        self.username = self.page.get_by_label("Username")
        self.password = self.page.get_by_label("Password")
        self.loginBtn = page.get_by_role("button", name="Login")

    def enter_username(self, username: str):
        self.username.fill(username)

    def enter_password(self, password: str):
        self.password.fill(password)

    def click_login_btn(self):
        self.loginBtn.click()