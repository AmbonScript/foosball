from __future__ import annotations
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
        Communicator.__type_out("Great, the tournament is about to start")
        Communicator.__count_down()
        Communicator.clear_screen()
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
    
    def display_matches(slot: Slot, match_nr: int) -> None:
        A_Team_Attacker: str = slot.get_slot(match_nr*4 + 1).player.name
        A_Team_Defender: str = slot.get_slot(match_nr*4 + 2).player.name
        B_Team_Attacker: str = slot.get_slot(match_nr*4 + 3).player.name
        B_Team_Defender: str = slot.get_slot(match_nr*4 + 4).player.name
        Communicator.display_table(A_Team_Attacker, A_Team_Defender, B_Team_Attacker, B_Team_Defender, match_nr + 1)
        TeamA_Won: bool = Communicator.__get_winner(match_nr + 1)
        goal_difference: int = Communicator.__get_goal_difference()
    
    def __get_winner(match_nr: int, message: str = None) -> bool:
        if message is None:
            message = f"Which team won MATCH {match_nr} [A/B]?"
        Communicator.__type_out(message)
        winner: str = input()
        if winner == "A" or winner == "B":
            return winner == "A"
        else:
            Communicator.__type_out("Please choose either A or B: ")
            return Communicator.__get_winner(match_nr, "")

    # def get_goal_difference():

    
    def display_table(A1: str, D1: str, A2: str, D2: str, match_nr: int):
        Communicator.clear_screen()
        print()
        print()
        print(f"MATCH {match_nr}")
        print("TEAM A")
        print(f"                       {A1}{Communicator.__make_space_between(A1)}{D1}     ")
        print("                       [#]                              [#]               [#]      [#]     ")
        print("                       [#]                              [#]               [#]      [#]     ")
        print("                        |                                |                 |        |      ")
        print("                        |                                |                 |        |      ")
        print(" -----------------------------------------------------------------------------------------")
        print("|     |        |        |        |           |           |        |        |        |     |")
        print("|     |        |        |       (*)          |          [#]       |        |        |     |")
        print("|     |        |        |        |           |           |        |        |        |     |")
        print("|     |        |       [#]       |           |           |       (*)       |        |     |")
        print("|     |        |        |       (*)          |          [#]       |        |        |     |")
        print("|     |       (*)       |        |       /\u203E\u203E\u203E|\u203E\u203E\u203E\       |        |       [#]       |     |")
        print("|\u203E\u203E|  |        |        |        |      /    |    \      |        |        |        |  |\u203E\u203E|")
        print("|  |  |        |        |        |     |     |     |     |        |        |        |  |  |")
        print("|  | (*)       |       [#]      (*)    |     |     |    [#]      (*)       |       [#] |  |")
        print("|  |  |        |        |        |     |     |     |     |        |        |        |  |  |")
        print("|__|  |        |        |        |      \    |    /      |        |        |        |  |__|")
        print("|     |       (*)       |        |       \___|___/       |        |       [#]       |     |")
        print("|     |        |        |       (*)          |          [#]       |        |        |     |")
        print("|     |        |       [#]       |           |           |       (*)       |        |     |")
        print("|     |        |        |        |           |           |        |        |        |     |")
        print("|     |        |        |       (*)          |          [#]       |        |        |     |")
        print("|     |        |        |        |           |           |        |        |        |     |")
        print(" --------------------------------------------|--------------------------------------------")
        print("      |        |                 |                                |                        ")
        print("      |        |                 |                                |                        ")
        print("     (*)      (*)               (*)                              (*)                       ")
        print("     (*)      (*)               (*)                              (*)                       ")
        print(f"     {D2}{Communicator.__make_space_between(D2, 59)}{A2}                       ")
        print("TEAM B")
        print()
        print()
    
    def __make_space_between(name: str, distance = 50):
        space_between: str = " "
        for i in range((distance - len(name))):
            space_between = space_between + " "
        return space_between

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
        if not num.isdigit():
            Communicator.__type_out("Please input a number: ")
            return Communicator.__receive_int("")
        return num
    
    def __get_number_of_players(message) -> int:
        num: int = Communicator.__receive_int(message)
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
    
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def __count_down(counts: int = 4):
        print()
        for i in range(counts):
            count: int = counts - i - 1
            print(f"{count}", end="\r")
            time.sleep(1)