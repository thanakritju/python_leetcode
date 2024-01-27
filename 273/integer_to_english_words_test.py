import unittest

from integer_to_english_words import Solution


class TestSolution(unittest.TestCase):
    def test_numberToWords(self):
        s = Solution()
        self.assertEqual(s.numberToWords(123), "One Hundred Twenty Three")
        self.assertEqual(s.numberToWords(1), "One")
        self.assertEqual(
            s.numberToWords(12345), "Twelve Thousand Three Hundred Forty Five"
        )

    def test_numberToWordsBase(self):
        s = Solution()
        self.assertEqual(s.numberToWordsBase(1), ["One"])
        self.assertEqual(s.numberToWordsBase(12), ["Twelve"])


if __name__ == "__main__":
    unittest.main()
