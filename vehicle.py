from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year, mileage):
        self._brand = brand
        self._model = model
        self._year = year
        self._mileage = mileage

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def get_info(self):
        return f"{self.brand} {self.model}, {self.year}, Mileage: {self.mileage}"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value


    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value


    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        self._mileage = value

class Car(Vehicle):
    def __init__(self, brand, model, year, mileage, num_doors):
        super().__init__(brand, model, year, mileage)
        self._num_doors = num_doors

    def start(self):
        return f"{self.brand} {self.model} car"

    def stop(self):
        return f"{self.brand} {self.model} car"

    def open_trunk(self):
        return "The trunk is open."

    @property
    def num_doors(self):
        return self._num_doors

    @num_doors.setter
    def num_doors(self, value):
        self._num_doors = value

class Bicycle(Vehicle):
    def __init__(self, brand, model, year, mileage, gear_count):
        super().__init__(brand, model, year, mileage)
        self._gear_count = gear_count

    def start(self):
        return f"{self.brand} {self.model} bicycle is starting."

    def stop(self):
        return f"{self.brand} {self.model} bicycle is stopping."

    def ring_bell(self):
        return "idk"


    @property
    def gear_count(self):
        return self._gear_count

    @gear_count.setter
    def gear_count(self, value):
        self._gear_count = value
