import requests
import allure
from utils.helpers import (
    register_user,
    login_user,
    get_ingredients,
    BASE_URL
)


@allure.title("Создание заказа с авторизацией")
def test_create_order_with_auth():
    user_data, _ = register_user()
    login_response = login_user(user_data["email"], user_data["password"])
    token = login_response.json()["accessToken"]

    ingredients = get_ingredients()
    ingredient_ids = [ingredients[0]["_id"], ingredients[1]["_id"]]

    headers = {
        "Authorization": token
    }

    payload = {
        "ingredients": ingredient_ids
    }

    response = requests.post(
        f"{BASE_URL}/api/orders",
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


@allure.title("Создание заказа без авторизации")
def test_create_order_without_auth():
    ingredients = get_ingredients()
    ingredient_ids = [ingredients[0]["_id"]]

    payload = {
        "ingredients": ingredient_ids
    }

    response = requests.post(f"{BASE_URL}/api/orders", json=payload)

    assert response.status_code == 200
    assert response.json()["success"] is True



@allure.title("Создание заказа с ингредиентами")
def test_create_order_with_ingredients():
    ingredients = get_ingredients()
    ingredient_ids = [ingredients[0]["_id"]]

    response = requests.post(
        f"{BASE_URL}/api/orders",
        json={"ingredients": ingredient_ids}
    )

    # API допускает заказ без авторизации, но с ингредиентами
    assert response.status_code == 200
    assert response.json()["success"] is True


@allure.title("Создание заказа без ингредиентов")
def test_create_order_without_ingredients():
    response = requests.post(
        f"{BASE_URL}/api/orders",
        json={}
    )

    assert response.status_code == 400
    assert response.json()["success"] is False


@allure.title("Создание заказа с неверным хешем ингредиентов")
def test_create_order_with_invalid_ingredient_hash():
    payload = {
        "ingredients": ["invalid_hash"]
    }

    response = requests.post(
        f"{BASE_URL}/api/orders",
        json=payload
    )

    assert response.status_code == 400
    assert response.json()["success"] is False

