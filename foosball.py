from competition import Competition
from communicator import Communicator
from player import Player

# Choose # of players
number_of_players: int = Communicator.choose_number_of_players()

# Choose player names
# Communicator.choose_player_names(number_of_players)

competition: Competition = Competition(number_of_players)
running: bool = Communicator.get_bool("Would you like to start the first round? [Y/N] ")
while running:
    competition.play_round()
    running = Communicator.get_bool("Would you like to start anbother round? [Y/N] ")


