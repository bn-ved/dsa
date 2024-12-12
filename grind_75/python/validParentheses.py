from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stk: List[str] = []
        for char in s:
            if char == "(":
                stk.append(")")
            elif char == "[":
                stk.append("]")
            elif char == "{":
                stk.append("}")
            elif len(stk) == 0 or stk.pop() != char:
                return False
        return True
