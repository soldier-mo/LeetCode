#description: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        if not head:
            return

        while head.next is not None:
            if head.val != head.next.val:
                tail.val = head.val
                tail.next = ListNode()
                tail = tail.next
                head = head.next

            else:
                head = head.next
        tail.val = head.val
        return dummy


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
    head = []
    print(solver.deleteDuplicates(arr_to_linked_list(head)))
main()