import pytest
import requests
import allure
from data.user_data import get_valid_user
from utils.urls import BASE_URL


@allure.feature("Создание пользователя")
class TestUserCreate:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        payload = get_valid_user()

        with allure.step("Отправка запроса на регистрацию пользователя"):
            response = requests.post(f"{BASE_URL}/api/auth/register", json=payload)

        assert response.status_code == 200
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert "user" in response.json()

    @allure.title("Создание уже существующего пользователя")
    def test_create_existing_user(self):
        payload = get_valid_user()

        requests.post(f"{BASE_URL}/api/auth/register", json=payload)

        with allure.step("Повторная регистрация пользователя"):
            response = requests.post(f"{BASE_URL}/api/auth/register", json=payload)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_without_required_field(self, missing_field):
        payload = get_valid_user()
        payload.pop(missing_field)

        with allure.step(f"Регистрация без поля {missing_field}"):
            response = requests.post(f"{BASE_URL}/api/auth/register", json=payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
