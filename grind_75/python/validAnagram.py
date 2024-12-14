class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map: dict[str, int] = {}

        for a, b in zip(s, t):
            map[a] = map.get(a, 0) + 1
            map[b] = map.get(b, 0) - 1

        for value in map.values():
            if value != 0:
                return False
        return True
