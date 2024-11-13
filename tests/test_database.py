from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

def test_available_buns():
    database = Database()
    buns = database.available_buns()
    assert all(isinstance(bun, Bun) for bun in buns)
    assert len(buns) > 0

def test_available_ingredients():
    database = Database()
    ingredients = database.available_ingredients()
    assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
    assert len(ingredients) > 0
