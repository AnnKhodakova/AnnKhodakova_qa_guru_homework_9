import allure
from selene import by, be
from selene.support.shared import browser


def test_github():
    with allure.step("Открываем главную страницу"):
        browser.open_url("https://github.com")

    with allure.step("Ищем репозиторий в поиске"):
        browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
    browser.element(".header-search-input").submit()

    with allure.step("Открываем репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие issue с номером 76"):
        browser.element(by.partial_text("#76")).should(be.visible)
