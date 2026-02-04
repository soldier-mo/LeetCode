# Description: https://leetcode.com/problems/balanced-binary-tree/description/
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: TreeNode) -> int:
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return height(root) != -1
    

###################################
#               main              #
###################################

def main():
    def new_node(val):
        return TreeNode(val)

    root1 = new_node(3)
    root1.left = new_node(9)
    root1.right = new_node(20)
    root1.right.left = new_node(15)
    root1.right.right = new_node(7)

    solution = Solution()
    
    print(solution.isBalanced(root1))  # Expected output: True

main()