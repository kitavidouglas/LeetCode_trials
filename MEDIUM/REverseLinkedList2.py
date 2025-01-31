''' Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

 '''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head  # No need to reverse if only one node or left == right
        
        dummy = ListNode(0)  # Dummy node to handle edge cases
        dummy.next = head
        prev = dummy

        # Step 1: Move `prev` to the node before `left`
        for _ in range(left - 1):
            prev = prev.next
        
        # Step 2: Reverse the sublist
        curr = prev.next
        next_node = None
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next  # Return the modified list

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Sample main function for testing
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head = create_linked_list([1, 2, 3, 4, 5])
    new_head = solution.reverseBetween(head, 2, 4)
    print_linked_list(new_head)  # Expected output: [1, 4, 3, 2, 5]

    # Test case 2
    head = create_linked_list([5])
    new_head = solution.reverseBetween(head, 1, 1)
    print_linked_list(new_head)  # Expected output: [5]
