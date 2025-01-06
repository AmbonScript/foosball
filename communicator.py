import sys
import time
import os
from player import Player
from slot import Slot

class Communicator:

    def choose_number_of_players() -> int:
        Communicator.__output_message("Welcome to foosball!\nI will help you run your tournament. Just answer a few simple questions")
        players: int = Communicator.__get_number_of_players("How many players will take part in the tournament? ")
        Communicator.__output_message(f"Very well. You chose {players} players")
        return players
    
    def choose_player_names(number_of_players: int) -> None:
        if Communicator.get_bool("Would you like to input the player names yourself? (If not, I will generate them for you) [Y/N] "):
            for i in range(number_of_players):
                Communicator.__receive_player_name(f"Please provide the name of player {i + 1}: ", i)
    
    def start_first_round() -> bool:
        Communicator.__type_out("Great, looks like the tournament is almost ready to start")
        Communicator.__count_down()
        Communicator.__clear_screen()
        return Communicator.get_bool("Would you like to start the first round? [Y/N] ")

    def get_bool(message) -> bool:
        Communicator.__type_out(message)
        choice: str = input()
        if choice == "y" or choice == "Y":
            return True
        if choice == "n" or choice == "N":
            return False
        else:
            Communicator.__type_out("Please choose either Y or N: ")
            return Communicator.get_bool("")
    
    def display_matches(slot: Slot) -> None:
        for i in range(int(Player.get_number_of_players_in_round() / 2)):
            print(i)
    
    def __receive_player_name(message, i: int) -> None:
        Communicator.__type_out(message)
        name: str = input()
        Player.set_name(name, i)

    def __output_message(message):
        Communicator.__type_out(message)
        print()  # Print a newline at the end of the message
        print()

    def __receive_int(message) -> int:
        Communicator.__type_out(message)
        num: int = input()
        # print()  # Print a newline at the end of the message
        return num
    
    def __get_number_of_players(message) -> int:
        num: int = Communicator.__receive_int(message)
        if not num.isdigit():
            Communicator.__type_out("Please input a number: ")
            return Communicator.__get_number_of_players("")
        num = int(num)
        if (num < 8) or (num > len(Player.get_names())):
            Communicator.__type_out(f"Please choose a number between 8 and {len(Player.get_names())}: ")
            return Communicator.__get_number_of_players("")
        return num
        
    def __type_out(message, delay=0.03):
        for char in message:
            sys.stdout.write(char)  # Write character without a newline
            sys.stdout.flush()      # Ensure the character is printed immediately
            if char == "." or char == "!" or char == "?":
                time.sleep(.5)
            time.sleep(delay)       # Wait for the specified delay
        time.sleep(.5)
    
    def __clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def __count_down(counts: int = 4):
        print()
        for i in range(counts):
            count: int = counts - i - 1
            print(f"{count}", end="\r")
            time.sleep(1)