package Week1;

public class searchInsert {
    public int SearchInsert(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= target) {
                return i; // Return the index if target is found or the position to insert
            }
        }
        return nums.length; // If the target is greater than all elements, insert at the end
    }

    public static void main(String[] args) {
        searchInsert solution = new searchInsert();
        int[] nums = {76, 93, 65, 86};
        int target = 86;
        int index = solution.SearchInsert(nums, target);
        System.out.println("Index of target or the position to insert it: " + index);
    }
}
