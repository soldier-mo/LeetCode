# description: https://leetcode.com/problems/palindrome-linked-list/description/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second_half = prev
        first_half = head

        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True


def main():
    solver = Solution()

    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(2)
    root.next.next.next = ListNode(1)

    print(solver.isPalindrome(root))


main()
