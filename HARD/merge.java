import java.util.PriorityQueue;

class Solution {
    public <ListNode> ListNode mergeKLists(ListNode[] lists) {
        // Base case: if the lists array is null or empty, return null
        if (lists == null || lists.length == 0) {
            return null;
        }

        // Create a priority queue (min-heap) to store nodes, sorted by their values
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);

        // Add the head of each non-empty linked list to the priority queue
        for (ListNode list : lists) {
            if (list != null) {
                minHeap.add(list);
            }
        }

        // Create a dummy node to build the merged list
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        // Process the priority queue until it's empty
        while (!minHeap.isEmpty()) {
            // Extract the smallest node from the priority queue
            ListNode smallest = minHeap.poll();
            current.next = smallest;
            current = current.next;

            // If the extracted node has a next node, add it to the priority queue
            if (smallest.next != null) {
                minHeap.add(smallest.next);
            }
        }

        // Return the merged list starting from dummy.next
        return dummy.next;
    }
}
