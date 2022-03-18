import pytest
from pages.product_page import ProductPage


# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# links_list = [link + str(i) for i in range(10)]
# links_list[7] = pytest.param(links_list[7], marks=pytest.mark.xfail(reason="[!] the page on link has a bug [!]"))

link_prod = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


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


def test_guest_should_see_login_link_on_product_page(browser):
    link_log = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link_log)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link_log = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link_log)
    page.open()
    page.go_to_login_page()
