import requests
import allure
from data.user_data import get_valid_user

BASE_URL = "https://stellarburgers.education-services.ru"


@allure.title("Создание уникального пользователя")
def test_create_unique_user():
    payload = get_valid_user()
    response = requests.post(f"{BASE_URL}/api/auth/register", json=payload)

    assert response.status_code == 200
    assert response.json()["success"] is True


@allure.title("Создание уже существующего пользователя")
def test_create_existing_user():
    payload = get_valid_user()

    requests.post(f"{BASE_URL}/api/auth/register", json=payload)
    response = requests.post(f"{BASE_URL}/api/auth/register", json=payload)

    assert response.status_code == 403
    assert response.json()["success"] is False


@allure.title("Создание пользователя без обязательного поля")
def test_create_user_without_required_field():
    payload = get_valid_user()
    payload.pop("email")

    response = requests.post(f"{BASE_URL}/api/auth/register", json=payload)

    assert response.status_code == 403
    assert response.json()["success"] is False
