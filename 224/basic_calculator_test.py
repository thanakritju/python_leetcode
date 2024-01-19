import unittest

import basic_calculator


class TestSolution(unittest.TestCase):
    def test_calculate(self):
        s = basic_calculator.Solution()
        self.assertEqual(s.calculate("-1"), -1)
        self.assertEqual(s.calculate("1 + 1"), 2)
        self.assertEqual(s.calculate(" 2-1 + 2 "), 3)
        self.assertEqual(s.calculate("(1+(4+5+2)-3)+(6+8)"), 23)
        self.assertEqual(s.calculate("   (  3 ) "), 3)
        self.assertEqual(s.calculate("-(2 + 3)"), -5)

    def test_calculate_list(self):
        s = basic_calculator.Solution()
        self.assertEqual(s.calculate_list(["3"]), 3)
        self.assertEqual(s.calculate_list(["-", "3"]), -3)
        self.assertEqual(s.calculate_list(["1", "+", "1"]), 2)
        self.assertEqual(s.calculate_list(["1", "-", "3"]), -2)
        self.assertEqual(s.calculate_list(["2", "-", "1", "+", "2"]), 3)

    def test_tokenize(self):
        s = basic_calculator.Solution()
        self.assertEqual(s.tokenize("1 + 1"), ["1", "+", "1"])
        self.assertEqual(s.tokenize("   (  3 ) "), ["(", "3", ")"])
        self.assertEqual(s.tokenize(" 2-1 + 2 "), ["2", "-", "1", "+", "2"])
        self.assertEqual(
            s.tokenize("(1+(4+25)-3)"),
            ["(", "1", "+", "(", "4", "+", "25", ")", "-", "3", ")"],
        )


if __name__ == "__main__":
    unittest.main()
