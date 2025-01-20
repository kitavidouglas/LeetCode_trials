class Solution:
    def isValidSudoku(self, board):
        # Create sets for rows, columns, and sub-boxes
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        # Iterate through each cell of the board
        for i in range(9):
            for j in range(9):
                current = board[i][j]

                # If the cell is empty, skip it
                if current == '.':
                    continue

                # Convert the digit character to an index (0-based)
                num = int(current) - 1

                # Calculate the box index
                box_index = (i // 3) * 3 + (j // 3)

                # Check if the number already exists in the current row, column, or box
                if rows[i][num] or cols[j][num] or boxes[box_index][num]:
                    return False

                # Mark the number as seen in the row, column, and box
                rows[i][num] = True
                cols[j][num] = True
                boxes[box_index][num] = True

        # If no conflicts were found, the board is valid
        return True
