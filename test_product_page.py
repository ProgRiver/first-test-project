from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link_2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link_2)
    page.open()
    page.should_be_button_basket()
    page.click_btn_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name_product()
    page.should_be_correct_price()
    