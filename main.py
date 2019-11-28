import sys
import brain_commands as random_move

commands_brain = ["START", "TURN", "BEGIN", "BOARD", "INFO", "END", "ABOUT"]
functions_call = ["start", "turn", "begin", "board", "info", "end", "about"]


def start(a, b):
    # Give the size of the board
    print("OK")


def turn(a, b):
    # Gives the coordinate played by the opponent
    random_move.play_whatev()


def begin(a, b):
    # Means we begin
    random_move.play_whatev()


def board(a, b):
    print("Ye idk")


def info(a, b):
    print("we win w/e")


def end(a, b):
    print("return")


def about(a, b):
    print('name="LARD\'HON", version="0.1", author="Maxime Lardier & Claude Prod\'Hon", country="FR"')


def main():
    while True:
        line = sys.stdin.readline()
        command = line.strip().split(" ")
        if command[0] in commands_brain:
            param1 = command[1] if len(command) > 1 else 0
            param2 = command[2] if len(command) > 2 else 0
            globals()[functions_call[commands_brain.index(command[0])]](param1, param2)
        else:
            print("Unknown command")


main()
