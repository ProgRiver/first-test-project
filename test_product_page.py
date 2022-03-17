import pytest
from pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links_list = [link + str(i) for i in range(10)]
links_list[7] = pytest.param(links_list[7], marks=pytest.mark.xfail(reason="[!] the page on link has a bug [!]"))


@pytest.mark.parametrize('url', links_list)
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.should_be_button_basket()
    page.click_btn_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name_product()
    page.should_be_correct_price()
