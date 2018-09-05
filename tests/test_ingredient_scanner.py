# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.getcwd())
print(sys.path)

from unittest import TestCase
from ingredient import Ingredient, IngredientScanner
from product_base import piers_z_kurczaka_z_ryzem, jajecznica_na_boczku, twarog_z_owocami

class IngredientScannerTest(TestCase):

    def test_scan_meal_product_list(self):

        self.assertEqual(
            self._get_string_ingredient_list(['200g wieprzowiny', '300g ziemniaków', 'brokuly']),
            '200g-wieprzowiny,300g-ziemniaków,brokuly'
        )
        self.assertEqual(
            self._get_string_ingredient_list(['200 g wieprzowiny', '300 g ziemniaków', 'brokuly']),
            '200g-wieprzowiny,300g-ziemniaków,brokuly'
        )


    def _get_string_ingredient_list(self, ingredient_list):
        ingredientList = IngredientScanner.scan(ingredient_list)
        stringIngredientList = ','.join([str(ingredient) for ingredient in ingredientList])
        return stringIngredientList

