'''
Abstract factory that creates the Factory for each brand of car.
'''

from factories import *
from meta_classes import AbstractFactory

class AbstractCarFactory(AbstractFactory):
    '''
    Abstract factory that manages all the car brands and their models.
    '''

    def create_factory(self, requested_car_brand):
        '''
        Returns the object of the factory of a certain car brand.
        '''

        car_factories = {
            'Honda' : HondaFactory(),
            'Nissan' : NissanFactory(),
            'Toyota' : ToyotaFactory()
        }

        try:
            return car_factories[requested_car_brand]
        except KeyError as err:
            raise KeyError("The requested brand of car : %s is not found!"%(requested_car_brand))
