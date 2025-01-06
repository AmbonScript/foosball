import sys
import time

class Communicator:

    @staticmethod
    def output_message(message):
        Communicator.type_out(message)
        print()  # Print a newline at the end of the message
        print()

    def receive_int(message) -> int:
        Communicator.type_out(message)
        num: int = input()
        print()  # Print a newline at the end of the message
        return num
    
    def get_number_of_players(message) -> int:
        num: int = Communicator.receive_int(message)
        if not num.isdigit():
            Communicator.type_out("Please input a number: ")
            return Communicator.get_number_of_players("")
        num = int(num)
        if (num < 8) or (num > 60):
            Communicator.type_out("Please choose a number between 8 and 60: ")
            return Communicator.get_number_of_players("")
        return num
    
    def get_bool(message) -> bool:
        Communicator.type_out(message)
        choice: str = input()
        if choice == "y" or choice == "Y":
            return True
        if choice == "n" or choice == "N":
            return False
    
    def type_out(message, delay=0.03):
        for char in message:
            sys.stdout.write(char)  # Write character without a newline
            sys.stdout.flush()      # Ensure the character is printed immediately
            if char == "." or char == "!" or char == "?":
                time.sleep(.5)
            time.sleep(delay)       # Wait for the specified delay
        time.sleep(.5)