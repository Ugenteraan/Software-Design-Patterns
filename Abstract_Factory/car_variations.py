'''
Variations of cars.
'''

from meta_classes import Car
import costs


class ToyotaCorolla(Car):
    '''
    Creates Toyota Corolla car class. Inherits the interface Car.
    '''

    cost = 0

    def create_door(self):
        '''
        Creates Toyota Corolla doors.
        '''
        self.cost += costs.car_doors['toyota']['corolla']
        print("Toyota Corolla door is added to the Toyota Corolla car!")

    def create_car_body(self):
        '''
        Creates the Toyota Corolla car body.
        '''
        self.cost += costs.car_body['toyota']['corolla']
        print("Toyota Corolla body is added to the Toyota Corolla car!")

    def create_tyres(self):
        '''
        Creates the Toyota Corolla car tyres.
        '''
        self.cost += costs.car_tyres['toyota']['corolla']
        print("Toyota Corolla tyres are added to the Toyota Corolla car!")


class ToyotaVios(Car):
    '''
    Creates Toyota Vios car class. Inherits the interface Car.
    '''

    cost = 0

    def create_door(self):
        '''
        Creates Toyota Vios doors.
        '''
        self.cost += costs.car_doors['toyota']['vios']
        print("Toyota Vios door is added to the Toyota Vios car!")

    def create_car_body(self):
        '''
        Creates the Toyota Vios car body.
        '''
        self.cost += costs.car_body['toyota']['vios']
        print("Toyota Vios body is added to the Toyota Vios car!")

    def create_tyres(self):
        '''
        Creates the Toyota Vios car tyres.
        '''
        self.cost += costs.car_tyres['toyota']['vios']
        print("Toyota Vios tyres are added to the Toyota Vios car!")

class NissanAlmera(Car):
    '''
    Creates Nissan Almera car class. Inherits the interface Car.
    '''

    cost = 0

    def create_door(self):
        '''
        Creates Nissan Almera doors.
        '''
        self.cost += costs.car_doors['nissan']['almera']
        print("Nissan Almera door is added to the Nissan Almera car!")

    def create_car_body(self):
        '''
        Creates the Nissan Almera car body.
        '''
        self.cost += costs.car_body['nissan']['almera']
        print("Nissan Almera body is added to the Nissan Almera car!")

    def create_tyres(self):
        '''
        Creates the Nissan Almera car tyres.
        '''
        self.cost += costs.car_tyres['nissan']['almera']
        print("Nissan Almera tyres are added to the Nissan Almera car!")

class NissanSerena(Car):
    '''
    Creates Nissan Serena car class. Inherits the interface Car.
    '''

    cost = 0

    def create_door(self):
        '''
        Creates Nissan Serena doors.
        '''
        self.cost += costs.car_doors['nissan']['serena']
        print("Nissan Serena door is added to the Nissan Serena car!")

    def create_car_body(self):
        '''
        Creates the Nissan Serena car body.
        '''
        self.cost += costs.car_body['nissan']['serena']
        print("Nissan Serena body is added to the Nissan Serena car!")

    def create_tyres(self):
        '''
        Creates the Nissan Serena car tyres.
        '''
        self.cost += costs.car_tyres['nissan']['serena']
        print("Nissan Serena tyres are added to the Nissan Serena car!")


class HondaAccord(Car):
    '''
    Creates Honda Accord car class. Inherits the interface Car.
    '''

    cost = 0

    def create_door(self):
        '''
        Creates Honda Accord doors.
        '''
        self.cost += costs.car_doors['honda']['accord']
        print("Honda Accord door is added to the Honda Accord car!")

    def create_car_body(self):
        '''
        Creates the NHonda Accord car body.
        '''
        self.cost += costs.car_body['honda']['accord']
        print("Honda Accord body is added to the Honda Accord car!")

    def create_tyres(self):
        '''
        Creates the Honda Accord car tyres.
        '''
        self.cost += costs.car_tyres['honda']['accord']
        print("Honda Accord tyres are added to the Honda Accord car!")

class HondaCivic(Car):
    '''
    Creates Honda Civic car class. Inherits the interface Car.
    '''

    cost = 0

    def create_door(self):
        '''
        Creates Honda Civic doors.
        '''
        self.cost += costs.car_doors['honda']['civic']
        print("Honda Civic door is added to the Honda Civic car!")

    def create_car_body(self):
        '''
        Creates the Honda Civic car body.
        '''
        self.cost += costs.car_body['honda']['civic']
        print("Honda Civic body is added to the Honda Civic car!")

    def create_tyres(self):
        '''
        Creates the Honda Civic car tyres.
        '''
        self.cost += costs.car_tyres['honda']['civic']
        print("Honda Civic tyres are added to the Honda Civic car!")
