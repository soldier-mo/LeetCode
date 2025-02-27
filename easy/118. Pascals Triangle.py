# description: https://leetcode.com/problems/pascals-triangle/description/
from typing import List
from unittest import result


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle


def main():
    solver = Solution()
    numRows = 5
    numRows2 = 1

    print(solver.generate(numRows))
    print(solver.generate(numRows2))


main()
