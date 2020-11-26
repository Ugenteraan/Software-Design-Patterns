'''
Contains class(es) (known as Context) that manages all the strategies. Client will only communicate with this class and not the discount strategies directly.
In this example, there's only one context and that is to manage the discount strategies.
'''

from meta_classes import Contexts
import discounts

class DiscountContext(Contexts):

    def list_strategies(self):
        '''
        Returns all the available strategies in a list as strings.
        '''
        #the objects for the discount strategies can only be accessed with self.
        self.strategies = {
            'ChristmasStrategy' : discounts.ChristmasDiscount,
            'ThanksgivingStrategy' : discounts.ThanksgivingDiscount,
            'NormalStrategy' : discounts.NormalDiscount
        }

        return self.strategies.keys() #return only the keys.


    def __init__(self, price, strategy):
        '''
        Calculates the discount based on the given strategy.
        '''

        if not strategy in self.list_strategies():
            raise ValueError("The given strategy does not exist! Use list_strategies method to check all the available strategies.")

        self.price = price
        self.discount_strategy = self.strategies[strategy] #holds the object of the selected strategy class.
        self.discounted_price = price #by default it's the same as the original price.


    def perform_operation(self):
        '''
        Perform the discount calculation and returns the discounted price.
        '''
        chosen_strategy = self.discount_strategy(self.price)
        return chosen_strategy.calculate_discount()
