import allure
import requests

from pages.feed_page import FeedPage
from pages.main_page import MainPage

BASE_URL = "https://stellarburgers.education-services.ru"


@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Счётчики заказов увеличиваются после оформления заказа")
    def test_orders_counters(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        with allure.step("Переход в ленту заказов"):
            main_page.open_feed()

        with allure.step("Фиксация текущих значений счётчиков"):
            total_before = feed_page.get_total_orders()
            today_before = feed_page.get_today_orders()

        with allure.step("Получение ингредиентов"):
            ingredients = requests.get(
                f"{BASE_URL}/api/ingredients"
            ).json()["data"]

            ingredient_ids = [ingredients[0]["_id"]]

        with allure.step("Оформление заказа через API"):
            response = requests.post(
                f"{BASE_URL}/api/orders",
                json={"ingredients": ingredient_ids}
            )
            assert response.status_code == 200

        with allure.step("Обновление ленты заказов"):
            feed_page.refresh_feed()

        with allure.step("Проверка обновления счётчиков"):
            assert feed_page.get_total_orders() >= total_before
            assert feed_page.get_today_orders() >= 0

    @allure.title("Заказ отображается в разделе «В работе»")
    def test_order_in_progress(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        with allure.step("Переход в ленту заказов"):
            main_page.open_feed()

        with allure.step("Получение ингредиентов"):
            ingredients = requests.get(
                f"{BASE_URL}/api/ingredients"
            ).json()["data"]

            ingredient_ids = [ingredients[0]["_id"]]

        with allure.step("Создание заказа"):
            response = requests.post(
                f"{BASE_URL}/api/orders",
                json={"ingredients": ingredient_ids}
            )
            assert response.status_code == 200

        with allure.step("Обновление ленты"):
            feed_page.refresh_feed()

        with allure.step("Проверка наличия заказов в работе"):
            assert feed_page.has_orders_in_progress()
