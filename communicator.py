from __future__ import annotations
import sys
import time
import os
from player import Player
from slot import Slot
from team import Team
from result import Result
from position import Position
from typing import List

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
        Communicator.__type_out("Great, the tournament is about to start in:")
        Communicator.__count_down()
        Communicator.clear_screen()
        return True
    
    def start_round(number: int) -> None:
        Communicator.clear_screen()
        Communicator.__type_out(f"Starting Round #{number}\n")

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
    
    def choose_manual_results() -> bool:
        return Communicator.get_bool("Would you like to input the match results yourself? (If not, I will generate them) [Y/N] ")
    
    def display_matches_and_get_results(slot: Slot, match_nr: int) -> None:
        A_Team_Attacker: str = slot.get_slot(match_nr*4 + 1).player.name
        A_Team_Defender: str = slot.get_slot(match_nr*4 + 2).player.name
        B_Team_Attacker: str = slot.get_slot(match_nr*4 + 3).player.name
        B_Team_Defender: str = slot.get_slot(match_nr*4 + 4).player.name
        Communicator.display_table(A_Team_Attacker, A_Team_Defender, B_Team_Attacker, B_Team_Defender, match_nr + 1)
        winning_team: Team = Communicator.__get_winner(match_nr + 1)
        goal_difference: int = Communicator.__get_goal_difference()
        Result.add_match_result(match_nr, winning_team, goal_difference)

    def show_rankings() -> None:
        Communicator.clear_screen()
        print("ATTACKER RANKINGS                            ||      DEFENDER RANKING    ")
        print("-----------------------------------------------------------------------------------------------")
        print("NAME              | WINS | GOAL DIFFERENCE   ||      NAME              | WINS | GOAL DIFFERENCE   ")
        print("---------------------------------------------||------------------------------------------------")
        for i in range(Player.get_number_of_players()):
            rank = i + 1
            attacker: Player = Player.get_player_with_rank(rank, Position.ATTACKER)
            defender: Player = Player.get_player_with_rank(rank, Position.DEFENDER)
            Communicator.__type_out(f"{attacker.name}{Communicator.__make_space_between(attacker.name, 15)}  |  {attacker._Player__attacker_wins}   |    {attacker._Player__attacker_goal_difference}{Communicator.__make_space_between(str(attacker._Player__attacker_goal_difference), 14)}||      {defender.name}{Communicator.__make_space_between(defender.name, 15)}  | {defender._Player__defender_wins}   |    {defender._Player__defender_goal_difference}\n", 0.005)
        # print("Press any key to continue")
        # input()
    
    def end_competition() -> None:
        print("\n")
        Communicator.__type_out("The foosball competition has ended\n")
        attacker: Player = Player.get_player_with_rank(1, Position.ATTACKER)
        defender: Player = Player.get_player_with_rank(1, Position.DEFENDER)
        Communicator.__type_out(f"{attacker.name} was the best attacker\n")
        Communicator.__type_out(f"{defender.name} was the best defender\n")

    def __get_winner(match_nr: int, message: str = None) -> Team:
        if message is None:
            message = f"Which team won MATCH {match_nr} [A/B]? "
        Communicator.__type_out(message)
        winner: str = input()
        if winner == "A":
            return Team.A
        if winner == "B":
            return Team.B
        else:
            Communicator.__type_out("Please choose either A or B: ")
            return Communicator.__get_winner(match_nr, "")

    def __get_goal_difference(message: str = "How many goals did the losing team score? ") -> int:
        goals: int = int(Communicator.__receive_int(message))
        if (goals < 0) or (goals > 7):
            goals = Communicator.__get_goal_difference("Please input a number between 0 and 7 ")
        return (8 - goals)
    
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
        
    def __type_out(message, delay=0.03, sleep_time=.5):
        for char in message:
            sys.stdout.write(char)  # Write character without a newline
            sys.stdout.flush()      # Ensure the character is printed immediately
            if char == "." or char == "!" or char == "?":
                time.sleep(sleep_time)
            time.sleep(delay)       # Wait for the specified delay
        time.sleep(sleep_time)
    
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def __count_down(counts: int = 4):
        print()
        for i in range(counts):
            count: int = counts - i - 1
            print(f"{count}", end="\r")
            time.sleep(1)
    
    def opening_animation():
        # Communicator.__are_you_ready("LAAAAAAAAAAAAAAAAAADIIIIEEEEEESSSSS. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAND. GENTLEMEN!", True)
        # Communicator.__are_you_ready("ARE")
        # Communicator.__are_you_ready("YOU")
        # Communicator.__are_you_ready("READY?")
        # Communicator.__roll_table()
        # Communicator.__lets_play_foosball()
        Communicator.__wiggle_table()
        pass

    def __are_you_ready(word: str, do_typing: bool=False):
        Communicator.clear_screen()
        for i in range(10):
            print()
        if do_typing:
            Communicator.__type_out(f"                                                     {word}")
        else:
            print(f"                                                     {word}")
            time.sleep(1)
        Communicator.clear_screen()
    
    def __roll_table():
        # Communicator.clear_screen()
        for i in range(len(Communicator.table)):
            Communicator.__show_table((len(Communicator.table)-i))
            time.sleep(.1)
        time.sleep(2)
    
    def __lets_play_foosball():
        Communicator.clear_screen()
        Communicator.__shout("LET'S")
        # Communicator.__flash_table()
        Communicator.__shout("PLAY")
        # Communicator.__flash_table()
        Communicator.__shout("FOOSBALL!!!!")

    
    def __shout(word: str):
        Communicator.clear_screen()
        for i in range(14):
            print()
        print(f"                                                    {word}")
        time.sleep(1)
        

    def __flash_table():
        Communicator.clear_screen()
        Communicator.__show_table(0)
        time.sleep(1)

    def __show_table(start_line: int, table = None):
        if table is None:
            table = Communicator.table
        tafel = ""
        for i in range(start_line, len(table)):
            tafel = tafel + table[i] + "\n"
        # Communicator.clear_screen()
        print(tafel, end="\r")
        print("\033[1;1H", end="", flush=True)
    
    def __wiggle_table():
        Communicator.clear_screen()
        wiggle: bool = False
        Communicator.__show_table(0)
        for i in range(10):
            if wiggle:
                Communicator.__show_table(0, Communicator.wiggle_table)
            else:
                Communicator.__show_table(0)
            time.sleep(1)
            wiggle = not wiggle
    
    table: List[str] = [
        "                                                                                                         ",
        "                                                                                                         ",
        "                                                                                                         ",
        "                              [#]                              [#]               [#]      [#]     ",
        "                              [#]                              [#]               [#]      [#]     ",
        "                               |                                |                 |        |      ",
        "                               |                                |                 |        |      ",
        "        -----------------------------------------------------------------------------------------",
        "       |     |        |        |        |           |           |        |        |        |     |",
        "       |     |        |        |       (*)          |          [#]       |        |        |     |",
        "       |     |        |        |        |           |           |        |        |        |     |",
        "       |     |        |       [#]       |           |           |       (*)       |        |     |",
        "       |     |        |        |       (*)          |          [#]       |        |        |     |",
        "       |     |       (*)       |        |       /\u203E\u203E\u203E|\u203E\u203E\u203E\       |        |       [#]       |     |",
        "       |\u203E\u203E|  |        |        |        |      /    |    \      |        |        |        |  |\u203E\u203E|",
        "       |  |  |        |        |        |     |     |     |     |        |        |        |  |  |",
        "       |  | (*)       |       [#]      (*)    |     |     |    [#]      (*)       |       [#] |  |",
        "       |  |  |        |        |        |     |     |     |     |        |        |        |  |  |",
        "       |__|  |        |        |        |      \    |    /      |        |        |        |  |__|",
        "       |     |       (*)       |        |       \___|___/       |        |       [#]       |     |",
        "       |     |        |        |       (*)          |          [#]       |        |        |     |",
        "       |     |        |       [#]       |           |           |       (*)       |        |     |",
        "       |     |        |        |        |           |           |        |        |        |     |",
        "       |     |        |        |       (*)          |          [#]       |        |        |     |",
        "       |     |        |        |        |           |           |        |        |        |     |",
        "        --------------------------------------------|--------------------------------------------",
        "             |        |                 |                                |                        ",
        "             |        |                 |                                |                        ",
        "            (*)      (*)               (*)                              (*)                       ",
        "            (*)      (*)               (*)                              (*)                       ",
        "                                                                                                         "
        ]
    
    wiggle_table: List[str] = [
        "                                                                                                         ",
        "                                                                                                         ",
        "                              [#]                              [#]                                ",
        "                              [#]                              [#]               [#]      [#]     ",
        "                               |                                |                [#]      [#]     ",
        "                               |                                |                 |        |      ",
        "                               |                                |                 |        |      ",
        "        -----------------------------------------------------------------------------------------",
        "       |     |        |        |        |           |          [#]       |        |        |     |",
        "       |     |        |        |        |           |           |        |        |        |     |",
        "       |     |        |       [#]      (*)          |           |        |        |        |     |",
        "       |     |        |        |        |           |          [#]      (*)       |        |     |",
        "       |     |        |        |        |           |           |        |        |        |     |",
        "       |     |        |        |       (*)      /\u203E\u203E\u203E|\u203E\u203E\u203E\       |        |       [#]       |     |",
        "       |\u203E\u203E|  |       (*)       |        |      /    |    \      |        |        |        |  |\u203E\u203E|",
        "       |  | (*)       |       [#]       |     |     |     |    [#]       |        |        |  |  |",
        "       |  |  |        |        |        |     |     |     |     |       (*)       |       [#] |  |",
        "       |  |  |        |        |       (*)    |     |     |     |        |        |        |  |  |",
        "       |__|  |        |        |        |      \    |    /      |        |        |        |  |__|",
        "       |     |        |        |        |       \___|___/      [#]       |       [#]       |     |",
        "       |     |       (*)      [#]       |           |           |        |        |        |     |",
        "       |     |        |        |       (*)          |           |       (*)       |        |     |",
        "       |     |        |        |        |           |          [#]       |        |        |     |",
        "       |     |        |        |        |           |           |        |        |        |     |",
        "       |     |        |        |       (*)          |           |        |        |        |     |",
        "        --------------------------------------------|--------------------------------------------",
        "             |        |                 |                                |                        ",
        "            (*)       |                 |                                |                        ",
        "            (*)       |                 |                               (*)                       ",
        "                     (*)               (*)                              (*)                       ",
        "                     (*)               (*)                                                           ",
        "                                                                                                         ",
        "                                                                                                         "
        ]