# description: https://leetcode.com/problems/reverse-bits/description/


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Shift result left and add the last bit of n
            result = (result << 1) | (n & 1)
            n >>= 1  # Shift n right
        return result

def main():
    solver = Solution()
    n = 0b00000010100101000001111010011100
    n1 = 0b11111111111111111111111111111101

    print(solver.reverseBits(n))
    print(solver.reverseBits(n1))


main()
