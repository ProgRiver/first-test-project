from .base_page import BasePage
from .locators import BasketLocators, ProductPageLocators


class ProductPage(BasePage):
    def click_btn_add_to_basket(self):
        self.browser.find_element(*BasketLocators.BTN_BASKET).click()
    

    def should_be_button_basket(self):
        """Проверка наличия кнопки добавления в корзину"""
        assert self.is_element_present(*BasketLocators.BTN_BASKET), "[!] Button add to basket is not presented [!]"
    

    def should_be_correct_name_product(self):
        """Проверка присутствия корректного названия товара в тексте сообщения"""
        text_prod = self.browser.find_element(*BasketLocators.PRODUCT_NAME).text
        text_in_basket = self.browser.find_element(*BasketLocators.PROD_NAME_MESSAGE).text
        assert text_prod.strip() == text_in_basket.strip(), "[!] No product name in message [!]"


    def should_be_correct_price(self):
        """Проверка корректной стоимости товара в тексте сообщения"""
        text_price = self.browser.find_element(*BasketLocators.PRODUCT_PRICE).text
        text_in_massage = self.browser.find_element(*BasketLocators.PROD_PRICE_MESSAGE).text
        assert text_price.strip() == text_in_massage.strip(), "[!] No product price in message [!]"


    def should_not_be_success_message(self):
        """Сообщение об успехе отображается, но не должно"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "[!] Success message is presented, but should not be [!]"
    

    def should_be_disappeared(self):
        """Сообщение, что элемент не исчезает"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "[!] Not disappeared [!]"