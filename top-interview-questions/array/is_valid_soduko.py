import unittest

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    if ((num, 'in row', i) in seen or 
                        (num, 'in column', j) in seen or 
                        (num, 'in block', i//3, j//3) in seen):
                        return False
                    seen.add((num, 'in row', i))
                    seen.add((num, 'in column', j))
                    seen.add((num, 'in block', i//3, j//3))
        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isValidSudoku_valid_board(self):
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertTrue(self.solution.isValidSudoku(board))

    def test_isValidSudoku_invalid_board(self):
        board = [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertFalse(self.solution.isValidSudoku(board))

if __name__ == '__main__':
    unittest.main()
