# description: https://leetcode.com/problems/pascals-triangle-ii/description/
from typing import List
from unittest import result


class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        triangle = []

        for i in range(rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle[rowIndex]


def main():
    solver = Solution()
    rowIndex = 3
    rowIndex2 = 0

    print(solver.getRow(rowIndex))
    print(solver.getRow(rowIndex2))


main()
