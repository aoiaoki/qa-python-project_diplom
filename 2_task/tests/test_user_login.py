import requests
import allure
import pytest
from utils.urls import BASE_URL


@allure.suite("Логин пользователя")
class TestUserLogin:

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, registered_user):
        payload = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }

        with allure.step("Отправка запроса на логин"):
            response = requests.post(
                f"{BASE_URL}/api/auth/login",
                json=payload
            )

        body = response.json()

        assert response.status_code == 200
        assert "accessToken" in body
        assert "refreshToken" in body
        assert body["user"]["email"] == registered_user["email"]

    @allure.title("Логин с неверным логином и паролем")
    def test_login_with_invalid_credentials(self):
        payload = {
            "email": "wrong@mail.ru",
            "password": "wrongpassword"
        }

        with allure.step("Попытка логина с неверными данными"):
            response = requests.post(
                f"{BASE_URL}/api/auth/login",
                json=payload
            )

        body = response.json()

        assert response.status_code == 401
        assert body["message"] == "email or password are incorrect"

    @allure.title("Логин без обязательных полей")
    @pytest.mark.parametrize("field", ["email", "password"])
    def test_login_without_required_field(self, field):
        payload = {
            "email": "test@mail.ru",
            "password": "password123"
        }
        payload.pop(field)

        with allure.step(f"Логин без поля {field}"):
            response = requests.post(
                f"{BASE_URL}/api/auth/login",
                json=payload
            )

        body = response.json()

        assert response.status_code == 401
        assert body["message"] == "email or password are incorrect"
