'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.  CONFIRM'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Create a dummy node to start the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both lists
        while l1 or l2 or carry:
            # Get the values from both lists, if available
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Sum the values and the carry from the previous operation
            total = val1 + val2 + carry
            
            # Update carry for the next iteration
            carry = total // 10
            
            # The current digit is the remainder of the total divided by 10
            current.next = ListNode(total % 10)
            
            # Move the current pointer to the next node
            current = current.next
            
            # Move to the next nodes in l1 and l2 if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        # Return the next of dummy_head which points to the start of the result list
        return dummy_head.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy_head = ListNode()
    current = dummy_head
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

# Helper function to print the linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Sample main function to compute sample values
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: l1 = [2, 4, 3], l2 = [5, 6, 4]
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print("Result of adding l1 and l2:")
    print_linked_list(result)  # Expected output: 7 -> 0 -> 8

    # Test case 2: l1 = [9], l2 = [1]
    l1 = create_linked_list([9])
    l2 = create_linked_list([1])
    result = solution.addTwoNumbers(l1, l2)
    print("Result of adding l1 and l2:")
    print_linked_list(result)  # Expected output: 0 -> 1

    # Test case 3: l1 = [9, 9, 9], l2 = [1]
    l1 = create_linked_list([9, 9, 9])
    l2 = create_linked_list([1])
    result = solution.addTwoNumbers(l1, l2)
    print("Result of adding l1 and l2:")
    print_linked_list(result)  # Expected output: 0 -> 0 -> 0 -> 1
