#!/usr/bin/env python
# -*- coding: utf-8 -*-


class FoodProduct:

    """
    General food product class
    """

    def __init__(self, name, macros=None,
                 quantity_to_weight_ratio=1, micros=None):
        self.name = name
        # ratio 1 - 1 unit = 1kg
        # ratio 2 - 1 unit = 0.5kg
        # ratio 0.5 - 1 unit = 2kg
        self.quantity_to_weight_ratio = quantity_to_weight_ratio
        self.macros = macros
        self.micros = micros

    def __str__(self):
        return self.name


class Macros:
    """
    class representing macros for a food product
    """

    def __init__(self, carbs=0, fats=0, proteins=0):
        # macros are in grams per 100g
        self.carbs = carbs
        self.fats = fats
        self.proteins = proteins

    def multiply_macros_by(self, multiple):
        self.carbs = self.carbs * multiple
        self.fats = self.fats * multiple
        self.proteins = self.proteins * multiple

    def addMacros(self, macros_to_add):
        self.carbs += macros_to_add.carbs
        self.fats += macros_to_add.fats
        self.proteins += macros_to_add.proteins


class Micros:
    """
    class representing micro elements for a food product
    """

    def __init__(self, microelements=dict()):
        # miros are in grams per 100g
        self.microelements = microelements


class FoodProductScanner:
    """
    scanner in resource (may be a text file)
    """
