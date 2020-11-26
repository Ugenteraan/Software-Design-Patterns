'''
The discount algorithms that takes the original price as an input and calculates discount based on a certain occasion and returns the discounted price.
'''

from meta_classes import Discounts



class ChristmasDiscount(Discounts):
    '''
    Calculates the discount for the Christmas occasion.
    '''

    def __init__(self, price):
        '''
        Initialize parameters.
        '''
        self.price = price

    def calculate_discount(self):
        '''
        Discount calculation for the Christmas occasion.
        '''
        return self.price - self.price*0.2 #20% discount.

class ThanksgivingDiscount(Discounts):
    '''
    Calculates the discount for the Thanksgiving occasion.
    '''

    def __init__(self, price):
        '''
        Initialize parameters.
        '''
        self.price = price


    def calculate_discount(self):
        '''
        Discount calculation for the Thanksgiving occasion.
        '''
        return self.price - self.price*0.1 #10% discount.

class NormalDiscount(Discounts):
    '''
    Calculates the discount for the Normal days.
    '''

    def __init__(self, price):
        '''
        Initialize parameters.
        '''
        self.price = price


    def calculate_discount(self):
        '''
        Discount calculation for the Normal days.
        '''
        return self.price - self.price*0.0 #No discount on normal days.
