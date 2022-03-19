from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        """Проверка на корректный url адрес"""
        assert "login" in self.browser.current_url, "[*] 'login' not in url [*]"


    def should_be_login_form(self):
        """Проверка наличия формы логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "[*] Login form is not presented [*]"


    def should_be_register_form(self):
        """Проверка наличия формы регистрации"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "[*] Register form is not presented [*]"
    

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.ADD_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.ADD_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONTROL_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_REGISTER).click()
