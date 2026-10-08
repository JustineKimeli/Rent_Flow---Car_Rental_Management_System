from vehicle import EconomyCar,SUV, LuxuryCar
from Customer import Customer
from Payment import MpesaPayment
from Rental_system import CarRentalSystem


system = CarRentalSystem("SafariDrive Rentals")


# Adding vehicles
car1 = EconomyCar("KDK 123A", "Toyota", "Axio", 2022, 4000)
car2 = SUV("KDJ 456B", "Toyota", "Prado", 2023, 8000)
car3 = LuxuryCar("KDJ 672B", "Nissan", "X-Trail", 2021, 6500)
car4 = LuxuryCar("KDL 789C", "Mercedes-Benz", "E-Class", 2024, 15000)


for car in [car1, car2, car3, car4]:
    system.add_vehicle(car)

# Customer registration
customer1 = Customer("C001", "James Mbugua", "0718583206", "87654321", "DL46831")
system.register_customer(customer1)


# Renting Mercedes-Benz for 5 days
system.show_available_vehicles()
rental1 = system.rent_vehicle(customer1, car4, 5)
rental1.display_rental_details()


# Trial
try:
    system.rent_vehicle(customer1, car2,2)
except ValueError as error:
    print(f"Error: {error}")

# Return the vehicle 2 days late
system.return_vehicle(rental1, actual_days =6)
payment1 = MpesaPayment(rental1, "0718583206")
system.process_payment(payment1)


system.generate_report()
