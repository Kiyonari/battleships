#!/usr/bin/env python3.9
from unittest import TestCase
from Game import Ship, Position


class TestShip(TestCase):

    def setUp(self) -> None:
        self.ship = Ship(Position(2, 5), 'E')
        print(f"Created a ship at position {self.ship.get_position()}, facing {self.ship.orientation}")

    def test_get_position(self):
        self.assertEqual(self.ship.get_position(), Position(2, 5))

    def test_rotate_right(self):
        self.ship.rotate_right()
        self.assertEqual(self.ship.orientation, 'S')

    def test_rotate_left(self):
        self.ship.rotate_left()
        self.assertEqual(self.ship.orientation, 'N')
