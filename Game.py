# Mateusz Slowik
# Group 50
import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
from GameObjects import GameObjects
from GameObjects import Puzzle
from Player import Player

# Controll the overall flow of the game
class Game:
    def __init__(self):
        self.game_objects = GameObjects()
        self.puzzle = Puzzle()
        self.player = Player(name="Player")
        self.game_over = False
        self.won_game = False

    # Controll hardcoded tank scene
    def tank(self):
        print(Style.BRIGHT + "You opened a metal tank.")
        print("It seems to be empty, except small manual")
        print("Xenocide Bomb: This weapon releases a burst of energy that instantly neutralizes the molecular bonds ")
        print("of any alien organisms within a certain radius. The intense energy field created by the bomb")
        print("is so unstable that it completely destroys the weapon and renders it useless after a single use")
        print()

    # Controll hardcoded note scene
    def notebook(self):
        print(Style.BRIGHT + "You opened a notebook and read: ")
        print(
            Style.BRIGHT + "DAY 51: " + Style.RESET_ALL + "Along the way, I encountered an AI system that has taken control of the ship and is trying to stop me from escaping.")
        print("I'm just a space worker, I can't use these computers. If anyone else is stuck here too, you must")
        print(
            "outsmart the AI system by hacking " + Fore.BLUE + Style.BRIGHT + "3 terminals" + Style.RESET_ALL + " and overcoming challenges to make your way to the ship's airlock center.")
        print()
        print(
            "Unfortunately I lost all my " + Style.BRIGHT + Fore.GREEN + "Xenocide bomb" + Style.RESET_ALL + "-s when I was escaping from a group of aliens, ")
        print(
            "but I'm sure you can find them somewhere on the ship. This is the only way to defeat the alien in combat.")
        print()
        print(
            "Moreover, aliens are not the only threat. They're doing terrible experiments on other life forms here. Somewhere on this ship, there's a" + Fore.RED + Style.BRIGHT + " giant mutant" + Style.RESET_ALL + "that ")
        print(
            "doesn't seem to be impressed by my bombs. It also seems much more dangerous than aliens. Stay away from him.")
        print("Good Luck, for me is too late")
        print()
        print(
            "PS: I left my work " + Style.BRIGHT + "navigator" + Style.RESET_ALL + ". It will help you navigate yourself in this dark ship")
        print()

    # Controll hardcoded intro scene
    def intro(self):
        print("You are a space explorer who has been sent on a mission to explore a distant planet.")
        print("As you approach the planet, you notice a strange spaceship in the distance.")
        print(
            "You decide to investigate, but as you get closer, your ship is suddenly pulled into the other ship's gravitational field.")
        print()
        print("You awaken to find yourself trapped on the alien spaceship with no way to escape.")
        print("The ship is filled with traps, puzzles, and enemies that are out to get you.")
        print("Your objective is to find a way off the ship by exploring and solving the challenges that lie ahead.")
        print()
        print(
            "As you explore the ship, you discover that the alien race that built the ship has been experimenting on different life forms from various planets")
        print(
            "Some of these experiments have gone horribly wrong, and you'll need to fight off these mutated creatures to survive.")
        print()
        print("Can you find a way off the ship and return home safely? ")
        print()
        print(Fore.YELLOW + Style.BRIGHT + "The fate of your mission and your life rests in your hands.")

    # Control the game
    def play(self):
        isStarted = False
        computerCounter = 3
        print(Style.BRIGHT + "Welcome to the game!")
        print()
        print()
        self.intro()
        print()
        start = input("Enter 'start' to start the game ")
        try:
            if start == "start":
                print("====================================")
                isStarted = True
                self.game_objects.look_around()
                print(
                    "A body of a dead " + Fore.RED + Style.BRIGHT + "astronaut " + Fore.RESET + Style.RESET_ALL + "with a" + Fore.BLUE + Style.BRIGHT + " note")
                print("Metal tank with a skull icon and the words 'Explosive'")
                self.player.print_status()
                tank = False
                book = False
                while not tank or not book:
                    notebook = input("Enter 'read a note' to examine a note or 'go to tank' to search the tank: ")
                    if notebook == "read a note":
                        self.notebook()
                        book = True
                    if notebook == "go to tank":
                        self.tank()
                        tank = True
        except:
            print("An exception occurred")

        while isStarted:
            print("====================================")
            # display game information
            self.game_objects.look_around()
            self.player.print_status()
            # ask the player for their next move
            move = input("Enter your move (north/south/east/west): ")
            # move the player and check for game over conditions
            if not self.game_objects.move_player(move):
                print("Invalid move. Try again.")
            elif self.game_objects.check_for_enemy():
                enemy = self.game_objects.check_for_enemy()
                print(f"You have encountered an {enemy.name}!")
                fight = input("Do you want to fight? (y/n)")
                if fight.lower() == "y":
                    if self.player.fight():
                        self.game_objects.remove_enemy(enemy)
                        print("Enemy defeated!")
                    else:
                        print("You were defeated. Game over.")
                        return
                else:
                    self.player.player_runAway()

            elif self.game_objects.check_for_mutant():
                mutant = self.game_objects.check_for_mutant()
                print(f"You have encountered an " + Style.BRIGHT + Back.RED + mutant.name + " !")
                fight = input("Do you want to fight? (y/n)")
                if fight.lower() == "y":
                    print("You were defeated. Game over.")
                    return

                else:
                    print("You were defeated. Game over.")
                    return
            elif self.game_objects.check_for_item():
                item = self.game_objects.check_for_item()
                self.player.add_item(item)
                self.game_objects.remove_item(item)
                print(f"You have found a {item.name}!")
            elif self.game_objects.check_for_puzzle():
                puzzle = self.game_objects.check_for_puzzle()
                print(f"You have found a {puzzle}!")
                answer = input("Enter the answer to the puzzle: ")
                correctAnswer = Puzzle.get_answer(puzzle)
                if int(correctAnswer) == int(answer):
                    self.game_objects.remove_puzzle(puzzle)
                    print("Puzzle solved!")
                    computerCounter -= 1
                    print(str(computerCounter) + " Coputers left")
                else:
                    print("Incorrect answer. Try again.")
            elif self.game_objects.check_exit_reached():
                if computerCounter == 0:
                    print("Congratulations, you have reached the exit!")
                    return
                else:
                    print("You found an exit")
                    print("You need to hack all 3 computers to open the airlock")
            print("====================================")
