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
        self.assertEqual(
            s.numberToWords(1234567),
            "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        )
        self.assertEqual(
            s.numberToWords(1234567891),
            "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One",
        )
        self.assertEqual(
            s.numberToWords(111),
            "One Hundred Eleven",
        )
        self.assertEqual(
            s.numberToWords(1000),
            "One Thousand",
        )
        self.assertEqual(
            s.numberToWords(1000000),
            "One Million",
        )
        self.assertEqual(
            s.numberToWords(1000000000),
            "One Billion",
        )
        self.assertEqual(
            s.numberToWords(0),
            "Zero",
        )

    def test_numberToWordsBase(self):
        s = Solution()
        self.assertEqual(s.numberToWordsBase(1), ["One"])
        self.assertEqual(s.numberToWordsBase(0), ["Zero"])
        self.assertEqual(s.numberToWordsBase(12), ["Twelve"])


if __name__ == "__main__":
    unittest.main()
