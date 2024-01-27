import unittest

from find_minimum_in_rotated_sorted_array import Solution


class TestSolution(unittest.TestCase):
    def test_findMin(self):
        s = Solution()
        self.assertEqual(s.findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(s.findMin([3, 4, 5, 1, 2, 2, 2, 3]), 1)
        self.assertEqual(s.findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(s.findMin([11, 13, 15, 17]), 11)


if __name__ == "__main__":
    unittest.main()
