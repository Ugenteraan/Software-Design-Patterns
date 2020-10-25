'''
Factory for the car objects.
'''

from cars import Honda, Toyota, Suzuki, Nissan
from meta_classes import Factory

class CarFactory(Factory):

    def factory_call(self, requested_car):
        '''
        Returns the object of the desired car.
        '''

        car_brands = {
            'Honda' : Honda(),
            'Nissan': Nissan(),
            'Suzuki': Suzuki(),
            'Toyota': Toyota()
        }

        try:
            return car_brands[requested_car]
        except KeyError as err:
            raise ValueError("The requested car : %s is not found in the factory!"%(requested_car))
