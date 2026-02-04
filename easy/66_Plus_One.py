#description: https://leetcode.com/problems/plus-one/description/
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in list(str(int("".join([str(x) for x in digits]))+1))]
    
def main():
    digits = [1,2,3]
    solver = Solution()
    print(solver.plusOne(digits))
main()
