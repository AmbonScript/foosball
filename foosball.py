from competition import Competition
from communicator import Communicator
from player import Player

# Begin with a clear screen
Communicator.clear_screen()

# Opening animation
Communicator.opening_animation()

# Choose # of players
number_of_players: int = Communicator.choose_number_of_players()

# Choose player names
Communicator.choose_player_names(number_of_players)

# Start the competition
number_of_players: int = 8
competition: Competition = Competition(number_of_players)
running: bool = Communicator.start_first_round()

# Run the competition
while running:
    competition.play_round()
    running = Communicator.get_bool("Would you like to start another round? [Y/N] ")

# End the competition
Communicator.end_competition()
