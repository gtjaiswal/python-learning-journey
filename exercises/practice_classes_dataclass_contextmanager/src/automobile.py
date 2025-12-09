class Vehicle:

    def __init__(self, brand:str, model : str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Year: {self.year} Brand: {self.brand} Model: {self.model}"

class Car(Vehicle):
    def __init__(self, brand:str, model : str, year: int, num_doors : int):
        super().__init__(brand,model,year)
        self.num_doors = num_doors

    def get_info(self):
        return super().get_info()+ f" (Doors: {self.num_doors})"

class ElectricCar(Car):
    def __init__(self, brand:str, model : str, year: int, num_doors : int, battery_capacity:int):
        super().__init__(brand,model, year,num_doors)
        self.battery_capacity = battery_capacity

    def get_info(self):
        return super().get_info()+ f" Battery Capacity: {self.battery_capacity})"

if __name__ =="__main__":
    # Test it:
    vehicle = Vehicle("Toyota", "Generic", 2020)
    car = Car("Honda", "Civic", 2021, 4)
    ev = ElectricCar("Tesla", "Model 3", 2023, 4, 75)
    print(vehicle.get_info())
    print(car.get_info())
    print(ev.get_info())