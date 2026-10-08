# Vehicle.py
# Encapsulation

from abc import ABC, abstractmethod

# Parent class
class Vehicle(ABC):
    def __init__(self, registration_number, make, model, year, daily_rate):
        if daily_rate < 0:
            raise ValueError("Daily rate cannot be negative")
        
        self.registration_number = registration_number
        self.make = make
        self.year = year
        self.model = model
        self.daily_rate = daily_rate
        self.__available = True 
    
    def display_details(self):
            status = "Available" if self.__available else "Rented"
            print(f"{self.year} {self.make} {self.model} ({self.registration_number}) - {status}")


    # Properties
    def is_available(self):
        return self.__available

    def mark_as_available(self):
        self.__available = True
    
    def mark_as_rented(self):
        self.__available = False

    

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    @abstractmethod
    def get_vehicle_type():
        pass

    
    


class EconomyCar(Vehicle):
     def calculate_rental_cost(self, days):

        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        return self.daily_rate * days


     def get_vehicle_type(self):
            return "EconomyCar"
        
class SUV(Vehicle):
    def calculate_rental_cost(self, days):

        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")
        # SUVs: daily_rate × days + one-time service charge
        return (self.daily_rate * days) + 2000

    def get_vehicle_type(self):
            return "SUV"



class LuxuryCar(Vehicle):
    def calculate_rental_cost(self, days):

        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        # 10% premium for luxury cars
        base = self.daily_rate * days
        insurance = base * 0.10
        return base + insurance

    def get_vehicle_type(self):
            return "LuxuryCar"




