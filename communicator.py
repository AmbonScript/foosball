import sys
import time

class Communicator:
    __delay=0.03

    @staticmethod
    def output_message(message, delay=0.03):
        for char in message:
            sys.stdout.write(char)  # Write character without a newline
            sys.stdout.flush()      # Ensure the character is printed immediately
            time.sleep(delay)       # Wait for the specified delay
        time.sleep(.5)
        print()  # Print a newline at the end of the message

    def receive_input_int(message, delay=0.03) -> int:
        for char in message:
            sys.stdout.write(char)  # Write character without a newline
            sys.stdout.flush()      # Ensure the character is printed immediately
            time.sleep(delay)       # Wait for the specified delay
        num: int = input()
        print()  # Print a newline at the end of the message
        return num
    
    def get_number_of_players(message) -> int:
        num: int = Communicator.receive_input_int(message)
        return num