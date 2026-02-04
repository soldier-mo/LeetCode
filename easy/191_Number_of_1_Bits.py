# description: https://leetcode.com/problems/number-of-1-bits/description/


class Solution:
    def hammingWeight(self, n: int) -> int:
        #normal
        return bin(n).count('1')
    
        #better
        return len([x for x in bin(n) if x == '1'])
    
        #best
        count = 0
        while n:
            n &= (n - 1)  # Entfernt das niedrigste gesetzte Bit
            count += 1
        return count

def main():
    solver = Solution()
    n = 11
    n1 = 2147483645

    print(solver.hammingWeight(n))
    print(solver.hammingWeight(n1))


main()
