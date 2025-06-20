"""
The vending machine should support multiple products with different prices and quantities.
The machine should accept coins and notes of different denominations.
The machine should dispense the selected product and return change if necessary.
The machine should keep track of the available products and their quantities.
The machine should handle multiple transactions concurrently and ensure data consistency.
The machine should provide an interface for restocking products and collecting money.
The machine should handle exceptional scenarios, such as insufficient funds or out-of-stock products.
"""

"""
The Product class represents a product in the vending machine, with properties such as name and price.
The Coin and Note enums represent the different denominations of coins and notes accepted by the vending machine.
The Inventory class manages the available products and their quantities in the vending machine. It uses a concurrent hash map to ensure thread safety.
The VendingMachineState interface defines the behavior of the vending machine in different states, such as idle, ready, and dispense.
The IdleState, ReadyState, and DispenseState classes implement the VendingMachineState interface and define the specific behaviors for each state.
The VendingMachine class is the main class that represents the vending machine. It follows the Singleton pattern to ensure only one instance of the vending machine exists.
The VendingMachine class maintains the current state, selected product, total payment, and provides methods for state transitions and payment handling.
The VendingMachineDemo class demonstrates the usage of the vending machine by adding products to the inventory, selecting products, inserting coins and notes, dispensing products, and returning change.
"""

# 2:33PM
# 2:35PM

from typing import List, Dict 
from enum import Enum, auto

class DenominationEnum(Enum):
    COIN: auto
    NOTE: auto

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 

class Denomination:
    def __init__(self, amount):
        self.amount = amount 

    def __eq__(self, other):
        return isinstance(other, Denomination) and self.amount == other.amount

    def __hash__(self):
        return self.amount


class Coin( Denomination):
    def __init__(self, amount):
        self.type = DenominationEnum.COIN


class Note( Denomination):
    def __init__(self, amount):
        self.type = DenominationEnum.NOTE


class VendingMachine:
    def __init__(self):
        self.products : Dict[str, int] = {}
        self.money: Dict[Denomination, int] = {}

    def buy(self, product_name, money: dict[Denomination, int]):
        if product_name not in self.products:
            raise Exception("Product in stock!")
        else:
            total_amount = 0
            for denomination, quantity in money.items():
                total_amount += denomination.price * quantity
            if total_amount < self.products[product_name].price:
                raise Exception("Insufficent balance!")
            
            
            product = self.products[product_name]
            product.quantity -= 1
            if product.quantity == 0:
                del self.products[product_name]
        

    def restocking_product (self,product_name, price, quantity):
        if product_name in self.products:
            product = self.products[product_name]
            if product.price != price:
                raise Exception("Product with inconsist price!")
            product.quantity += quantity
        else:
            self.products[product_name] = Product(product_name, price, quantity)

        
    def collect_money (self, money: Dict[Denomination, int]):
        for denomination, quantity in money.item():
            if denomination in self.money:
                self.money[denomination] += quantity 
            else:
                self.money[denomination] =  quantity 

