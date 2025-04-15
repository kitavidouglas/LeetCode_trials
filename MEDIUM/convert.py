class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge cases: if only one row (or string too short), it's unchanged
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Prepare a list of buffers, one per row
        rows = [''] * numRows
        cur_row = 0
        going_down = False
        
        # Walk through each character, toggling direction at the top/bottom
        for c in s:
            rows[cur_row] += c
            # reverse direction if we're at the first or last row
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            # step up or down
            cur_row += 1 if going_down else -1
        
        # Join all rows to get the final string
        return ''.join(rows)
