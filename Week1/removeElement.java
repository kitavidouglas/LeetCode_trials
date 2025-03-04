package Week1;

public class removeElement {
    public int RemoveElement(int[] nums, int val) {
        int count = 0; // Initialize count for elements not equal to val
        
        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            // If the current element is not equal to val
            if (nums[i] != val) {
                // Keep the element and update the count
                nums[count] = nums[i];
                count++;
            }
        }
        
        // Return the count of elements not equal to val
        return count;
    }

    public static void main(String[] args) {
        removeElement solution = new removeElement();
        int[] nums = {4,9,7,4};
        int val = 4;
        int k = solution.RemoveElement(nums, val);
        System.out.println("Number of elements in nums which are not equal to val: " + k);
        System.out.print("Modified nums array: ");
        for (int i = 0; i < k; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}

