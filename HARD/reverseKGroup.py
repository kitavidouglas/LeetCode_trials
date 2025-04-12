# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Check if there are at least k nodes left in the list.
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # Node after the kth node.
            # Reverse the group.
            prev, curr = group_next, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Will become the tail of the reversed group.
            group_prev.next = kth  # Connect previous part with new head (kth node).
            group_prev = temp  # Move group_prev pointer to the tail of the reversed group.

        return dummy.next
