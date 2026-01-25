import requests
import allure
from utils.helpers import register_user, login_user, BASE_URL


@allure.title("Логин под существующим пользователем")
def test_login_existing_user():
    user_data, _ = register_user()

    response = login_user(user_data["email"], user_data["password"])

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "accessToken" in response.json()


@allure.title("Логин с неверным логином и паролем")
def test_login_with_invalid_credentials():
    payload = {
        "email": "wrong@mail.ru",
        "password": "wrongpassword"
    }

    response = requests.post(f"{BASE_URL}/api/auth/login", json=payload)

    assert response.status_code == 401
    assert response.json()["success"] is False
