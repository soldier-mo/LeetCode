#description: https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next

def linked_list_to_arr(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr           

def arr_to_linked_list(arr):
    if not arr: 
        return None
    
    original = ListNode()
    current = original
    for v in arr:
        current.next = ListNode(v)
        current = current.next
    return original.next

def main():
    l1 = arr_to_linked_list([2,4,3])
    l2 = arr_to_linked_list([5,6,4])
    s = Solution()
    print(linked_list_to_arr(s.addTwoNumbers(l1, l2)))
main()
