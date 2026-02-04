# description: https://leetcode.com/problems/excel-sheet-column-title/description/


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return "".join(result[::-1])


def main():
    solver = Solution()
    columnNumber = 1
    columnNumber2 = 28
    columnNumber3 = 701

    print(solver.convertToTitle(columnNumber))
    print(solver.convertToTitle(columnNumber2))
    print(solver.convertToTitle(columnNumber3))


main()
