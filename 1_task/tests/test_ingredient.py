from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_ingredient_init():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    assert ingredient.type == INGREDIENT_TYPE_SAUCE
    assert ingredient.name == "hot sauce"
    assert ingredient.price == 100


def test_get_price():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    assert ingredient.get_price() == 200


def test_get_name():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
    assert ingredient.get_name() == "sausage"


def test_get_type():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 150)
    assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
