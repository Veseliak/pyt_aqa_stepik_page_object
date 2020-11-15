from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, 'Incorrect url'

    def should_be_login_form(self):
        login_form_present = self.browser.is_element_present(*MainPageLocators.LOGIN_FORN)
        assert login_form_present, 'Login form is not present'

    def should_be_register_form(self):
        register_form_present = self.browser.is_element_present(*MainPageLocators.REGISTER_FORM)
        assert register_form_present, 'register form is not present'