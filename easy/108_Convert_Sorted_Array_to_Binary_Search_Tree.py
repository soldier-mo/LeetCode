#Description: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root
    

#####################################
#               Helper              # 
#####################################

def print_tree(node, level=0, label="."):
    # !GENERATED WITH AI!
    if node is not None:
        print(" " * (level * 4) + label + ": " + str(node.val))
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")


###################################
#               main              # 
###################################

def main():
    nums = [-10, -3, 0, 5, 9]
    solution = Solution()
    bst_root = solution.sortedArrayToBST(nums)
    print_tree(bst_root)

if __name__ == "__main__":
    main()
