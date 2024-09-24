#Description: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0;
        while i < len(nums)-1:
            if nums[i] == nums[i + 1]:
                nums.pop(i+1)
            else:
                i += 1
        return i+1
    
def main():
    nums = [-1,0,0,0,0,3,3]

    solution = Solution()
    k = solution.removeDuplicates(nums)

    print(nums)

main()

