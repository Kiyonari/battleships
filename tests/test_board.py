from unittest import TestCase

from Game import Ship, Board, Position


class TestBoard(TestCase):
    def setUp(self) -> None:
        self.board = Board(10)
        self.assertFalse(self.board.ships_list)

    def test_add_ship(self):
        self.board.add_ship("1, 1, E")
        self.assertIsInstance(self.board.ships_list[0], Ship)
        self.assertEqual(self.board.ships_list[0].position, Position(x=1, y=1))
        self.board.add_ship("0, 0, W")
        self.assertEqual(len(self.board.ships_list), 2)

    def test_move(self):
        self.board.add_ship("1, 1, E")
        ship = self.board.get_ship(Position(1, 1))
        self.board.move(ship)
        self.assertEqual(ship.position, Position(2, 1))

    def test_move_into_ship(self):
        self.board.add_ship("1, 1, E")
        self.board.add_ship("2, 1, E")
        ship = self.board.get_ship(Position(1, 1))
        self.assertRaises(ValueError, self.board.move, ship)

    def test_move_out_of_grid(self):
        self.board.add_ship("0, 1, W")
        ship = self.board.get_ship(Position(0, 1))
        self.assertRaises(IndexError, self.board.move, ship)

    def test_shoot(self):
        self.board.add_ship("1, 1, E")
        self.board.shoot(Position(1, 1))
        self.assertEqual(self.board.ships_list[0].sunk, True)
