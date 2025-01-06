from competition import Competition
from communicator import Communicator


Communicator.output_message("Welcome to foosball!\nI will help you organize your tournament. Just follow my instructions")
players: int = Communicator.get_number_of_players("How many players will take part in the tournament? ")
Communicator.output_message(f"Very well. You chose {players} players")

# competition: Competition = Competition(players)
# for i in range(2):
#     competition.play_round()

