# description: https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev


def array_to_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def main():
    s = Solution()
    l = array_to_linked_list([1, 2, 3, 4, 5])
    print(s.reverseList(l))
    print(l)


main()
