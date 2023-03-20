import unittest

from ..Chess.game import Chess
from ..Chess.controller import Controller


class Testing(unittest.TestCase):

    def test_bishop_move(self):
        chess = Chess()
        chess.move_piece(6, 3, 4, 3)
        chess.move_piece(1, 4, 3, 4)
        chess.move_piece(7, 2, 4, 5)
        chess.move_piece(0, 5, 3, 2)
        chess.move_piece(4, 3, 3, 3)
        chess.move_piece(3, 4, 4, 4)

        bishop_moves = chess.get_bishop_moves(4, 5)
        valid_moves = [(3, 6), (2, 7), (3, 4), (2, 3), (1, 2),
                       (5, 6), (5, 4), (6, 3), (7, 2)]
        self.assertEqual(bishop_moves, valid_moves)

        bishop_moves = chess.get_bishop_moves(3, 2)
        valid_moves = [(2, 3), (1, 4), (0, 5), (2, 1), (4, 3),
                       (5, 4), (6, 5), (4, 1), (5, 0)]
        self.assertEqual(bishop_moves, valid_moves)

    def test_rook_move(self):
        chess = Chess()
        chess.move_piece(6, 0, 4, 0)
        chess.move_piece(1, 7, 3, 7)
        chess.move_piece(7, 0, 5, 0)
        chess.move_piece(0, 7, 2, 7)
        chess.move_piece(5, 0, 5, 3)
        chess.move_piece(2, 7, 2, 4)
        chess.move_piece(5, 3, 4, 3)
        chess.move_piece(2, 4, 3, 4)

        valid_moves = [(3, 3), (2, 3), (1, 3), (5, 3), (4, 2),
                       (4, 1), (4, 4), (4, 5), (4, 6), (4, 7)]
        rook_moves = chess.get_rook_moves(4, 3)
        self.assertEqual(rook_moves, valid_moves)

        chess.move_piece(4, 0, 3, 0)

        valid_moves = [(2, 4), (4, 4), (5, 4), (6, 4), (3, 3),
                       (3, 2), (3, 1), (3, 0), (3, 5), (3, 6)]
        rook_moves = chess.get_rook_moves(3, 4)
        self.assertEqual(rook_moves, valid_moves)

    def test_queen_move(self):
        chess = Chess()
        chess.move_piece(6, 4, 4, 4)
        chess.move_piece(1, 2, 3, 2)
        chess.move_piece(7, 3, 3, 7)
        chess.move_piece(0, 3, 2, 1)
        chess.move_piece(3, 7, 3, 3)
        chess.move_piece(2, 1, 5, 1)

        queen_moves = chess.get_queen_moves(3, 3)
        valid_moves = [(2, 3), (1, 3), (4, 3), (5, 3), (3, 2), (3, 4), (3, 5),
                       (3, 6), (3, 7), (2, 2), (1, 1), (2, 4), (1, 5), (4, 2), (5, 1)]
        self.assertEqual(queen_moves, valid_moves)

        chess.move_piece(6, 7, 5, 7)
        chess.move_piece(5, 1, 5, 0)
        chess.move_piece(4, 4, 3, 4)

        queen_moves = chess.get_queen_moves(5, 0)
        valid_moves = [(4, 0), (3, 0), (2, 0), (6, 0), (5, 1), (5, 2),
                       (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (4, 1), (6, 1)]
        self.assertEqual(queen_moves, valid_moves)

    def test_king_move(self):
        chess = Chess()
        chess.move_piece(6, 4, 4, 4)
        chess.move_piece(1, 2, 3, 2)
        chess.move_piece(7, 3, 3, 7)
        chess.move_piece(0, 3, 2, 1)
        chess.move_piece(3, 7, 3, 3)
        chess.move_piece(2, 1, 5, 1)
        chess.move_piece(6, 7, 5, 7)
        chess.move_piece(5, 1, 5, 0)
        chess.move_piece(4, 4, 3, 4)
        chess.move_piece(1, 4, 2, 4)
        chess.move_piece(7, 4, 6, 4)
        chess.move_piece(0, 4, 1, 4)
        chess.move_piece(6, 3, 5, 3)

        king_moves = chess.get_moves('king', 'b', 1, 4)
        valid_moves = [(0, 4), (0, 3)]
        self.assertEqual(king_moves, valid_moves)

        chess.move_piece(6, 4, 5, 4)
        chess.move_piece(1, 3, 2, 3)

        king_moves = chess.get_moves('king', 'w', 5, 4)
        valid_moves = [(4, 4), (6, 4), (5, 5), (6, 3)]
        self.assertEqual(king_moves, valid_moves)

        pawn_moves = chess.get_pawn_moves('b', 5, 3)
        valid_moves = []
        self.assertEqual(pawn_moves, valid_moves)

    def test_knights_move(self):
        chess = Chess()
        chess.move_piece(7, 1, 5, 2)
        chess.move_piece(0, 6, 2, 5)
        chess.move_piece(5, 2, 3, 3)
        chess.move_piece(2, 5, 4, 6)

        valid_moves = [(1, 2), (2, 1), (4, 1), (5, 2),
                       (5, 4), (4, 5), (2, 5), (1, 4)]
        knight_moves = chess.get_moves('knight', 'w', 3, 3)
        self.assertEqual(knight_moves, valid_moves)

        chess.move_piece(6, 1, 5, 1)

        valid_moves = [(6, 7), (2, 7), (2, 5), (3, 4), (5, 4), (6, 5)]
        knight_moves = chess.get_moves('knight', 'b', 4, 6)
        self.assertEqual(knight_moves, valid_moves)

    def test_get_all_movements_for_pawns(self):
        chess = Chess()
        pawns_moves = chess.get_enemy_moves('b', True)
        valid_moves = [(2, 4), (2, 1), (2, 7), (3, 4), (3, 1), (3, 7), (2, 0),
                       (3, 0), (2, 3), (3, 3), (2, 6), (3, 6), (2, 2), (3, 2), (2, 5), (3, 5)]
        self.assertEqual(pawns_moves, valid_moves)

        pawns_moves = chess.get_enemy_moves('w', True)
        valid_moves = [(4, 4), (4, 0), (5, 5), (4, 3), (5, 4), (4, 6), (5, 1),
                       (4, 2), (5, 7), (4, 5), (5, 0), (5, 6), (5, 3), (4, 1), (4, 7), (5, 2)]
        self.assertEqual(pawns_moves, valid_moves)

    def test_is_check(self):
        chess = Chess()
        chess.move_piece(6, 4, 4, 4)
        chess.move_piece(1, 5, 3, 5)
        chess.move_piece(7, 3, 3, 7)

        is_check = chess.is_check(chess.board, 'b')
        self.assertTrue(is_check)

        chess.move_piece(1, 6, 2, 6)
        chess.move_piece(3, 7, 2, 6)

        is_check = chess.is_check(chess.board, 'b')
        self.assertTrue(is_check)

        chess.move_piece(1, 7, 2, 6)
        is_check = chess.is_check(chess.board, 'b')
        self.assertFalse(is_check)


if __name__ == '__main__':
    unittest.main()
