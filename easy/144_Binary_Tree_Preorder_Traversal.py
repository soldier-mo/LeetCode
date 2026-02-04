# description: https://leetcode.com/problems/binary-tree-preorder-traversal/description/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preOrderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node: Optional[TreeNode]):
            if node is None:
                return

            # node
            result.append(node.val)

            # left subtree
            traverse(node.left)

            # right subtree
            traverse(node.right)

        traverse(root)
        return result

    def preOrderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root] #LIFO
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


def main():
    #       2
    #      / \
    #     1   3

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    solution = Solution()
    print(solution.preOrderTraversalRecursive(root))
    print(solution.preOrderTraversalIterative(root))


main()
