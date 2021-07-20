from copy import copy
from dataclasses import dataclass
from itertools import cycle, dropwhile
import re
from typing import Optional


@dataclass
class Position:
    x: int
    y: int

    def move(self, orientation) -> "Position":
        new_pos = Position(self.x, self.y)
        if orientation == 'N':
            new_pos.y += 1
        if orientation == 'E':
            new_pos.x += 1
        if orientation == 'S':
            new_pos.y -= 1
        if orientation == 'W':
            new_pos.x -= 1
        return new_pos


orientation_grid = ["N", "E", "S", "W"]


class Ship:

    position: Position
    orientation: str
    sunk: bool = False

    def __init__(self, position: Position, orientation: str):
        self.position = position
        self.orientation = orientation

    def get_position(self) -> Position:
        return self.position

    def rotate_right(self) -> None:
        cycled = cycle(orientation_grid)
        skipped = dropwhile(lambda x: x != self.orientation, cycled)
        next(skipped)
        self.orientation = next(skipped)

    def rotate_left(self) -> None:
        cycled = cycle(reversed(orientation_grid))
        skipped = dropwhile(lambda x: x != self.orientation, cycled)
        next(skipped)
        self.orientation = next(skipped)


class Board:
    size: int
    ships_list: list[Ship]

    def __init__(self, size):
        if size < 0:
            raise ValueError("Board size must be positive")
        self.size = size
        self.ships_list = []

    def get_ship(self, position: Position) -> Optional[Ship]:
        for ship in self.ships_list:
            if position == ship.position:
                return ship
        return None

    def check_coordinates(self, position: Position) -> bool:
        if position.x > self.size or position.y > self.size:
            raise IndexError(f"Ship isn't on the grid. Must be lower than {self.size}")
        if position.x < 0 or position.y < 0:
            raise IndexError("X or Y value must be positive")

        for ship in self.ships_list:
            if position == ship.position:
                raise ValueError(f"A ship is already present at {position.x, position.y}")

        return True

    def add_ship(self, string) -> None:
        sanitized = re.sub(r'[( )]', '', string)
        x, y, orientation = sanitized.split(',')
        position = Position(int(x), int(y))
        if self.check_coordinates(position):
            new_ship = Ship(position, orientation)
            self.ships_list.append(new_ship)

    def move(self, ship: Ship) -> None:
        new_pos = ship.position.move(ship.orientation)
        self.check_coordinates(new_pos)
        ship.position = new_pos

    def shoot(self, target: Position):
        ship = self.get_ship(target)
        if ship:
            ship.sunk = True

    def exec_instruction(self, instruction: str) -> None:
        pass
