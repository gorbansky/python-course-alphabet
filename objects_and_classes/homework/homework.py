"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
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

    def __init__(self, price, car_type, producer, mileage):

        error_stack = ''

        if not isinstance(price, int) and not isinstance(price, float):
            error_stack += "\n'Price' argument should be numeric\n"

        if not isinstance(mileage, int) and not isinstance(mileage, float):
            error_stack += "\n'Mileage' argument should be numeric\n"

        if car_type not in CARS_TYPES:
            error_stack += "\nIncorrect value for 'Type' argument\n"

        if producer not in CARS_PRODUCER:
            error_stack += "\nIncorrect value for 'Producer' argument\n"

        if error_stack:
            raise CustomException(error_stack)

        self.__price = float(price)
        self.__car_type = car_type
        self.__producer = producer
        self.__mileage = float(mileage)
        self.__id = uuid4()
        self.__in_garage = False
        self.__flag = True

    def __str__(self):
        return "Price: ${}, Type: {}, Producer: {}, Id: {}, Mileage: {}"\
                .format(self.__price, self.__car_type, self.__producer, self.__id, self.__mileage)

    def __eq__(self, other):
        return self.__price == other.price

    def __ne__(self, other):
        return self.__price != other.price

    def __gt__(self, other):
        return self.__price > other.price

    def __ge__(self, other):
        return self.__price >= other.price

    def __lt__(self, other):
        return self.__price < other.price

    def __le__(self, other):
        return self.__price <= other.price

    def __next__(self):
        if self.__flag:
            self.__flag = False
            return self
        else:
            self.__flag = True
            raise StopIteration

    def __iter__(self):
        return self

    def change_id(self):
        self.__id = uuid4()

    def get_price(self):
        return self.__price

    def get_id(self):
        return self.__id

    def set_garage(self, flag):
        self.__in_garage = flag

    def is_in_garage(self):
        return self.__in_garage


class Garage:

    cars: List[Car]

    def enough_space(self):
        return self.places-len(self.cars) >= 0

    def rollback(self, cars):
        for v_car in cars:
            v_car.set_garage(False)

    def __init__(self, town, places, cars=None, owner=None):

        error_stack = ''
        rollback_list = []

        if not isinstance(places, int):
            error_stack += "\n'Places' argument should be 'int'\n"

        if places <= 0:
            error_stack += "\n'Places' argument should be greater than 0\n"

        if town not in TOWNS:
            error_stack += "\nIncorrect value for 'Town' argument\n"

        if cars:
            for v_car in cars:
                if v_car.is_in_garage():
                    error_stack += "\nCar with id "+str(v_car.id)+" can not be added to more than one garage\n"
                else:
                    v_car.set_garage(True)
                    rollback_list.append(v_car)

        if error_stack:
            self.rollback(rollback_list)
            raise CustomException(error_stack)

        self.__town = town
        self.cars = cars if cars is not None else []
        self.places = places
        self.owner = owner
        self.flag = True

        if not self.enough_space():
            self.rollback(rollback_list)
            raise CustomException("\nThere is no enough free places in garage\n")

        rollback_list.clear()

    def __str__(self):
        return "Town: {}, Cars: {}, Places: {}, Owner: {}"\
                .format(self.__town, len(self.cars), self.places, self.owner)

    def __next__(self):
        if self.flag:
            self.flag = False
            return self
        else:
            self.flag = True
            raise StopIteration

    def __iter__(self):
        return self

    def __lt__(self, other):
        return self.free_space() < other.free_space()

    def __contains__(self, car):
        return car.get_id() in (v_car.get_id() for v_car in self.cars)

    def remove(self, car):
        if car in self.cars:
            self.cars.remove(car)
            car.set_garage(False)
        else:
            raise CustomException("\nCar with id "+str(car.get_id())+" doesn`t exists in this garage\n")

    def add(self, car):
        if car not in self and not car.is_in_garage():
            self.cars.append(car)
            car.set_garage(True)
        else:
            raise CustomException("\nCar with id "+str(car.get_id())+" already exists in garage\n")
        if not self.enough_space():
            self.remove(car)
            raise CustomException("\nThere is no enough free places in garage\n")

    def hit_hat(self):
        return sum([car.get_price() for car in self.cars])

    def set_owner(self, owner_id=None):
        self.owner = owner_id

    def free_space(self):
        return self.places-len(self.cars)


class Millionaire:

    garages = List[Garage]

    def rollback(self, garages):
        for v_garage in garages:
            v_garage.set_owner()

    def __init__(self, name, garages=None):

        error_stack = ''
        rollback_list = []

        self.name = str(name)
        self.register_id = uuid4()

        if garages:
            self.garages = garages
            for v_garage in garages:
                if v_garage.owner:
                    error_stack += "\nGarage can not be assigned to more than one owner\n"
                else:
                    v_garage.set_owner(self.register_id)
                    rollback_list.append(v_garage)
        else:
            self.garages = []

        if error_stack:
            self.rollback(rollback_list)
            raise CustomException(error_stack)

        rollback_list.clear()

    def __str__(self):
        return "Name: {}, Garages: {}, Cars: {}, Total cars cost: {}" \
            .format(self.name, self.garages_count(), self.cars_count(), self.hit_hat())

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __ne__(self, other):
        return self.hit_hat() != other.hit_hat()

    def hit_hat(self):
        return sum(map(lambda garage: garage.hit_hat(), self.garages))

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum(map(lambda garage: len(garage.cars), self.garages))

    def add_car(self, car, garage=None):
        if garage:
            if garage in self.garages:
                garage.add(car)
            else:
                raise CustomException("\n"+self.name+" is not owner of this garage\n")
        else:
            self.garages.sort(reverse=True)
            self.garages[0].add(car)

