from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, BasketLocators
from math import log, sin


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print()
            print(f"[-] Your code: {alert_text} [-]")
            alert.accept()
        except NoAlertPresentException:
            print("[!] No second alert presented [!]")


    def is_not_element_present(self, how, what, timeout=4):
        """Метод проверяет, что элемент не появляется на странице в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    

    def is_disappeared(self, how, what, timeout=4):
        """Метод проверяет, что какой-то элемент исчезает"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()


    def should_be_login_link(self):
        """Проверка наличия ссылки на страницу логина"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "[*] Login link is not presented [*]"
    

    def go_to_basket_page(self):
        """Переход в корзину по кнопке в шапке сайта"""
        self.browser.find_element(*BasketLocators.BTN_GO_TO_BASKET).click()
    

    def should_be_go_to_basket_page(self):
        """Проверка наличия кнопки в шапке сайта для перехода на страницу корзины"""
        assert self.is_element_present(*BasketLocators.BTN_GO_TO_BASKET), "[!] Button basket is not presented [!]"