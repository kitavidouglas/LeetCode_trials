#Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Add a zero-height bar at the end to ensure the stack is fully processed
        heights.append(0)
        stack = []  # Stack to store indices of histogram bars
        max_area = 0
        
        for i, h in enumerate(heights):
            # Process the stack until the current height is greater than the height at the stack's top
            while stack and heights[stack[-1]] > h:
                # Pop the top of the stack
                height = heights[stack.pop()]
                # Calculate the width
                width = i if not stack else i - stack[-1] - 1
                # Update the maximum area
                max_area = max(max_area, height * width)
            # Push the current index onto the stack
            stack.append(i)
        
        return max_area


# Example usage
if __name__ == "__main__":
    
    solution = Solution()
    
    # Example 1
    heights1 = [2, 1, 5, 6, 2, 3]
    print("Largest Rectangle Area for [2, 1, 5, 6, 2, 3]:", solution.largestRectangleArea(heights1))
    
    # Example 2
    heights2 = [2, 4]
    print("Largest Rectangle Area for [2, 4]:", solution.largestRectangleArea(heights2))
    
    # Example 3
    heights3 = [6, 2, 5, 4, 5, 1, 6]
    print("Largest Rectangle Area for [6, 2, 5, 4, 5, 1, 6]:", solution.largestRectangleArea(heights3))

