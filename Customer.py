# Customer.py
# Parent Class
class Customer:
    def __init__(self,customer_id, name, phone_number, national_id, driving_licence):
        if not driving_licence:
            raise ValueError("Customer must have driveing licence.")
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.national_id = national_id
        self.driving_licence = driving_licence
        self.rentals = []  # A list of new objects


    def display_info(self):
        print(f"Customer {self.customer_id} Name: {self.name}, Phone: {self.phone_number}")

    def add_rental(self,rental):
        self.rentals.append(rental)


    def view_rentals(self,rentals):
        if not self.rentals:
            print(f"{self.name} has no rental history.")

        else:
            print(f"Rental history for {self.name}")
            for rent in self.rentals:
                rent.display_rental_details()
        