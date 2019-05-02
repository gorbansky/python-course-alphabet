"""
Вам небхідно написати 3 класи. Мільйонери Гаражі та Автомобілі.
Звязкок наступний один мільйонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""

from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from uuid import uuid4
from typing import List


class CustomException(Exception):
    def __init__(self, message):
        self.message = message


class Car:

    def __init__(self, price, type, producer, mileage):

        errorStack = ''

        if not isinstance(price, int) and not isinstance(price, float):
            errorStack += "\n'Price' argument should be numeric\n"

        if not isinstance(mileage, int) and not isinstance(mileage, float):
            errorStack += "\n'Mileage' argument should be numeric\n"

        if type not in CARS_TYPES:
            errorStack += "\nIncorrect value for 'Type' argument\n"

        if producer not in CARS_PRODUCER:
            errorStack += "\nIncorrect value for 'Producer' argument\n"

        if errorStack:
            raise CustomException(errorStack)

        self.price = float(price)
        self.type = type
        self.producer = producer
        self.mileage = float(mileage)
        self.id = uuid4()

    def __str__(self):
        return "Price: ${}, Type: {}, Producer: {}, Id: {}, Mileage: {}"\
                .format(self.price, self.type, self.producer, self.id, self.mileage)

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def ChangeId(self):
        self.id = uuid4()


class Garage:

    cars: List[Car]

    def enoughSpace(self):
        return self.places-len(self.cars) >= 0

    def __init__(self, town, places, cars=None, owner=None):

        errorStack = ''

        if not isinstance(places, int):
            errorStack += "\n'Places' argument should be 'int'\n"

        if places <= 0:
            errorStack += "\n'Places' argument should be greater than 0\n"

        if town not in TOWNS:
            errorStack += "\nIncorrect value for 'Town' argument\n"

        if errorStack:
            raise CustomException(errorStack)

        self.town = town
        self.cars = cars if cars is not None else []
        self.places = places
        self.owner = owner

        if not self.enoughSpace():
            raise CustomException("\nThere is no enough free places in garage\n")

    def __str__(self):
        return "Town: {}, Cars: {}, Places: {}, Owner: {}"\
                .format(self.town, len(self.cars), self.places, self.owner)

    def remove(self, car):
        if car in self.cars:
            self.cars.remove(car)
        else:
            raise CustomException("\nCar doesn`t exists in this garage\n")

    def add(self, car):
        if car not in self.cars:
            self.cars.append(car)
        else:
            raise CustomException("\nCar already exists in this garage\n")
        if not self.enoughSpace():
            self.remove(car)
            raise CustomException("\nThere is no enough free places in garage\n")

    def hit_hat(self):
        return sum([car.price for car in self.cars])


class Millionaire:
    pass




######################################
'''
try:
    c1 = Car(price='10000', type='Seda', producer='Bugatt', mileage='100')
except CustomException as err:
    print("c1", err, "\n")

try:
    c1 = Car(price=10000, type='Sedan', producer='Bugatt', mileage=100)
except CustomException as err:
    print("c1", err, "\n")

try:
    c1 = Car(price=10000, type='Seda', producer='Bugatti', mileage=100)
except CustomException as err:
    print("c1", err, "\n")

try:
    c1 = Car(price='10000', type='Sedan', producer='Bugatti', mileage='100')
except CustomException as err:
    print("c1", err, "\n")

try:
    c1 = Car(price=10000, type='Sedan', producer='Bugatti', mileage='100')
except CustomException as err:
    print("c1", err, "\n")

try:
    c1 = Car(price='10000', type='Sedan', producer='Bugatti', mileage=100)
except CustomException as err:
    print("c1", err, "\n")

c1 = Car(price=10000, type='Sedan', producer='Bugatti', mileage=100)

print("c1", c1, "\n")

c1.ChangeId()

print("c1", c1, "\n")

c2 = Car(price=20000, type='Truck', producer='Ford', mileage=90000)

print("c2", c2, "\n")

print("c2 == c1", c2 == c1, "\n")

print("c2 > c1", c2 > c1, "\n")

print("c2 >= c1", c2 >= c1, "\n")

print("c2 < c1", c2 < c1, "\n")

print("c2 <= c1", c2 <= c1, "\n")

print("c2 != c1", c2 != c1, "\n")
'''

g1 = Garage('Kiev', 2)
c1 = Car(price=10000, type='Sedan', producer='Bugatti', mileage=100)
c2 = Car(price=20000, type='Truck', producer='Ford', mileage=90000)
print(1)
g1.add(c1)
print(g1)
print(2)
g1.add(c2)
print(g1)