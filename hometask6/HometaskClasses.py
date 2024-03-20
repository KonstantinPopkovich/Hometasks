from enum import Enum
from dataclasses import dataclass

class CarEnum(Enum):
    Peugeot = "Peugeot"
    Mercedes = "Mercedes"
    BMW = "BMW"
    Porsche = "Porsche"

@dataclass
class CarCenter:
    wheels = 4
    engine = "benzin" or "electricity"
    cars_itself: CarEnum
    model: str
    year: int
    price: float

    def __init__(self, cars_itself, model, year, price):
        self._cars_itself = cars_itself
        self._model = model
        self._year = year
        self._price = price

    @property
    def cars_itself(self):
        return self._cars_itself

    @cars_itself.setter
    def cars_itself(self, value):
        self._cars_itself = value

    @cars_itself.deleter
    def cars_itself(self):
        del self._cars_itself

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @model.deleter
    def model(self):
        del self._model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @year.deleter
    def year(self):
        del self._year

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

    @property
    def formatted_price(self):
        return f"${self._price}$"

    @staticmethod
    def price_with_discount(price, discount: int):
        return price * (1 - discount / 100)

    @classmethod
    def create_from_string(cls, car_string: str):
        cars_itself, model, year, price = car_string.split(",")
        return cls(CarEnum[cars_itself], model, int(year), float(price))
#car = CarCenter.create_from_string("BMW,X5,2023,20000.0")

#def __str__(self):
    #return f"{self.year} {selfcars_itself.value} {self.model} {self.formatted_price}"

    def __str__(self):
        return (f"{self.cars_itself.value} {self.model} {self.year} {self.formatted_price} "
                f"${self.price_with_discount(self._price,15)}$"
                )

class Car_Equality(CarCenter):

    def __eq__(self, other):
        if isinstance(other, Car_Equality):
            return self.price == other.price
        raise ValueError(f"I cannot compare with {type(other)}")

    def __lt__(self, other):
        if isinstance(other, Car_Equality):
            return self.price < other.price
        raise ValueError(f"I cannot compare with {type(other)}")

    def __le__(self, other):
        if isinstance(other, Car_Equality):
            return self.price <= other.price
        raise ValueError(f"I cannot compare with {type(other)}")

    def __gt__(self, other):
        if isinstance(other, Car_Equality):
            return self.price > other.price
        raise ValueError(f"I cannot compare with {type(other)}")

    def __ge__(self, other):
        if isinstance(other, Car_Equality):
            return self.price >= other.price
        raise ValueError(f"I cannot compare with {type(other)}")

    def __add__(self, other):
        if isinstance(other, Car_Equality):
            return self.price + other.price
        raise ValueError(f"I cannot add with {type(other)}")

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.price + other
        raise ValueError(f"I cannot add with {type(other)}")

car1 = Car_Equality(CarEnum.Peugeot, "306_Universal", 1997, 2500.0)
car2 = Car_Equality(CarEnum.BMW, "x5", 2023, 20000.0)

print(car1 == car2)
print(car1 < car2)
print(car1 <= car2)
print(car1 > car2)
print(car1 >= car2)
print(car1 + car2)
print(1000000 + car1)

class ElectricCarEnum(Enum):
    Tesla = "Tesla"
    BMW = "BMW"
    Nissan = "Nissan"

class ElectricCar(CarCenter):
    def __init__(self, cars_itself, model, year, price, battery_capacity: float):
        super().__init__(cars_itself, model, year, price)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f"{super().__str__()} {self.battery_capacity} kWh"

car1 = Car_Equality(CarEnum.Peugeot, "306 Universal", 1997, 2500.0)
car2 = Car_Equality(CarEnum.BMW, "x5", 2023, 20000.0)
car3 = CarCenter(CarEnum.Porsche, "Cayenne", 2022, 55000.0)
print(car1)
print(car2)
print(car3)

electric_car1 = ElectricCar(ElectricCarEnum.Tesla, "Model S", 2023, 80000.0, 100)
electric_car2 = ElectricCar(ElectricCarEnum.Nissan, "Juke", 2022, 20000.0, 85)
print(electric_car1, electric_car2)

from enum import Enum
from abc import ABCMeta, abstractmethod

class BicycleModel(Enum):
    Aist = "Aist"
    GT = "GT"
    Stels = "Stels"
    Merida = "Merida"

class SellerMixin:
    def sell(self, model):
        if model in self.name:
            self.name.remove(model)
            print(f"Yes, we've got {model.value} bicycle.")
        else:
            print(f"Sorry, we don't have {model.value} bicycle.")

class Bicyclesection(SellerMixin, metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Hello, my name is Egor. How can I help you?")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("We're glad to see you as our customer. Bye!")

with Bicyclesection([BicycleModel.Aist, BicycleModel.GT, BicycleModel.Stels, BicycleModel.Merida]) as section:
    section.sell(BicycleModel.GT)


from abc import ABC, abstractmethod

def mister_dec (func):
    def wrapper(self):
        return f"Mister {func(self)}"
    return wrapper
class EmployeeABC(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @abstractmethod
    def sell(self):
        pass

class CarSeller(EmployeeABC):
    @mister_dec
    def sell(self):
        return f"{self.name} {self.surname} sells cars."

class ElectricCarSeller(EmployeeABC):
    @mister_dec
    def sell(self):
        return f"{self.name} {self.surname} sells electric cars."

class BicycleSeller(EmployeeABC):
    @mister_dec
    def sell(self):
        return f"{self.name} {self.surname} sells bicycles."

class CarAndElectricCarSeller(EmployeeABC):
    @mister_dec
    def sell(self):
        return f"{self.name} {self.surname} sells cars and electric cars."

ivan_ivanov = CarSeller("Ivan", "Ivanov")
sergey_sergeev = ElectricCarSeller("Sergey", "Sergeev")
egor_egorov = BicycleSeller("Egor", "Egorov")
anton_antonov = CarAndElectricCarSeller("Anton", "Antonov")

print(ivan_ivanov.sell())
print(sergey_sergeev.sell())
print(egor_egorov.sell())
print(anton_antonov.sell())