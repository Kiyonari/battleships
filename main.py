#!/usr/bin/env python3.9
import argparse
import re
from Game import Board


def main():
    parser = argparse.ArgumentParser(description='A game of battleships')
    parser.add_argument('input', help="path to input file")
    args = parser.parse_args()
    with open(args.input) as f:
        board_size = int(f.readline())
        ship_line = f.readline()
        pattern = re.compile(r"""( \( \d+ ,\s* \d+ ,\s* [NSEW] \) )""", re.VERBOSE)
        match = pattern.findall(ship_line)
        instructions = [line[:-1] for line in f.readlines()]

    board = Board(board_size)
    for ship in match:
        board.add_ship(ship)

    for line in instructions:
        board.exec_instruction(line)

    with open("output.txt", "w") as f:
        for ship in board.ships_list:
            state = ""
            if ship.sunk:
                state = " SUNK"
            f.write(f"({ship.position.x}, {ship.position.y}, {ship.orientation}){state}\n")


if __name__ == '__main__':
    main()
