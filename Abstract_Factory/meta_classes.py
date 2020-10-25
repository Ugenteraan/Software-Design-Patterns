'''
Abstract and Interface classes.
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
    Interface class for the car factories.
    '''

    @abstractmethod
    def factory_call(self):

        pass


class AbstractFactory(metaclass=ABCMeta):
    '''
    Abstract class for the abstract car factories.
    '''

    @abstractmethod
    def create_factory(self):
        pass

    def manufacture_car(self, requested_car_brand, requested_car_model):
        '''
        Manufacture the requested car model upon invocation. (Default implementation!)
        '''

        factory_obj = self.create_factory(requested_car_brand=requested_car_brand)
        car_model_obj = factory_obj.factory_call(requested_car_model=requested_car_model)
        car_model_obj.create_car_body()
        car_model_obj.create_door()
        car_model_obj.create_tyres()

        return car_model_obj
