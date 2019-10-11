from test.car import Car
from test.my_Electric import ElectricCar

my_tesla = ElectricCar('teslas', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

my_beetele = Car('volkswagen', 'beetle', 2016)
print("\n\n" + my_beetele.get_descriptive_name())