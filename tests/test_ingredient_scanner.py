# -*- coding: utf-8 -*-
from unittest import TestCase
from classes.ingredient import IngredientScanner


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

