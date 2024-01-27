from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        ans = []
        thousand = num // 1000
        if thousand > 0:
            ans = ans + self.numberToWordsBase(thousand)
            ans.append("Thousand")
        hundred = num % 1000
        ans = ans + self.numberToWordsBase(hundred)

        return " ".join(ans)

    def numberToWordsBase(self, num: int) -> List[str]:
        ans = []
        digitmaps = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirdteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
        }
        if (num % 1000) // 100 > 0:
            ans.append(digitmaps[(num % 1000) // 100])
            ans.append("Hundred")
        if (num % 100) // 10 > 0:
            ans.append(digitmaps[((num % 100) // 10) * 10])
        if num % 10 != 0:
            ans.append(digitmaps[num % 10])
        return ans
