from product import Macros

class Meal:

    def __init__(self, ingredients = [])
        self.ingredients = ingredients
        self.mealMacros = Macros()

    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)

    def addIngredients(self, ingredients):
        self.ingredients.extend(ingredients)

    def calculateMealMacros(self):
        mealMacros = Macros()
        for ingredient in self.ingredients:
            mealMacros.addMacros(ingredient.macros)
            self.mealMacros = mealMacros

