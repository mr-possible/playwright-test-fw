from playwright.sync_api import Page, expect

from ..components import login_modal


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.flash_incorrect_cred = page.locator("//div[@id='flash']/b[contains(.,'invalid')]")

    def login(self, username: str, password: str):
        lm = login_modal.LoginModal(self.page)
        lm.enter_username(username)
        lm.enter_password(password)
        lm.click_login_btn()

    def is_incorrect_credential_flash_displayed(self) -> bool:
        try:
            expect(self.flash_incorrect_cred).to_be_visible(timeout=10000)  # 10 seconds timeout
            return True
        except AssertionError:
            return False
