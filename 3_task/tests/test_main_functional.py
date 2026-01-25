import allure
from pages.main_page import MainPage


@allure.title("Переход по клику на «Конструктор»")
def test_open_constructor(main_page):
    main_page.open_constructor()


@allure.title("Переход по клику на «Лента заказов»")
def test_open_feed(main_page):
    main_page.open_feed()


@allure.title("Открытие и закрытие модального окна ингредиента")
def test_ingredient_modal(main_page):
    main_page.open_ingredient_modal()
    main_page.close_ingredient_modal()
    main_page.wait_modal_closed()


@allure.title("Ингредиент добавляется в конструктор")
def test_ingredient_added_to_constructor(main_page):
    main_page.add_ingredient_to_constructor()
    assert main_page.constructor_has_items()





