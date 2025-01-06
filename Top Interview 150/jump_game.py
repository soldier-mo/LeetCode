#Description: https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy-Algorithm
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i + nums[i])

            if max_reach >= len(nums) - 1:
                return True

        return False

def main():
    s = Solution()
    # print(s.canJump([2,3,1,1,4])) 
    print(s.canJump([3,0,8,2,0,0,1]))
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
main()