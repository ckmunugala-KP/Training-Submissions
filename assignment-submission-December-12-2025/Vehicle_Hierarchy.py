# Base class
class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    def vehicle_type(self):
        return "Generic Vehicle"

    def summary(self):
        return f"{self.vehicle_type()} | Brand: {self.brand} | Fuel: {self.fuel_type}"

    def details(self):
        print(self.summary())


# Child class - Car
class Car(Vehicle):
    def __init__(self, brand, fuel_type, doors):
        super().__init__(brand, fuel_type)
        self.doors = doors

    def vehicle_type(self):
        return "Car"

    def details(self):
        super().details()
        print(f"Doors: {self.doors}")


# Child class - Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, brand, fuel_type, has_sidecar):
        super().__init__(brand, fuel_type)
        self.has_sidecar = has_sidecar

    def vehicle_type(self):
        return "Motorcycle"

    def details(self):
        super().details()
        print(f"Sidecar: {'Yes' if self.has_sidecar else 'No'}")


# Child class - Truck
class Truck(Vehicle):
    def __init__(self, brand, fuel_type, load_capacity):
        super().__init__(brand, fuel_type)
        self.load_capacity = load_capacity

    def vehicle_type(self):
        return "Truck"

    def details(self):
        super().details()
        print(f"Load Capacity: {self.load_capacity} tons")


# ----------- User Menu -----------
vehicles = []

while True:
    print("\n=== Vehicle Management System ===")
    print("1. Add Car")
    print("2. Add Motorcycle")
    print("3. Add Truck")
    print("4. View All Vehicles")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        brand = input("Enter brand: ")
        fuel = input("Enter fuel type: ")
        doors = int(input("Enter number of doors: "))
        vehicles.append(Car(brand, fuel, doors))
        print("Car added successfully.")

    elif choice == "2":
        brand = input("Enter brand: ")
        fuel = input("Enter fuel type: ")
        sidecar = input("Has sidecar (yes/no): ").lower() == "yes"
        vehicles.append(Motorcycle(brand, fuel, sidecar))
        print("Motorcycle added successfully.")

    elif choice == "3":
        brand = input("Enter brand: ")
        fuel = input("Enter fuel type: ")
        capacity = float(input("Enter load capacity (tons): "))
        vehicles.append(Truck(brand, fuel, capacity))
        print("Truck added successfully.")

    elif choice == "4":
        if not vehicles:
            print("No vehicles added yet.")
        else:
            print("\n--- Vehicles Entered ---")
            for index, vehicle in enumerate(vehicles, start=1):
                print(f"\nVehicle {index}")
                vehicle.details()
                print("-" * 30)

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
