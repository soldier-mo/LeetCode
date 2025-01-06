#Description: https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:
        min_need = float('inf')
        if len(nums) == 1:
            return 0
        
        if nums[0] >= len(nums)-1:
            return 1
 
            min_need = min(min_need, self.jump(nums[i+1:]) + 1)
            
        return min_need


def main():
    s = Solution()
    # print(s.jump([3,1,1,1,1,1,1,0]))
    # print(s.jump([2,1,1,1,1])) 
    # print(s.jump([2,3,1,0,4]))
    print(s.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))
main()