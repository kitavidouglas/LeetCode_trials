/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
/*  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
*/
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create sets for rows, columns, and sub-boxes to store seen numbers
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        // Iterate through each cell of the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is empty, skip it
                if (current == '.') {
                    continue;
                }

                // Convert the digit character to an index (0-based)
                int num = current - '1';

                // Check if the number already exists in the current row, column, or box
                if (rows[i][num] || cols[j][num] || boxes[(i / 3) * 3 + j / 3][num]) {
                    return false;
                }

                // Mark the number as seen in the row, column, and box
                rows[i][num] = true;
                cols[j][num] = true;
                boxes[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        // If no conflicts were found, the board is valid
        return true;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeNthFromEnd'");
    }
}
