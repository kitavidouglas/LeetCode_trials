'''
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

'''
class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # Step 1: Sort meetings by start time
        meetings.sort()
        
        # Step 2: Merge overlapping intervals
        merged_days = 0
        prev_start, prev_end = -1, -1

        for start, end in meetings:
            if start > prev_end:  # Non-overlapping meeting
                merged_days += (end - start + 1)
            else:  # Overlapping meeting
                merged_days += max(0, end - prev_end)
            
            prev_end = max(prev_end, end)  # Update last merged end
        
        # Step 3: Compute free days
        return days - merged_days
