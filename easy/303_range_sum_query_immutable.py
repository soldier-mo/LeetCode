# description: https://leetcode.com/problems/range-sum-query-immutable/description/

class NumArray(object):

    def __init__(self, nums):
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1] + n)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)

def main():
    n = [-2,0,3,-5,2,-1] 
    num_arr = NumArray(n)
    print(num_arr.sumRange(0,2))
    print(num_arr.sumRange(2,5))
    print(num_arr.sumRange(0,5))

main()
