from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def sould_be_not_product_in_basket(self):
        """Товара нет и не появляется на странице корзины""" 
        assert self.is_not_element_present(*BasketLocators.PROD_IN_BASKET), "[!] Product in basket [!]"
    

    def sould_be_empty_basket(self):
        """Есть сообщение, что корзина пустая"""
        assert self.is_element_present(*BasketLocators.EMPTY_BASKET), "[!] No empty basket [!]"
    
