''' Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
 You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        # Helper function to perform backtracking
        def backtrack(start, target, current_combination):
            # If target becomes 0, we found a valid combination
            if target == 0:
                result.append(list(current_combination))
                return
            
            # Try all candidates starting from the 'start' index
            for i in range(start, len(candidates)):
                # If the candidate is greater than the remaining target, no point in exploring further
                if candidates[i] > target:
                    continue
                # Add current candidate to the combination
                current_combination.append(candidates[i])
                # Recurse with reduced target (we don't increment 'i' because we can reuse candidates)
                backtrack(i, target - candidates[i], current_combination)
                # Backtrack, remove the last added element
                current_combination.pop()
        
        result = []
        backtrack(0, target, [])
        return result

# Sample main function to compute sample values
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Candidates = [2, 3, 6, 7], Target = 7
    candidates = [2, 3, 6, 7]
    target = 7
    print(f"Combination sums for target {target} with candidates {candidates}: {solution.combinationSum(candidates, target)}")

    # Test case 2: Candidates = [2, 3, 5], Target = 8
    candidates = [2, 3, 5]
    target = 8
    print(f"Combination sums for target {target} with candidates {candidates}: {solution.combinationSum(candidates, target)}")

    # Test case 3: Candidates = [2], Target = 1
    candidates = [2]
    target = 1
    print(f"Combination sums for target {target} with candidates {candidates}: {solution.combinationSum(candidates, target)}")

    # Test case 4: Candidates = [1], Target = 4
    candidates = [1]
    target = 4
    print(f"Combination sums for target {target} with candidates {candidates}: {solution.combinationSum(candidates, target)}")
