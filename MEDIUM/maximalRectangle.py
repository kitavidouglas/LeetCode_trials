''''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        max_area = 0
        cols = len(matrix[0])
        # Initialize heights array with an extra 0 at the end to handle remaining bars
        heights = [0] * (cols + 1)
        
        for row in matrix:
            # Update the histogram heights
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # Compute largest rectangle in histogram for the current row
            stack = []
            for i in range(cols + 1):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    # Determine the width of the rectangle
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * width)
                stack.append(i)
                
        return max_area
