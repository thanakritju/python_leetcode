from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ans = []
        billion = num // 1000000000
        if billion > 0:
            ans = ans + self.numberToWordsBase(billion)
            ans.append("Billion")
            num = num % 1000000000
        million = num // 1000000
        if million > 0:
            ans = ans + self.numberToWordsBase(million)
            ans.append("Million")
            num = num % 1000000
        thousand = num // 1000
        if thousand > 0:
            ans = ans + self.numberToWordsBase(thousand)
            ans.append("Thousand")
            num = num % 1000
        if num > 0:
            ans = ans + self.numberToWordsBase(num)

        return " ".join(ans)

    def numberToWordsBase(self, num: int) -> List[str]:
        ans = []
        digitmaps = {
            0: "Zero",
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
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }
        if num in digitmaps.keys():
            ans.append(digitmaps[num])
            return ans
        if (num % 1000) // 100 > 0:
            ans.append(digitmaps[(num % 1000) // 100])
            ans.append("Hundred")
        if (num % 100) // 10 > 0:
            if num % 100 in digitmaps.keys():
                ans.append(digitmaps[num % 100])
                return ans
            ans.append(digitmaps[((num % 100) // 10) * 10])
        if num % 10 != 0:
            ans.append(digitmaps[num % 10])
        return ans
