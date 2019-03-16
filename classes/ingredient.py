import copy
from .product import FoodProduct

WEIGHT_UNITS = ['g']
AMOUNT_TYPE = {1: 'weight', 2: 'quantity', 3: 'indefinite'}


class Ingredient:

    """
    Ingredient of a meal
    """

    def __init__(self, food_product, amount=None,
                 weight_unit=None, amount_type=1):
        self.food_product = food_product
        self.amount = amount
        self.amount_type = amount_type
        self.weight_unit = weight_unit
        if AMOUNT_TYPE[self.amount_type] == 'weight':
            self.weight = amount
        elif AMOUNT_TYPE[self.amount_type] == 'quantity':
            self.weight = int(amount) * \
                (1 / food_product.quantityToWeightRatio)

    def calculateMacros(self):
        ingredient_macros = copy.deepcopy(self.food_product.macros)
        ingredient_macros.multiply_macros_by(10 * self.weight)
        return ingredient_macros

    def __str__(self):
        if AMOUNT_TYPE[self.amount_type] == 'weight':
            return '{}{}-{}'.format(self.weight,
                                    self.weight_unit, self.food_product)
        elif AMOUNT_TYPE[self.amount_type] == 'quantity':
            return '{}-{}'.format(self.amount, self.food_product)
        elif AMOUNT_TYPE[self.amount_type] == 'indefinite':
            return '{}'.format(self.food_product)


class IngredientScanner:
    """
    scanner in resource (may be a text file)
    """
    @staticmethod
    def scan(textList):
        ingredient_list = []
        for item in textList:
            words = item.split()
            if len(words) == 1:
                amount_type = 3
                amount = None
                food_product = words[0]
                weight_unit = None
            elif words[0][-1] in WEIGHT_UNITS:
                amount_type = 1
                amount = words[0][:-1]
                food_product = ' '.join(words[1:])
                weight_unit = words[0][-1]
            elif words[1] in WEIGHT_UNITS:
                amount_type = 1
                amount = words[0]
                food_product = ' '.join(words[2:])
                weight_unit = words[1]
            else:
                amount_type = 2
                amount = words[0]
                food_product = ' '.join(words[1:])
                weight_unit = None

            ingredient = Ingredient(food_product, amount, weight_unit, amount_type)
            ingredient_list.append(ingredient)

        return ingredient_list
