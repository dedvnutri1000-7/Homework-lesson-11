class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def plus_speed(self):
        self.__speed += 5

    def minus_speed(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def rotate_speed(self):
        self.__speed *= -1

Tesla = Car('Tesla', 'M', 1999)
Tesla.plus_speed()
