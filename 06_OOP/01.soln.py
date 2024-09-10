class Car:   #This is Class
    total_car = 0
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
        Car.total_car += 1


    def get_brand(self):
        return self.brand + "!"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fule_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "car is a means of transport"
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


    def fule_type(self):
        return "Electric charge"

# my_tesla = ElectricCar("tesla", "model s", "87KWH")

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.full_name())
# print(my_tesla.fule_type())

punch = Car("tata", "punch")
fortuner = Car("totato","fortuner")
print(punch.fule_type())
print(fortuner.fule_type())
print(Car.total_car)
# print(my_tesla.general_description())



# my_car = Car("toyota", "fortuner")  #This is object
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("tata","punch")
# print(my_new_car.model)


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"
    
class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla= ElectricCarTwo("tesla", "model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())