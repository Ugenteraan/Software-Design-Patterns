'''
Concrete Classes for every brand of cars.
'''

from meta_classes import Car
import costs


class Honda(Car):
    '''
    Creates Honda car class. Inherits the interface Car.
    '''


    cost = 0

    def create_door(self):
        '''
        Creates Honda doors.
        '''
        self.cost += costs.car_doors['Honda']
        print("Honda door is added to the Honda car!")

    def create_car_body(self):
        '''
        Creates the Honda car body.
        '''
        self.cost += costs.car_body['Honda']
        print("Honda body is added to the Honda car!")

    def create_tyres(self):
        '''
        Creates the Honda car tyres.
        '''
        self.cost += costs.car_tyres['Honda']
        print("Honda tyres are added to the Honda car!")


class Toyota(Car):
    '''
    Creates Toyota car class. Inherits the interface Car.
    '''

    cost = 0

    def create_door(self):
        '''
        Creates Toyota doors.
        '''
        self.cost += costs.car_doors['Toyota']
        print("Toyota door is added to the Toyota car!")

    def create_car_body(self):
        '''
        Creates the Toyota car body.
        '''
        self.cost += costs.car_body['Toyota']
        print("Toyota body is added to the Toyota car!")

    def create_tyres(self):
        '''
        Creates the Toyota car tyres.
        '''
        self.cost += costs.car_tyres['Toyota']
        print("Toyota tyres are added to the Toyota car!")

class Suzuki(Car):
    '''
    Creates Suzuki car class. Inherits the interface Car.
    '''

    cost = 0

    def create_door(self):
        '''
        Creates Suzuki doors.
        '''
        self.cost += costs.car_doors['Suzuki']
        print("Suzuki door is added to the Suzuki car!")

    def create_car_body(self):
        '''
        Creates the Suzuki car body.
        '''
        self.cost += costs.car_body['Suzuki']
        print("Suzuki body is added to the Suzuki car!")

    def create_tyres(self):
        '''
        Creates the Suzuki car tyres.
        '''
        self.cost += costs.car_tyres['Suzuki']
        print("Suzuki tyres are added to the Suzuki car!")

class Nissan(Car):
    '''
    Creates Nissan car class. Inherits the interface Car.
    '''

    cost = 0

    def create_door(self):
        '''
        Creates Nissan doors.
        '''
        self.cost += costs.car_doors['Nissan']
        print("Nissan door is added to the Nissan car!")

    def create_car_body(self):
        '''
        Creates the Nissan car body.
        '''
        self.cost += costs.car_body['Nissan']
        print("Nissan body is added to the Nissan car!")

    def create_tyres(self):
        '''
        Creates the Nissan car tyres.
        '''
        self.cost += costs.car_tyres['Nissan']
        print("Nissan tyres are added to the Nissan car!")
