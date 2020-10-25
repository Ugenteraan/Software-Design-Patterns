'''
Python implementation of the Factory Design Pattern.

The example code here illustrates how a car manufacturing company that manufactures different brand of cars such as Toyota, Honda, and Nissan may write
their software logics using the Factory method.
'''


from factories import CarFactory

def client_code(requested_car):
    '''
    Receives the request from the client to create a specific car and get the cost of manufacturing the car.
    '''
    #use the factory to manufacture and get the desired object of the car.
    car_object = CarFactory().manufacture_car(requested_car=requested_car)

    return car_object



manufacture_cars = ['Honda', 'Suzuki', 'Toyota', 'Nissan', 'Ferrari', 'Toyota']

for car in manufacture_cars:

    obj = client_code(car)
    print("The %s car you requested is now completed! The total cost of the manufacture is : RM %g"%(car, obj.cost))
