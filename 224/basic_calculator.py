from typing import List
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        q = deque()
        tokens = self.tokenize(s)
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == ")":
                l = deque()
                each = q.pop()
                while True:
                    if each != "(":
                        l.appendleft(each)
                        each = q.pop()
                    else:
                        break
                q.append(str(self.calculate_list(l)))

            else:
                if token in ["(", "+", "-"]:
                    q.append(token)
                else:
                    q.append(int(token))
            i += 1

        return self.calculate_list(q)

    def calculate_list(self, l: List[str]) -> int:
        ans = 0
        operation = ""
        for token in l:
            if token not in ["+", "-"]:
                if operation == "-":
                    ans -= int(token)
                else:
                    ans += int(token)
            else:
                operation = token
        return ans

    def tokenize(self, s: str) -> List[str]:
        ans = []
        cur = ""
        for c in s:
            if c in ["(", ")", "+", "-"]:
                if cur != "":
                    ans.append(cur.strip())
                    cur = ""
                ans.append(c.strip())
            elif c != " ":
                cur += c

        if cur != "":
            ans.append(cur.strip())
            cur = ""

        return ans
