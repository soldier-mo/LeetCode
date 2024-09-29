#Description: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0;
        counter = 1
        while i < len(nums)-1:
            if nums[i] == nums[i + 1]:
                if counter >= 2:
                    nums.pop(i + 1)
                else:
                    counter += 1
                    i += 1
            else:
                counter = 1
                i += 1
        return i+1
    
def main():
    nums = [0,0,1,1,1,1,2,3,3]

    solution = Solution()
    k = solution.removeDuplicates(nums)

    print(nums)

main()

