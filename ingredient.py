import copy

class Ingredient:

    AMOUNT_TYPE = {1 : 'weight', 2 : 'quantity'}

    """
    Ingredient of a meal
    """
    def __init__(self, foodProduct, amount, amountType = 1):
        self.foodProduct = foodProduct
        self.amount = amount
        if AMOUNT_TYPE[amountType] == 'weight':
            self.weight = amount
        else if AMOUNT_TYPE[amountType] == 'quantity':
            self.weight = amount * (1/foodProduct.quantityToWeightRatio)

    def calculateMacros(self):
        ingredientMacros = copy.deepcopy(self.foodProduct.macros)
        ingredientMacros.multiplyMacrosBy(10 * self.weight)
        return ingredientMacros

class IngredientScanner:
    """
    scanner in resource (may be a text file)
    """
        


        
