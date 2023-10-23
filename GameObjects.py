# Mateusz Slowik
# Group 50
import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


class GameObjects:
    def __init__(self):
        self.player_location = (0, 0)
        self.exit_location = (5, 5)
        self.enemies = []
        self.items = []
        self.mutants = []
        self.puzzles = []
        self.generate_game_objects()

    def generate_game_objects(self):
        # generate enemies, items, and puzzles randomly
        for i in range(3):
            enemy = Enemy()
            self.enemies.append(enemy)

        mutant = Mutant()
        self.mutants.append(mutant)

        for i in range(3):
            item = Item()
            self.items.append(item)
        for i in range(3):
            puzzle = Puzzle()
            self.puzzles.append(puzzle)

    def look_around(self):
        # print information about the player's location
        print(f"You are at location {self.player_location}.")
        print("You see:")
        # print information about nearby objects
        for enemy in self.enemies:
            if self.check_distance(self.player_location, enemy.location) < 2:
                print(f"An " + Fore.RED + Style.BRIGHT + enemy.name + '\033[39m' + " nearby.")
        for item in self.items:
            if self.check_distance(self.player_location, item.location) < 2:
                print(f"A " + Fore.GREEN + Style.BRIGHT + item.name + '\033[39m' + " nearby.")
        for puzzle in self.puzzles:
            if self.check_distance(self.player_location, puzzle.location) < 2:
                print(f"A " + Fore.BLUE + Style.BRIGHT + puzzle.name + '\033[39m' + " nearby.")
        for mutant in self.mutants:
            if self.check_distance(self.player_location, mutant.location) < 2:
                print(f"An " + Fore.RED + Style.BRIGHT + mutant.name + '\033[39m' + " nearby.")

    # Move player in chosen direction
    def move_player(self, direction):
        # move the player in the specified direction
        x, y = self.player_location
        if direction == "north":
            y += 1
        elif direction == "south":
            y -= 1
        elif direction == "east":
            x += 1
        elif direction == "west":
            x -= 1
        else:
            return False
        # check if the new location is valid
        if self.check_location_valid((x, y)):
            self.player_location = (x, y)

            # Print map headers
            print(Style.BRIGHT + "======== N A V I G A T O R ======== ")
            print("   ", end="")
            for i in (range(6)):
                print(i, end="  ")
            print()

            # Print rows with row labels and player location
            for i in reversed(range(6)):
                print(str(i).rjust(2), end=" ")
                for j in range(6):
                    if self.player_location == (j, i):
                        print(Fore.GREEN + "x  ", end="")
                    else:
                        print("-  ", end="")
                print()
            return True
        else:
            return False

    def check_location_valid(self, location):
        # check if a location is valid (not outside the game boundaries)
        x, y = location
        if x < 0 or x > 5 or y < 0 or y > 5:
            return False
        else:
            return True

    def check_distance(self, location1, location2):
        # check the distance between two locations
        x1, y1 = location1
        x2, y2 = location2
        distance = abs(x1 - x2) + abs(y1 - y2)
        return distance

    def check_for_enemy(self):
        # check if the player has encountered an enemy
        for enemy in self.enemies:
            if enemy.location == self.player_location:
                return enemy
        return None

    def check_for_mutant(self):
        # check if the player has encountered a mutant
        for mutant in self.mutants:
            if mutant.location == self.player_location:
                return mutant
        return None

    def check_for_item(self):
        # check if the player has found an item
        for item in self.items:
            if item.location == self.player_location:
                return item
        return None

    def check_for_puzzle(self):
        # check if the player has found a puzzle
        for puzzle in self.puzzles:
            if puzzle.location == self.player_location:
                return puzzle
        return None

    def remove_enemy(self, enemy):
        # remove a defeated enemy from the game objects
        self.enemies.remove(enemy)

    def remove_puzzle(self, puzzle):
        # remove a solved puzzle from the game objects
        self.puzzles.remove(puzzle)

    def remove_item(self, item):
        # remove a defeated enemy from the game objects
        self.items.remove(item)

    def check_exit_reached(self):
        if self.player_location == self.exit_location:
            return True
        else:
            return False


def generate_location():
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    return x, y


class Enemy:
    def __init__(self):
        self.location = generate_location()
        self.health = 100
        self.name = "Alien"

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"The enemy at location {self.location} has been defeated!")


def generate_random_location():
    # generate a random location within the game boundaries
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    return (x, y)


class Item:
    def __init__(self):
        self.name = "Xenocide Bomb"
        self.description = "This weapon releases a burst of energy that instantly neutralizes the molecular bonds of any alien organisms within a certain radius. The intense energy field created by the bomb is so unstable that it completely destroys the weapon and renders it useless after a single use."
        self.location = generate_random_location()
        self.quantity = 1

    def __str__(self):
        return self.name


class Puzzle:
    name = "Terminal"

    def __init__(self):
        self.location = (random.randint(0, 5), random.randint(0, 5))
        self.operation = random.choice(['+', '-', '*'])
        self.operand1 = random.randint(1, 10)
        self.operand2 = random.randint(1, 10)
        self.answer = self.get_answer()
        self.name = "Terminal"

    def __str__(self):
        return f"{self.operand1} {self.operation} {self.operand2} = ?"

    def get_answer(self):
        if self.operation == '+':
            result = self.operand1 + self.operand2
            return int(result)
        elif self.operation == '-':
            result = self.operand1 - self.operand2
            return int(result)
        elif self.operation == '*':
            result = self.operand1 * self.operand2
            return int(result)
        else:
            return None

class Mutant:
    def __init__(self):
        self.location = (random.randint(0, 4), random.randint(1, 4))
        self.health = 100
        self.name = "Mutant"

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"The enemy at location {self.location} has been defeated!")
