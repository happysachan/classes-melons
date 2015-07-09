"""This file should have our melon-type classes in it."""
class Melon(object):
    def __init__(self, base_cost=5):
        if self.species in ["Casaba", "Ogens"]: #this string is in this list of strings
            self.base_cost = base_cost + 1
        else:
            self.base_cost = base_cost

        if self.imported == True:
            self.base_cost = self.base_cost * 1.5
        else:
            self.base_cost = self.base_cost

        if self.shape == "square":
            self.base_cost = self.base_cost * 2
        else:
            self.base_cost = self.base_cost
            
class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = float(self.base_cost * qty)   
        if qty < 3:
            pass 
        else:
            total = total * .75
        return total

class CantaloupeOrder(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']


    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = float(self.base_cost * qty)  
        if qty < 5:
            pass 
        else:
            total = total * .5
        return total

class CasabaOrder(Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = float(self.base_cost * qty)  
        return total

class SharlynOrder(Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = float(self.base_cost * qty)  
        return total


class SantaClausOrder(Melon):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = float(self.base_cost * qty)  
        return total

class ChristmasOrder(Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = float(self.base_cost * qty)  
        return total


class HornedMelonOrder(Melon):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = float(self.base_cost * qty)  
        return total


class XiguaOrder(Melon):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']


    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = float(self.base_cost * qty)  
        return total


class OgenOrder(Melon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Summer', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = float(self.base_cost * qty)  
        return total