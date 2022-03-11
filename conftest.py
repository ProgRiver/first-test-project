import pytest
import time
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    """
    Фикстура объявления браузера и настроек. Передается в тест, как параметр.
    """
    language_on_request = request.config.getoption("language")
    settings = webdriver.ChromeOptions()

    # Настройки запроса
    settings.add_experimental_option("prefs", {"intl.accept_languages": language_on_request})
    # Настройки терминала (убирает лишнюю информацию)
    settings.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=settings)
    yield driver

    # Установите ожидание закрытия браузера 
    time.sleep(5)
    driver.quit()