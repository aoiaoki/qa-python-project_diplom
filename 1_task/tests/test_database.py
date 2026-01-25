from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_database_init():
    database = Database()
    assert len(database.buns) == 3
    assert len(database.ingredients) == 6


def test_available_buns():
    database = Database()
    buns = database.available_buns()
    assert isinstance(buns, list)
    assert all(isinstance(bun, Bun) for bun in buns)


def test_available_ingredients():
    database = Database()
    ingredients = database.available_ingredients()
    assert isinstance(ingredients, list)
    assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
