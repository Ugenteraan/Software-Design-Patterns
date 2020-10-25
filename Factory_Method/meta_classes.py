'''
Interface for every brand of cars.
'''

from abc import ABCMeta, abstractmethod


class Car(metaclass=ABCMeta):
    '''
    Interface for every brand of cars.
    '''
    @property
    def cost(self):
        raise NotImplementedError

    @abstractmethod
    def create_door(self):
        #You can also provide a default implementation for this method.
        pass

    @abstractmethod
    def create_car_body(self):
        #You can also provide a default implementation for this method.
        pass

    @abstractmethod
    def create_tyres(self):
        #You can also provide a default implementation for this method.
        pass


class Factory(metaclass=ABCMeta):
    '''
    Abstract class for the factories.
    '''

    @abstractmethod
    def factory_call(self):

        pass

    def manufacture_car(self, requested_car):
        '''
        Manufacture the requested car upon invocation. (Default implementation!)
        '''
        obj = self.factory_call(requested_car=requested_car)
        obj.create_car_body()
        obj.create_door()
        obj.create_tyres()

        return obj