"""
The parking lot should have multiple levels, each level with a certain number of parking spots.
The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
Each parking spot should be able to accommodate a specific type of vehicle.
The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
The system should track the availability of parking spots and provide real-time information to customers.
The system should handle multiple entry and exit points and support concurrent access.
"""

"""
system.park(vehicle)
system.unpark(vehicle)
system.check_availability()
system.
"""

from enum import Enum, auto

class VehicleType(Enum):
    CAR = auto()
    MOTOCYCLE = auto()
    TRUCK = auto()

class Vehicle:
    def __init__(self) -> None:
        self.type

class Car(Vehicle):
    def __init__(self) -> None:
        self.type = VehicleType.CAR

class Motorcycle(Vehicle):
    def __init__(self) -> None:
        self.type = VehicleType.MOTOCYCLE

class Truck(Vehicle):
    def __init__(self, type) -> None:
        self.type = VehicleType.TRUCK

class Parklot():
    def __init__(self, type) -> None:
        self.type = type


class ParkLevel():
    def __init__(self, id, capcity) -> None:
        self.id = id 
        self.capcity = capcity
        self.vehicles: list[Vehicle] = []

class ParkLot():
    def __init__(self) -> None:
        self.levels: list[ParkLevel] = []



