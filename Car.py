from Battery import *
class Car:
    """ Базовый класс автомобиля"""

    def __init__(self, marka, speed):
        """инициализирует атрибуты марки и скорости автомобиля"""
        self.marka = marka
        self.speed = speed
        self.odometr = 0

    def car_ride(self, hours = 0):
        amount = self.speed * hours
        print("Машина проехала" + str(amount) + " километров ")
        self.update_odometr(amount)
        # return
    def odometr_reading(self):
        """ Покажем пробег автомобиля"""
        print("У автомобиля пробег " + str(self.odometr) + " на счетчике")

    def update_odometr(self, kilomtrs):
        self.odometr = kilomtrs


class Tesla(Car):
    """ Представляет класс автомобиля с электродвигателем"""
    def __init__(self, marka, speed):
        """ инициалзирует атрибуты класса-родителя"""
        super().__init__(marka, speed)
        self.battery = Battery(240)
    @staticmethod
    def name_of_son_say():
        print("X-af-10")


