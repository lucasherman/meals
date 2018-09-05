import copy

WEIGHT_UNITS = ['g']
AMOUNT_TYPE = {1 : 'weight', 2 : 'quantity', 3 : 'indefinite'}

class Ingredient:

    """
    Ingredient of a meal
    """
    def __init__(self, foodProduct, amount=None, weightUnit=None, amountType = 1):
        self.foodProduct = foodProduct
        self.amount = amount
        self.amountType = amountType
        self.weightUnit = weightUnit
        if AMOUNT_TYPE[self.amountType] == 'weight':
            self.weight = amount
        elif AMOUNT_TYPE[self.amountType] == 'quantity':
            self.weight = amount * (1/foodProduct.quantityToWeightRatio)

    def calculateMacros(self):
        ingredientMacros = copy.deepcopy(self.foodProduct.macros)
        ingredientMacros.multiplyMacrosBy(10 * self.weight)
        return ingredientMacros

    def __str__(self):
        if AMOUNT_TYPE[self.amountType] == 'weight':
            return '{}{}-{}'.format(self.weight, self.weightUnit, self.foodProduct)
        elif AMOUNT_TYPE[self.amountType] == 'quantity':
            return '{}-{}'.format(self.amount, self.foodProduct)
        elif AMOUNT_TYPE[self.amountType] == 'indefinite':
            return '{}'.format(self.foodProduct)


class IngredientScanner:
    """
    scanner in resource (may be a text file)
    """
    @staticmethod
    def scan(textList):
        ingredientList = []
        for item in textList:
            words = item.split()
            if len(words) == 1:
                amountType = 3
                amount = None
                foodProduct = words[0]
                weightUnit = None
            elif words[0][-1] in WEIGHT_UNITS:
                amountType = 1
                amount = words[0][:-1]
                foodProduct = ' '.join(words[1:])
                weightUnit = words[0][-1]
            elif words[1] in WEIGHT_UNITS:
                amountType = 1
                amount = words[0]
                foodProduct = ' '.join(words[2:])
                weightUnit = words[1]
            else:
                amountType = 2
                amount = words[0]
                foodProduct = ' '.join(words[1:])
                weightUnit = None

            ingredient = Ingredient(foodProduct, amount, weightUnit, amountType)
            ingredientList.append(ingredient)

        return ingredientList
        


        
