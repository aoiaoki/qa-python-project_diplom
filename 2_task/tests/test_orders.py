import requests
import allure
from utils.urls import BASE_URL


@allure.suite("Заказы")
class TestOrders:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, auth_token, ingredient_ids):
        headers = {
            "Authorization": auth_token
        }
        payload = {
            "ingredients": ingredient_ids
        }

        with allure.step("Создание заказа авторизованным пользователем"):
            response = requests.post(
                f"{BASE_URL}/api/orders",
                json=payload,
                headers=headers
            )

        body = response.json()

        assert response.status_code == 200
        assert body["order"]["ingredients"]
        assert body["order"]["number"] > 0

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, ingredient_ids):
        payload = {
            "ingredients": ingredient_ids
        }

        with allure.step("Создание заказа без авторизации"):
            response = requests.post(
                f"{BASE_URL}/api/orders",
                json=payload
            )

        body = response.json()

        assert response.status_code == 200
        assert body["order"]["number"] > 0

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        with allure.step("Создание заказа без ингредиентов"):
            response = requests.post(
                f"{BASE_URL}/api/orders",
                json={}
            )

        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с некорректным id ингредиента")
    def test_create_order_with_invalid_ingredient_hash(self):
        payload = {
            "ingredients": ["invalid_hash"]
        }

        with allure.step("Создание заказа с неверным ингредиентом"):
            response = requests.post(
                f"{BASE_URL}/api/orders",
                json=payload
            )

        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "One or more ids provided are incorrect"
