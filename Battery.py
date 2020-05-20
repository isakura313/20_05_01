class Battery():
    """ Простой класс аккумулятора, который может обслуживать наш автомобиль"""

    def __init__(self, battery_size = 120):
        self.battery_size = battery_size
    def show_akk(self):
        print(str(self.battery_size) + " осталось")