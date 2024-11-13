import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_set_buns():
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 100
    burger = Burger()
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient():
    ingredient = Mock(spec=Ingredient)
    burger = Burger()
    burger.add_ingredient(ingredient)
    assert ingredient in burger.ingredients


def test_remove_ingredient():
    ingredient = Mock(spec=Ingredient)
    burger = Burger()
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert ingredient not in burger.ingredients


def test_move_ingredient():
    ingredient1 = Mock(spec=Ingredient)
    ingredient2 = Mock(spec=Ingredient)
    burger = Burger()
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2, ingredient1]


def test_get_price():
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 100
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 50
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    assert burger.get_price() == 250  # 100*2 + 50


def test_get_receipt():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 100
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Test Ingredient"
    ingredient.get_type.return_value = "filling"
    ingredient.get_price.return_value = 50  # добавляем значение для get_price

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert "Test Bun" in receipt
    assert "filling Test Ingredient" in receipt
    assert "Price: 250" in receipt  # 100*2 + 50 = 250

