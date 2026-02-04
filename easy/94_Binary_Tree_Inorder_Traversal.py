#description: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node: Optional[TreeNode]):
            if node is None:
                return
            
            # left subtree
            traverse(node.left)
            # node
            result.append(node.val)
            # right subtree
            traverse(node.right)
        
        traverse(root)
        return result

def main():
    #       2
    #      / \
    #     1   3

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    solution = Solution()
    print(solution.inorderTraversal(root))
main()
