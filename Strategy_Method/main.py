'''
Python implementation of the Strategy Design Pattern.

The example code here illustrates how a food ordering app manages many promotions and discounts that may be given to users at different occasions.
'''

from discount_strategies import DiscountContext


def calculate_discount(price, occasion=None):
    '''
    Calculates the price of an item after discount.
    '''

    item_price = price

    if occasion == 'Christmas':
        discounted_price = DiscountContext(item_price, strategy='ChristmasStrategy').perform_operation()
    elif occasion == 'Thanksgiving':
        discounted_price = DiscountContext(item_price, strategy='ThanksgivingStrategy').perform_operation()
    elif occasion == 'Normal':
        discounted_price = DiscountContext(item_price, strategy='NormalStrategy').perform_operation()
    else:
        raise ValueError("There are no such occasion!")

    return discounted_price


if __name__ == '__main__':

    print(calculate_discount(1000, 'Christmas'))