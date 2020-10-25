'''
Python implementation of the Abstract Factory Design Pattern.

The example code here illustrate how a car manufacturing company that not only manufactures different brand of cars, but also different model of cars in
each brand may write their software logic using the Abstract Factory method.
'''

from abstract_factories import AbstractCarFactory

def client_code(requested_brand, requested_model):
    '''
    Receives the request from the client code to create a specific model of car and get the cost of the manufacturing.
    '''

    car_object = AbstractCarFactory().manufacture_car(requested_car_brand=requested_brand, requested_car_model=requested_model)

    return car_object


manufacture_cars = [['Honda', 'Civic'], ['Honda', 'Accord'], ['Toyota', 'Vios'], ['Toyota', 'Corolla'],
                    ['Nissan', 'Almera'], ['Nissan', 'Serena'], ['Toyota', 'Camry']]

for car in manufacture_cars:

    obj = client_code(car[0], car[1])
    print("The %s %s car you requested is now completed! The total cost of the manufacture is : RM %g"%(car[0], car[1], obj.cost))
