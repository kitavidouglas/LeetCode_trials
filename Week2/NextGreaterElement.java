package Week2;

import java.util.*;

public class NextGreaterElement {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> nextGreater = new HashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();

        // Find the next greater element for each element in nums2
        for (int num : nums2) {
            while (!stack.isEmpty() && stack.peek() < num) {
                nextGreater.put(stack.pop(), num);
            }
            stack.push(num);
        }

        // Initialize result array with -1
        int[] ans = new int[nums1.length];
        Arrays.fill(ans, -1);

        // Find the next greater element for each element in nums1
        for (int i = 0; i < nums1.length; i++) {
            int num = nums1[i];
            if (nextGreater.containsKey(num)) {
                ans[i] = nextGreater.get(num);
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        NextGreaterElement solution = new NextGreaterElement();

        // Example usage
        int[] nums1 = {4, 1, 2};
        int[] nums2 = {1, 3, 4, 2};
        System.out.println(Arrays.toString(solution.nextGreaterElement(nums1, nums2)));  // Output: [-1, 3, -1]

        int[] nums3 = {2, 4};
        int[] nums4 = {1, 2, 3, 4};
        System.out.println(Arrays.toString(solution.nextGreaterElement(nums3, nums4)));  // Output: [3, -1]
    }
}
