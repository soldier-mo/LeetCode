# description: https://leetcode.com/problems/zigzag-conversion/description/


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        arr = [[] for _ in range(numRows)]

        row = 0
        direction = 1

        for i in s:
            arr[row].append(i)
            row += direction

            if row <= 0 or row >= numRows - 1:
                direction *= -1

        return "".join(["".join(x) for x in arr])


def main():
    solution = Solution()
    s = "PAYPALISHIRING"

    print(solution.convert(s, 4) == "PINALSIGYAHRPI")


main()
