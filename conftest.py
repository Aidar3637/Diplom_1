import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def sample_bun():
    return Bun("test bun", 150)

@pytest.fixture
def sample_ingredient_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50)

@pytest.fixture
def sample_ingredient_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "test filling", 100)

@pytest.fixture
def sample_burger(sample_bun, sample_ingredient_sauce, sample_ingredient_filling):
    burger = Burger()
    burger.set_buns(sample_bun)
    burger.add_ingredient(sample_ingredient_sauce)
    burger.add_ingredient(sample_ingredient_filling)
    return burger

@pytest.fixture
def sample_database():
    return Database()
