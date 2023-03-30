import allure
from selene import by, be
from selene.support.shared import browser


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_tab()
    should_see_tab_76("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open_url("https://github.com")


@allure.step("Ищем репозиторий {repo} в поиске")
def search_for_repository(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys(repo)
    browser.element(".header-search-input").submit()


@allure.step("Открываем репозиторий {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб issues")
def open_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие issue с номером {number}")
def should_see_tab_76(number):
    browser.element(by.partial_text("#76")).should(be.visible)
