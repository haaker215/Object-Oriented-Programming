class vehicle:
    def __init__(self,mileage,name,speed):
        self.mileage = mileage
        self.name = name
        self.speed = speed
class bus(vehicle):
    pass
obj = bus("Volvo",120,20)
print(obj.name)
print(obj.mileage)
print(obj.speed)