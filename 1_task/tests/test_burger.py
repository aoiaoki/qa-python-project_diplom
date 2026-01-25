from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_set_buns():
    burger = Burger()
    bun = Bun("black bun", 100)
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    burger.add_ingredient(ingredient)
    assert ingredient in burger.ingredients


def test_remove_ingredient():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_move_ingredient():
    burger = Burger()
    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == ingredient2
    assert burger.ingredients[1] == ingredient1


def test_get_price():
    burger = Burger()
    bun = Bun("black bun", 100)
    burger.set_buns(bun)

    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
    ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    assert burger.get_price() == 400  # 100*2 + 50 + 150


def test_get_receipt():
    burger = Burger()
    bun = Bun("black bun", 100)
    burger.set_buns(bun)

    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert "(==== black bun ====)" in receipt
    assert "= sauce hot sauce =" in receipt
    assert "Price: 250" in receipt
