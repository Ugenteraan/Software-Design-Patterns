'''
Contains all the meta classes that must be inherited by certain classes.
'''

from abc import ABCMeta, abstractmethod, abstractstaticmethod


class Contexts(metaclass=ABCMeta):
    '''
    Interface for the context classes.
    '''
    @abstractmethod
    def list_strategies(self):
        '''
        Lists all the available strategies to the client side.
        '''
        pass

    @abstractmethod
    def perform_operation(self):
        '''
        The context classes are implemented to perform a certain operation. Hence this method.
        '''
        pass


class Discounts(metaclass=ABCMeta):
    '''
    Interface for the discount classes.
    '''

    @abstractmethod
    def calculate_discount(self):
        '''
        Calculates the discount and returns the discounted price.
        '''
        pass
