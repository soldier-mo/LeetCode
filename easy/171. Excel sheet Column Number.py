# description: https://leetcode.com/problems/excel-sheet-column-number/description/


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for v in columnTitle:
            charIndexInAlphabet = ord(v) - ord('A') + 1  # A = 1 ... Z = 26
            result = result * 26 + charIndexInAlphabet

        return result


def main():
    solver = Solution()
    columnTitle = "A"
    columnTitle2 = "AAA"
    columnTitle3 = "ZY"

    print(solver.titleToNumber(columnTitle))
    print(solver.titleToNumber(columnTitle2))
    print(solver.titleToNumber(columnTitle3))


main()
