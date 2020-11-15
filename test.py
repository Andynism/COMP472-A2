import unittest
import puzzle

class TestPuzzle(unittest.TestCase):

    def test_check_puzzle_1(self):
        p_complete_1 = puzzle.Puzzle([1, 2, 3, 4, 5, 6, 7, 0])
        assert(p_complete_1.check_puzzle_1())
        assert(p_complete_1.zero == 7)
        assert(p_complete_1.in_first_col == False)
        assert(p_complete_1.in_first_row == False)
        assert(p_complete_1.in_last_col == True)
        assert(p_complete_1.in_last_row == True)

        p_incomplete_1 = puzzle.Puzzle([0, 1, 2, 3, 4, 5, 6, 7])
        assert(p_incomplete_1.check_puzzle_1() == False)
        assert(p_incomplete_1.zero == 0)
        assert(p_incomplete_1.in_first_col == True)
        assert(p_incomplete_1.in_first_row == True)
        assert(p_incomplete_1.in_last_col == False)
        assert(p_incomplete_1.in_last_row == False)

    def test_check_puzzle_2(self):
        p_complete_2 = puzzle.Puzzle([1, 3, 5, 7, 2, 4, 6, 0])
        assert(p_complete_2.check_puzzle_2())
        assert(p_complete_2.zero == 7)
        assert(p_complete_2.in_first_col == False)
        assert(p_complete_2.in_first_row == False)
        assert(p_complete_2.in_last_col == True)
        assert(p_complete_2.in_last_row == True)

        p_incomplete_2 = puzzle.Puzzle([4, 2, 0, 6, 1, 3, 5, 7])
        assert(p_incomplete_2.check_puzzle_2() == False)
        assert(p_incomplete_2.zero == 2)
        assert(p_incomplete_2.in_first_col == False)
        assert(p_incomplete_2.in_first_row == True)
        assert(p_incomplete_2.in_last_col == False)
        assert(p_incomplete_2.in_last_row == False)

    def test_up(self):
        p = puzzle.Puzzle([3, 4, 7, 6, 1, 2, 5, 0])
        up = p.up()
        self.assertEqual(up.cost, 1)
        self.assertEqual(up.zero, 3)
        self.assertEqual(up.arr, [3, 4, 7, 0, 1, 2, 5, 6])
        # Assert original puzzle unchanged
        self.assertEqual(p.cost, 0)
        self.assertEqual(p.zero, 7)
        self.assertEqual(p.arr, [3, 4, 7, 6, 1, 2, 5, 0])
        

    def test_down(self):
        p = puzzle.Puzzle([3, 4, 0, 6, 1, 2, 5, 7])
        down = p.down()
        self.assertEqual(down.cost, 1)
        self.assertEqual(down.zero, 6)
        self.assertEqual(down.arr, [3, 4, 5, 6, 1, 2, 0, 7])

    def test_left(self):
        p = puzzle.Puzzle([3, 4, 0, 6, 1, 2, 5, 7])
        left = p.left()
        self.assertEqual(left.cost, 1)
        self.assertEqual(left.zero, 1)
        self.assertEqual(left.arr, [3, 0, 4, 6, 1, 2, 5, 7])

    def test_right(self):
        p = puzzle.Puzzle([3, 4, 0, 6, 1, 2, 5, 7])
        right = p.right()
        self.assertEqual(right.cost, 1)
        self.assertEqual(right.zero, 3)
        self.assertEqual(right.arr, [3, 4, 6, 0, 1, 2, 5, 7])

    def test_wrap_first_col(self):
        p = puzzle.Puzzle([3, 4, 1, 6, 0, 2, 5, 7])
        left = p.left()
        self.assertEqual(left.cost, 2)
        self.assertEqual(left.zero, 7)
        self.assertEqual(left.arr, [3, 4, 1, 6, 7, 2, 5, 0])

    def test_wrap_last_col(self):
        p = puzzle.Puzzle([3, 4, 6, 0, 1, 2, 5, 7])
        right = p.right()
        self.assertEqual(right.cost, 2)
        self.assertEqual(right.zero, 0)
        self.assertEqual(right.arr, [0, 4, 6, 3, 1, 2, 5, 7])

    def test_top_left_corner(self):
        p = puzzle.Puzzle([0, 1, 2, 3, 4, 5, 6, 7])
        moves = p.corner()
        self.assertEqual(moves[0].cost, 3)
        self.assertEqual(moves[0].zero, 5)
        self.assertEqual(moves[0].arr, [5, 1, 2, 3, 4, 0, 6, 7])
        self.assertEqual(moves[1].cost, 3)
        self.assertEqual(moves[1].zero, 7)
        self.assertEqual(moves[1].arr, [7, 1, 2, 3, 4, 5, 6, 0])

    def test_top_right_corner(self):
        p = puzzle.Puzzle([1, 2, 3, 0, 4, 5, 6, 7])
        moves = p.corner()
        self.assertEqual(moves[0].cost, 3)
        self.assertEqual(moves[0].zero, 6)
        self.assertEqual(moves[0].arr, [1, 2, 3, 6, 4, 5, 0, 7])
        self.assertEqual(moves[1].cost, 3)
        self.assertEqual(moves[1].zero, 4)
        self.assertEqual(moves[1].arr, [1, 2, 3, 4, 0, 5, 6, 7])

    def test_bottom_left_corner(self):
        p = puzzle.Puzzle([1, 2, 3, 4, 0, 5, 6, 7])
        moves = p.corner()
        self.assertEqual(moves[0].cost, 3)
        self.assertEqual(moves[0].zero, 1)
        self.assertEqual(moves[0].arr, [1, 0, 3, 4, 2, 5, 6, 7])
        self.assertEqual(moves[1].cost, 3)
        self.assertEqual(moves[1].zero, 3)
        self.assertEqual(moves[1].arr, [1, 2, 3, 0, 4, 5, 6, 7])

    def test_bottom_right_corner(self):
        p = puzzle.Puzzle([1, 2, 3, 4, 5, 6, 7, 0])
        moves = p.corner()
        self.assertEqual(moves[0].cost, 3)
        self.assertEqual(moves[0].zero, 2)
        self.assertEqual(moves[0].arr, [1, 2, 0, 4, 5, 6, 7, 3])
        self.assertEqual(moves[1].cost, 3)
        self.assertEqual(moves[1].zero, 0)
        self.assertEqual(moves[1].arr, [0, 2, 3, 4, 5, 6, 7, 1])

if __name__ == '__main__':
    unittest.main()