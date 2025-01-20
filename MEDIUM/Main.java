/*  Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, 
and return the reversed list. 

*/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        int n = 2;
        ListNode newHead = solution.removeNthFromEnd(head, n);
        printList(newHead); // Output: [1, 2, 3, 5]
    }

    public static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.println();
    }
}
