# Mateusz Slowik
# Group 50
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#Controll all player statistics
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
    #Add founded items
    def add_item(self, item):
        self.inventory.append(item)

    #Remove items from inventory
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    #Controll health system
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("Game over!")

    #Prints status of the player
    def print_status(self):
        if self.health > 50:
            print("Health:" + Fore.LIGHTGREEN_EX + str(self.health))
        else:
            print("Health:" + Fore.RED + str(self.health))
        print("Inventory:")
        if self.inventory:
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("  (empty)")

    #Controll run-away system
    def player_runAway(self):

        self.health -= 50
        if self.health == 0:
            print("You were defeated. Game over.")
            quit()
        else:
            print("You barely run away.")

    # Controll fight system
    def fight(self):
        if self.inventory:
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("  (empty)")
        print("--------------------------")
        if item in self.inventory:
            self.remove_item(item)
            return True
        return False

