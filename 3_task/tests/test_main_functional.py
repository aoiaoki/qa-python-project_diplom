import allure

from pages.main_page import MainPage


@allure.feature("Главная страница")
class TestMainFunctional:

    @allure.title("Переход по клику на «Конструктор»")
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)

        with allure.step("Клик по вкладке «Конструктор»"):
            main_page.open_constructor()

        with allure.step("Проверка, что конструктор открыт"):
            assert main_page.is_constructor_opened()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_open_feed(self, driver):
        main_page = MainPage(driver)

        with allure.step("Клик по вкладке «Лента заказов»"):
            main_page.open_feed()

        with allure.step("Проверка, что открыта лента заказов"):
            assert main_page.is_feed_opened()

    @allure.title("Открытие и закрытие модального окна ингредиента")
    def test_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открытие модального окна ингредиента"):
            main_page.open_ingredient_modal()
            assert main_page.is_ingredient_modal_opened()

        with allure.step("Закрытие модального окна ингредиента"):
            main_page.close_ingredient_modal()
            main_page.wait_modal_closed()

        with allure.step("Проверка, что модальное окно закрыто"):
            assert not main_page.is_ingredient_modal_opened()

    @allure.title("Ингредиент добавляется в конструктор")
    def test_ingredient_added_to_constructor(self, driver):
        main_page = MainPage(driver)

        with allure.step("Добавление ингредиента в конструктор"):
            main_page.add_ingredient_to_constructor()

        with allure.step("Проверка, что в конструкторе появился ингредиент"):
            assert main_page.constructor_has_items()
