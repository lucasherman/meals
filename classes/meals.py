from classes.product import Macros


class Meal:

    def __init__(self, ingredients=[]):
        self.ingredients = ingredients
        self.meal_macros = Macros()

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def add_ingredients(self, ingredients):
        self.ingredients.extend(ingredients)

    def calculate_meal_macros(self):
        meal_macros = Macros()
        for ingredient in self.ingredients:
            meal_macros.add_macros(ingredient.macros)
            self.meal_macros = meal_macros
