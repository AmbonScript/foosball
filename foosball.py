from competition import Competition
from communicator import Communicator


Communicator.output_message("Welcome to foosball!")
players: int = Communicator.get_number_of_players("How many players will take part in the tournament? ")

# competition: Competition = Competition(players)
# for i in range(2):
#     competition.play_round()

