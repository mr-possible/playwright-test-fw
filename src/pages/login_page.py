from playwright.sync_api import Page, expect

from ..components import login_modal


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.flash_incorrect_cred = page.locator("//div[@id='flash']/b[contains(.,'invalid')]")
        self.nav_elements = page.locator("//div[@id='main-navbar']/ul/li/a").all()

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

    def are_nav_elements_displayed(self, expected_list: list) -> bool:
        actual_list = [item.text_content().strip() for item in self.nav_elements]
        return actual_list == expected_list
