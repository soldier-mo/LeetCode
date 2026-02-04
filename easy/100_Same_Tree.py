#description: https://leetcode.com/problems/same-tree/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        # make sure both q & p exists
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#####################################
#               Helper              # 
#####################################

def create_tree_from_list(lst):
    if not lst:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

###################################
#               main              # 
###################################

def main():
    p = create_tree_from_list([1,2,3])
    q = create_tree_from_list([1,2,3])
    solver = Solution()
    print(solver.isSameTree(p,q))
main()
