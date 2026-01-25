import random
import string
import requests

BASE_URL = "https://stellarburgers.education-services.ru"


def random_email():
    return f"test_{''.join(random.choices(string.ascii_lowercase, k=8))}@mail.ru"


def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


def random_name():
    return ''.join(random.choices(string.ascii_letters, k=6))


def register_user():
    payload = {
        "email": random_email(),
        "password": random_password(),
        "name": random_name()
    }
    response = requests.post(f"{BASE_URL}/api/auth/register", json=payload)
    return payload, response


def login_user(email, password):
    payload = {
        "email": email,
        "password": password
    }
    return requests.post(f"{BASE_URL}/api/auth/login", json=payload)


def get_ingredients():
    response = requests.get(f"{BASE_URL}/api/ingredients")
    return response.json()["data"]
