''' Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swapping nodes
            prev.next = second
            first.next = second.next
            second.next = first

            # Moving to the next pair
            prev = first
            head = first.next

        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Example usage:
head = create_linked_list([1, 2, 3, 4])
solution = Solution()
new_head = solution.swapPairs(head)
print_linked_list(new_head)  # Output: [2, 1, 4, 3]
