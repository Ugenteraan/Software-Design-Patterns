'''
Factories for each brand of car.
'''

from car_variations import *
from meta_classes import Factory


class HondaFactory(Factory):
    '''
    Factory for the Honda car models.
    '''

    def factory_call(self, requested_car_model):
        '''
        Returns the desired Honda car model object.
        '''

        car_variation = {
            'Accord' : HondaAccord(),
            'Civic' : HondaCivic()
        }

        try:
            return car_variation[requested_car_model]
        except KeyError as err:
            raise ValueError("The requested car : Honda %s is not found in the factory!"%(requested_car_model))

class ToyotaFactory(Factory):
    '''
    Factory for the Toyota car models.
    '''

    def factory_call(self, requested_car_model):
        '''
        Returns the desired Toyota car model object.
        '''

        car_variation = {
            'Corolla' : ToyotaCorolla(),
            'Vios' : ToyotaVios()
        }

        try:
            return car_variation[requested_car_model]
        except KeyError as err:
            raise ValueError("The requested car : Toyota %s is not found in the factory!"%(requested_car_model))

class NissanFactory(Factory):
    '''
    Factory for the Nissan car models.
    '''

    def factory_call(self, requested_car_model):
        '''
        Returns the desired Nissan car model object.
        '''

        car_variation = {
            'Almera' : NissanAlmera(),
            'Serena' : NissanSerena()
        }

        try:
            return car_variation[requested_car_model]
        except KeyError as err:
            raise ValueError("The requested car : Nissan %s is not found in the factory!"%(requested_car_model))
