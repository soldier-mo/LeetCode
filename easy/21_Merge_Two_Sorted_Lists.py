#description: https://leetcode.com/problems/merge-two-sorted-lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 if list1 is not None else list2
        
        return dummy.next

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
    solver = Solution()
    list1 = arr_to_linked_list([1,2,4])
    list2 = arr_to_linked_list([1,3,4])
    print(solver.mergeTwoLists(list1, list2))

main()
