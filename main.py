import re
from Game import Board


def main():
    with open("input.txt") as f:
        board_size = int(f.readline())
        ship_line = f.readline()
        pattern = re.compile(r"""
        (\(
        \d+     # Position x
        ,\s*    # Any number of spaces
        \d+     # Position y
        ,\s*    # Any number of spaces
        [NSEW]  # Cardinal direction
        \))
        """, re.VERBOSE)
        match = pattern.findall(ship_line)
        instructions = [line[:-1] for line in f.readlines()]

    board = Board(board_size)
    for ship in match:
        board.add_ship(ship)
    print(f"Board of size {board.size} created.")
    print(f"{len(board.ships_list)} ships placed.")

    for line in instructions:
        board.exec_instruction(line)

    sunken_ships = [ship for ship in board.ships_list if ship.sunk]
    print(sunken_ships)


if __name__ == '__main__':
    main()
