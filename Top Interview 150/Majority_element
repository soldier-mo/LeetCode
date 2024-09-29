#Description: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        if nums.count(candidate) > len(nums) // 2:
            return candidate


def main():
    nums = [2,2,2,1]

    s = Solution()
    print(s.majorityElement(nums))
main()