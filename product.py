#!/usr/bin/env python
# -*- coding: utf-8 -*-

class FoodProduct:
    
    """
    General food product class
    """
    
    def __init__(self, name, macros, quantityToWeightRatio = 1, micros = None):
        self.name = name
        # ratio 1 - 1 unit = 1kg
        # ratio 2 - 1 unit = 0.5kg
        # ratio 0.5 - 1 unit = 2kg
        self.quantityToWeightRatio = quantityToWeightRatio
        self.macros = macros
        self.micros = micros


class Macros:
    """
    class representing macros for a food product
    """
    def __init__(self, carbs = 0, fats = 0, proteins = 0):
        #macros are in grams per 100g
        self.carbs = carbs
        self.fats = fats
        self.proteins = proteins

    def multiplyMacrosBy(self, multiple):
        self.carbs = self.carbs * multiple
        self.fats = self.fats * multiple
        self.proteins = self.proteins * multiple

    def addMacros(self, macrosToAdd):
        self.carbs += macrosToAdd.carbs
        self.fats += macrosToAdd.fats
        self.proteins += macrosToAdd.proteins



class Micros:
    """
    class representing micro elements for a food product
    """
    
    def __init__(self, microelements = dict()):
        #miros are in grams per 100g
        self.microelements = microelements

class FoodProductScanner:
    """
    scanner in resource (may be a text file)
    """





