#Description: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #s1: Normal loop
        # while k > 0:
        #     nums.insert(0,nums.pop(len(nums)-1))
        #     k -= 1

        #s2: swap k ranges
        k = k % len(nums)
        if k != 0: #if k == 0 we have same arr
            nums[:k], nums[k:] = nums[-k:], nums[:-k]   

def main():
    nums = [1,2,3,4,5,6,7]

    s = Solution()
    print(s.rotate(nums, 3))
main()