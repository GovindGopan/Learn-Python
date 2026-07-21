class Vehicle:
    def __init__(self,_vehicle_id,_base_rate):
        self._vehicle_id = _vehicle_id
        self._base_rate = _base_rate
        
    def display_details(self):
        return ("vehicle id : {} , baserate : {}".format(self._vehicle_id,self._base_rate))
    
    def rental_charges(self):
        return 0.0
    
class Car(Vehicle):
    def __init__(self, _vehicle_id, _base_rate,num_seats):
        super().__init__(_vehicle_id, _base_rate)
        self.num_seats = num_seats
        
    def rental_charges(self):
        return self._base_rate * self.num_seats
    
class Bike(Vehicle):
    def __init__(self, _vehicle_id, _base_rate,bike_type):
        super().__init__(_vehicle_id, _base_rate)
        self.bike_type = bike_type
        
    def rental_charges(self):
        return self._base_rate * 0.5
    
def calculate_rental():
    a = Vehicle("VEH01",80.00)
    b = Car("CAR001", 100.00, 4)
    c = Bike("BIKE001", 50.00, "Motorcycle")
    print(a.rental_charges())
    print(b.rental_charges())
    print(c.rental_charges())
        
        
calculate_rental()