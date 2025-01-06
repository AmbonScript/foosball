from competition import Competition
from communicator import Communicator
from player import Player

# Choose # of players
Communicator.output_message("Welcome to foosball!\nI will help you organize your tournament. Just follow my instructions")
players: int = Communicator.get_number_of_players("How many players will take part in the tournament? ")
Communicator.output_message(f"Very well. You chose {players} players")

# Choose player names

competition: Competition = Competition(players)
running: bool = Communicator.get_bool("Would you like to start the first round? [Y/N] ")
while running:
    competition.play_round()
    running = Communicator.get_bool("Would you like to start anbother round? [Y/N] ")


