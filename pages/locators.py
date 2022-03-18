from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class BasketLocators():
    BTN_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PROD_NAME_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    PROD_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner > p > strong")


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
