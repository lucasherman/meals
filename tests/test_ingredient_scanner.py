# -*- coding: utf-8 -*-
from unittest import TestCase
from classes.ingredient import IngredientScanner


class IngredientScannerTest(TestCase):

    def test_scan_meal_product_list(self):

        self.assertEqual(
            self._get_string_ingredient_list(['200g wieprzowina', '300g ziemniaki', 'brokuly']),
            '200g-wieprzowina,300g-ziemniaki,brokuly'
        )
        self.assertEqual(
            self._get_string_ingredient_list(['200 g wieprzowiny', '300 g ziemniaków', 'brokuly']),
            '200g-wieprzowina,300g-ziemniaki,brokuly'
        )
        self.assertEqual(
            self._get_string_ingredient_list(['2 jogurty naturalne małe', '4 łyżeczki płatków owsianych',
                '4 łyżeczki otrębów gryczanych', '2 łyżeczki otrębów owsianych', 'maliny']),
            '2-jogurty naturalne małe,4-łyżeczki płatków owsianych,4-łyżeczki otrębów gryczanych,2-łyżeczki otrębów owsianych,maliny'
        )


    def _get_string_ingredient_list(self, ingredient_list):
        ingredient_list = IngredientScanner.scan(ingredient_list)
        string_ingredient_list = ','.join([str(ingredient) for ingredient in ingredient_list])
        return string_ingredient_list

