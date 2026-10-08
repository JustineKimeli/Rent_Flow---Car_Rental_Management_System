# RentFlow

**RentFlow** is a Python program, built with Object-Oriented Programming (OOP), that replaces the notebooks and spreadsheets used by **SafariDrive Rentals**, a growing car rental company in Kenya.

It keeps track of vehicles, customers, bookings, payments and returns, and answers the questions staff ask every day.

---

## The Problem

As the SafariDrive fleet grows, staff struggle to answer simple questions by hand. RentFlow answers each one:

| Question | RentFlow answer |
|----------|-----------------|
| Which vehicles are available right now? | `available_vehicles()` |
| Which vehicles are rented, and who has them? | `rented_vehicles()` |
| How long has each vehicle been out? | `rental.days_out()` |
| How much does a customer owe, and have they paid? | `rental.balance()` / `rental.is_fully_paid()` |
| Was a vehicle returned late? | `rental.is_late()` / `rental.days_late()` |
| How much money has the business made? | `total_revenue()` |

---

## Features

- Register and manage vehicles (available, rented, under maintenance)
- Register customers with ID and driving licence details
- Create bookings with automatic availability checks
- Record payments (cash, M-Pesa, card) against a rental, including part payments
- Process returns and detect late returns
- Calculate rental cost, late fees, amount paid and outstanding balance
- Generate reports: fleet status, active rentals, overdue rentals, customer balances, revenue


---

## OOP Design

### Classes

| Class | Responsibility |
|-------|----------------|
| `Vehicle` | Registration number, make, model, year, daily rate, status. Base class for vehicle types. |
| `Saloon`, `SUV`, `Van` | Subclasses of `Vehicle` with their own daily rates and rules. |
| `Customer` | Name, phone, national ID, licence number, list of rentals. |
| `Rental` | Links one customer to one vehicle. Holds start date, due date, return date, payments. Calculates days out, late days, total cost and balance. |
| `Payment` | Amount, method, date and the rental it belongs to. |
| `RentFlow` | The manager class. Stores all vehicles, customers and rentals, and provides the reports. |

### How the four OOP pillars are used

- **Encapsulation:** a vehicle's status and a rental's payments are changed only through methods (`rent()`, `return_vehicle()`, `add_payment()`), never edited directly.
- **Inheritance:** `Saloon`, `SUV` and `Van` extend `Vehicle`.
- **Polymorphism:** each vehicle type calculates its own daily rate, and `Rental` works the same way with any of them.
- **Abstraction:** staff call `rentflow.create_rental(...)` without needing to know how availability checks, cost maths or status updates work underneath.


## Project Structure

```
rentflow/
├── main.py                    # Menu- demo
├── Rental_Car_Flow/
│   ├── __init__.py
│   ├── Vehicle.py             # Vehicle, Saloon, SUV, Van
│   ├── Customer.py            # Customer
│   ├── Rental.py              # Rental
│   ├── Payment.py             # Payment
│   └── Rental_System.py       # RentFlow (reports and operations)
└── Readme.md


** Business Rules **

A vehicle can be rented only if its status is available.
Rental cost = number of days × daily rate (a part day counts as a full day).
Each day returned after the due date is late, and is charged a late fee of 150% of the daily rate.
Balance = total cost + late fees − total payments.
A rental is fully paid when its balance is 0 or less.
A vehicle becomes available again as soon as it is returned.



** Conclusion **

RentFlow shows how Object-Oriented Programming can turn the scattered notebooks and spreadsheets at SafariDrive Rentals into one organized, reliable system. Modelling real-world things as objects (vehicles, customers, rentals and payments), the program answers staff questions about availability, who has which car, how long it has been out, what is owed, whether it came back late, and how much money the business has made.

---

