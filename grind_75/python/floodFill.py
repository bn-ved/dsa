from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        R, C, prevColor = len(image), len(image[0]), image[sr][sc]
        if prevColor == color:
            return image

        def dfs(r, c):
            if image[r][c] == prevColor:
                image[r][c] = color
                if r + 1 < R:
                    dfs(r + 1, c)
                if r - 1 >= 0:
                    dfs(r - 1, c)
                if c + 1 < C:
                    dfs(r, c + 1)
                if c - 1 >= 0:
                    dfs(r, c - 1)

        dfs(sr, sc)
        return image
