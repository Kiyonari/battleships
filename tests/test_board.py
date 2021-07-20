from unittest import TestCase

from Game import Ship, Board, Position


class TestBoard(TestCase):
    def setUp(self) -> None:
        self.board = Board(10)
        self.assertFalse(self.board.ships_list)
        self.board.add_ship("1, 1, E")

    def test_add_ship(self):
        self.assertIsInstance(self.board.ships_list[0], Ship)
        self.assertEqual(self.board.ships_list[0].position, Position(x=1, y=1))
        self.board.add_ship("0, 0, W")
        self.assertEqual(len(self.board.ships_list), 2)

    def test_move(self):
        ship = self.board.get_ship(Position(1, 1))
        self.board.move(ship)
        self.assertEqual(ship.position, Position(2, 1))

    def test_move_into_ship(self):
        self.board.add_ship("2, 1, E")
        ship = self.board.get_ship(Position(1, 1))
        self.assertRaises(ValueError, self.board.move, ship)

    def test_move_out_of_grid(self):
        self.board.add_ship("0, 1, W")
        ship = self.board.get_ship(Position(0, 1))
        self.assertRaises(IndexError, self.board.move, ship)

    def test_shoot(self):
        self.board.shoot(Position(1, 1))
        self.assertEqual(self.board.ships_list[0].sunk, True)

    def test_shoot_instruction(self):
        ship = self.board.get_ship(Position(1, 1))
        self.board.exec_instruction("(0, 1)")
        self.assertEqual(ship.sunk, False)
        self.board.exec_instruction("(1, 1)")
        self.assertEqual(ship.sunk, True)

    def test_move_instruction(self):
        ship = self.board.get_ship(Position(1, 1))
        self.board.exec_instruction("(1, 1) MMMRM")
        self.assertEqual(ship.position, Position(4, 0))
