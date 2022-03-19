import pytest
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# links_list = [link + str(i) for i in range(10)]
# links_list[7] = pytest.param(links_list[7], marks=pytest.mark.xfail(reason="[!] the page on link has a bug [!]"))

# link_prod = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


# @pytest.mark.skip(reason="[-] Test skip [-]")
# @pytest.mark.parametrize('url', links_list)
# def test_guest_can_add_product_to_basket(browser, url):
#     page = ProductPage(browser, url)
#     page.open()
#     page.should_be_button_basket()
#     page.click_btn_add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_correct_name_product()
#     page.should_be_correct_price()


# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     prod = ProductPage(browser, link_prod)
#     prod.open()
#     prod.click_btn_add_to_basket()
#     prod.should_not_be_success_message()


# def test_guest_cant_see_success_message(browser):
#     prod = ProductPage(browser, link_prod)
#     prod.open()
#     prod.should_not_be_success_message()


# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     prod = ProductPage(browser, link_prod)
#     prod.open()
#     prod.click_btn_add_to_basket()
#     prod.should_be_disappeared()


# def test_guest_should_see_login_link_on_product_page(browser):
#     link_log = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link_log)
#     page.open()
#     page.should_be_login_link()


# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link_log = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link_log)
#     page.open()
#     page.go_to_login_page()


# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     prod_page = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
#     page = ProductPage(browser, prod_page)
#     page.open()
#     page.should_be_go_to_basket_page()
#     page.go_to_basket_page()
#     page_basket = BasketPage(browser, browser.current_url)
#     page_basket.sould_be_not_product_in_basket()
#     page_basket.sould_be_empty_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link_reg = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        password = "555paswTEST"
        self.reg = LoginPage(browser, link_reg)
        self.reg.open()
        self.reg.register_new_user(email, password)
        self.reg.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        prod2 = ProductPage(browser, link2)
        prod2.open()
        prod2.should_not_be_success_message()
    

    def test_user_can_add_product_to_basket(self, browser):
        link3 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page2 = ProductPage(browser, link3)
        page2.open()
        page2.should_be_button_basket()
        page2.click_btn_add_to_basket()
        page2.should_be_correct_name_product()
        page2.should_be_correct_price()

