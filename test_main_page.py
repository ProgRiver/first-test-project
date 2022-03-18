from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                         # открываем страницу
#     page.should_be_login_link()         # проверить наличие ссылки
#     page.go_to_login_page()             # переход на страницу логина
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_go_to_basket_page()
    page.go_to_basket_page()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.sould_be_not_product_in_basket()
    page_basket.sould_be_empty_basket()