#Given an m x n board of characters and a list of strings words, return all words on the board.

#Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
#The same letter cell may not be used more than once in a word.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # This will hold the word if the node represents the end of a word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def build_trie(words):
            root = TrieNode()
            for word in words:
                node = root
                for letter in word:
                    if letter not in node.children:
                        node.children[letter] = TrieNode()
                    node = node.children[letter]
                node.word = word  # Mark the end of the word
            return root
        
        def backtrack(row, col, parent):
            letter = board[row][col]
            current_node = parent.children[letter]
            
            # If we find a word, add it to the result
            if current_node.word:
                result.append(current_node.word)
                current_node.word = None  # Avoid duplicate words
            
            # Mark the current cell as visited
            board[row][col] = '#'
            
            # Explore all possible directions (up, down, left, right)
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != '#':
                    if board[r][c] in current_node.children:
                        backtrack(r, c, current_node)
            
            # Restore the current cell after exploring
            board[row][col] = letter
            
            # Prune the trie if the current node has no children
            if not current_node.children:
                del parent.children[letter]
        
        # Edge case: if board is empty or no words are given
        if not board or not words:
            return []
        
        # Build the Trie from the given words
        trie_root = build_trie(words)
        result = []
        
        # Start backtracking from every cell in the board
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie_root.children:
                    backtrack(row, col, trie_root)
        
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]
    
    print(solution.findWords(board, words))
